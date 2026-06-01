/**
 * flyer.ts — winged-creature rig (birds, bats, wyverns, fairies).
 *
 * Anatomy: a small body (head front-right, tail back-left) with two wings that
 * sweep up and down, plus tucked legs. Faces RIGHT (+x). The near wing is drawn
 * lighter, the far wing darker, so the overlapping wings stay readable. Flyers
 * float, so every frame is "airborne" and none is planted to a ground line.
 */
import {
  Limb2,
  MannequinColors,
  MannequinOpts,
  SpriteRig,
  capsule,
  DEFAULT_COLORS,
  deg,
  dot,
} from '@/app/utils/rigCore'

export interface FlyerPose {
  /** Body vertical offset, fraction of cell, + = up. */
  bodyY: number
  /** Body pitch, deg, + = nose down (diving), - = nose up. */
  bodyTilt: number
  /** Near wing: shoulder elevation (deg above horizontal-back) + elbow flex. */
  wingNear: Limb2
  /** Far wing (behind the body). */
  wingFar: Limb2
  /** Tail angle, deg below horizontal-back. */
  tail: number
  headTilt: number
}

const fp = (
  bodyY: number,
  bodyTilt: number,
  wing: [number, number],
  tail: number,
  headTilt = 0,
  wingFarDelta = 8
): FlyerPose => ({
  bodyY,
  bodyTilt,
  wingNear: { base: wing[0], flex: wing[1] },
  wingFar: { base: wing[0] - wingFarDelta, flex: wing[1] },
  tail,
  headTilt,
})

// wing.base = degrees of the upper-wing above the horizontal-back direction
// (90 = straight up, 0 = straight out to the side/back, negative = drooped down).

// Idle / hover: gentle flap in place, small bob.
const IDLE: FlyerPose[] = [
  fp(0.0, -4, [40, 30], 14),
  fp(0.01, -4, [55, 24], 12),
  fp(0.015, -4, [62, 20], 10),
  fp(0.01, -4, [48, 28], 12),
  fp(-0.005, -4, [28, 40], 16),
  fp(-0.01, -4, [14, 52], 18),
  fp(-0.005, -4, [26, 44], 16),
  fp(0.0, -4, [38, 34], 14),
]

// Flap / fly: full powered flap. Wings sweep from high+extended (upstroke) to
// low+swept (downstroke); the body LIFTS on the powerstroke and the wings FOLD
// (high flex) on the recovery upstroke so the membrane area visibly changes.
const FLAP: FlyerPose[] = [
  fp(0.04, 6, [86, 8], 10), // top of upstroke — wings high & fully spread
  fp(-0.01, 7, [52, 16], 4), // committing into the downstroke
  fp(-0.04, 9, [16, 28], -4), // mid downstroke — wings sweeping down
  fp(-0.02, 10, [-34, 44], -10), // BOTTOM powerstroke — wings low & swept, body driven up
  fp(0.05, 8, [-12, 56], -2), // catch — wings begin folding up
  fp(0.07, 6, [26, 44], 6), // recovery upstroke — wings folded (high flex)
  fp(0.06, 6, [58, 22], 9), // unfolding, rising
  fp(0.05, 6, [82, 10], 10), // back to top → loops to frame 1
]

// Glide: wings held extended and steady; only subtle tip flutter + tail sway.
const GLIDE: FlyerPose[] = [
  fp(0.0, -2, [10, 8], 10),
  fp(0.006, -2, [12, 7], 9),
  fp(0.01, -3, [13, 6], 8),
  fp(0.006, -3, [11, 7], 9),
  fp(0.0, -2, [9, 8], 10),
  fp(-0.006, -2, [8, 9], 11),
  fp(-0.01, -1, [7, 10], 12),
  fp(0.0, -2, [10, 8], 10),
]

// Dive: wings sweep back/tuck, body pitches nose-down and plunges, then flares.
const DIVE: FlyerPose[] = [
  fp(0.08, -6, [70, 14], 8), // pull up
  fp(0.05, 8, [30, 24], 0), // tip over
  fp(0.0, 28, [-6, 40], -10), // nose down
  fp(-0.08, 46, [-20, 62], -18), // steep plunge, wings tucked back
  fp(-0.18, 54, [-26, 70], -22), // fastest, fully swept
  fp(-0.24, 40, [-10, 56], -12), // begin pull-out
  fp(-0.22, 18, [20, 34], 2), // flare wings
  fp(-0.18, 0, [55, 18], 10), // level out
]

// Hurt: jolt back, wings splay, then settle.
const HURT: FlyerPose[] = [
  fp(0.0, -4, [40, 30], 14),
  fp(0.03, -22, [85, 6], 28, -18), // jolt up/back, wings flung wide
  fp(0.02, -28, [92, 4], 32, -24), // peak recoil
  fp(0.0, -18, [70, 14], 24, -14),
  fp(-0.02, -10, [50, 24], 18, -6),
  fp(-0.01, -6, [38, 32], 14),
  fp(0.0, -4, [40, 30], 14),
  fp(0.0, -4, [40, 30], 14),
]

// Death: wings collapse, body tumbles and falls toward the ground.
const DEATH: FlyerPose[] = [
  fp(0.02, -6, [60, 18], 12, -8), // hit
  fp(-0.04, 18, [20, 40], 4, 14), // wings fold, tip forward
  fp(-0.14, 60, [-20, 80], -8, 40), // tumbling, wings collapsing
  fp(-0.26, 110, [-40, 110], -16, 70), // upside-down fall
  fp(-0.36, 150, [-50, 130], -20, 95), // plummeting
  fp(-0.43, 175, [-55, 140], -22, 110), // near ground
  fp(-0.46, 182, [-58, 145], -24, 116), // crumpled
  fp(-0.47, 184, [-58, 146], -24, 118), // motionless on the ground
]

const ANIMS: Record<string, FlyerPose[]> = {
  idle: IDLE,
  flap: FLAP,
  glide: GLIDE,
  dive: DIVE,
  hurt: HURT,
  death: DEATH,
}

function drawMannequin(
  ctx: CanvasRenderingContext2D,
  frame: FlyerPose,
  opts: MannequinOpts
) {
  const { cellX, cellY, subject, cellSize } = opts
  const colors: MannequinColors = opts.colors ?? DEFAULT_COLORS

  const cx = cellX + subject.centerX
  // Flyers float around the vertical middle of the cell.
  const cy = cellY + cellSize * 0.46 - frame.bodyY * cellSize

  const bodyLen = cellSize * 0.34
  const bodyW = cellSize * 0.16
  const wingUpper = cellSize * 0.3
  const wingLower = cellSize * 0.28
  const wingW = cellSize * 0.05
  const ol = cellSize * 0.011

  const bt = deg(frame.bodyTilt)
  // Body axis: head end forward-right, tail end back-left, pitched by bodyTilt.
  const head = { x: cx + (bodyLen / 2) * Math.cos(bt), y: cy + (bodyLen / 2) * Math.sin(bt) }
  const rear = { x: cx - (bodyLen / 2) * Math.cos(bt), y: cy - (bodyLen / 2) * Math.sin(bt) }
  // Shoulder (wing root) sits near the front third of the back.
  const shoulder = { x: cx + bodyLen * 0.12 * Math.cos(bt), y: cy + bodyLen * 0.12 * Math.sin(bt) }

  // A wing drawn as a real FLIGHT SURFACE, not two sticks: the leading edge runs
  // shoulder → elbow (arm) → tip (primaries), and a filled MEMBRANE closes from
  // the tip back to the body rear so the guide unmistakably reads as a wing.
  // `base` is elevation above horizontal-back; up-and-back means -x and -y.
  const drawWing = (limb: Limb2, color: string, membraneColor: string) => {
    const aUp = deg(limb.base)
    const elbow = {
      x: shoulder.x - wingUpper * Math.cos(aUp),
      y: shoulder.y - wingUpper * Math.sin(aUp),
    }
    const tip = {
      x: elbow.x - wingLower * Math.cos(aUp - deg(limb.flex)),
      y: elbow.y - wingLower * Math.sin(aUp - deg(limb.flex)),
    }
    // Trailing edge anchor: the membrane's inner-rear corner sits a little
    // behind the wing root, toward the tail, so the surface fans out.
    const trail = {
      x: shoulder.x - bodyLen * 0.34 * Math.cos(bt),
      y: shoulder.y - bodyLen * 0.34 * Math.sin(bt),
    }
    // Filled membrane: shoulder → elbow → tip → trailing-rear → back.
    ctx.beginPath()
    ctx.moveTo(shoulder.x, shoulder.y)
    ctx.lineTo(elbow.x, elbow.y)
    ctx.lineTo(tip.x, tip.y)
    ctx.lineTo(trail.x, trail.y)
    ctx.closePath()
    ctx.fillStyle = membraneColor
    ctx.strokeStyle = colors.outline
    ctx.lineJoin = 'round'
    ctx.lineWidth = ol * 1.4
    ctx.fill()
    ctx.stroke()
    // Leading-edge "bones" on top so the wing arm + finger read clearly.
    capsule(ctx, shoulder.x, shoulder.y, elbow.x, elbow.y, wingW, color, colors.outline, ol)
    capsule(ctx, elbow.x, elbow.y, tip.x, tip.y, wingW * 0.7, color, colors.outline, ol)
    dot(ctx, elbow.x, elbow.y, wingW * 0.5, colors.joint)
    dot(ctx, tip.x, tip.y, wingW * 0.5, color, colors.outline, ol * 0.7)
  }

  // FAR wing first (dark membrane, behind the body).
  drawWing(frame.wingFar, colors.torso, colors.far)

  // Tail off the rear.
  const ta = bt + Math.PI + deg(frame.tail)
  const tail = { x: rear.x + cellSize * 0.22 * Math.cos(ta), y: rear.y + cellSize * 0.22 * Math.sin(ta) }
  capsule(ctx, rear.x, rear.y, tail.x, tail.y, wingW * 1.1, colors.far, colors.outline, ol)

  // Body.
  capsule(ctx, rear.x, rear.y, head.x, head.y, bodyW, colors.torso, colors.outline, ol)
  dot(ctx, cx, cy, bodyW * 0.55, colors.torso)

  // Head + beak at the front, with a small facing nub.
  const headR = cellSize * 0.085
  const headPos = { x: head.x + headR * 0.3 * Math.cos(bt), y: head.y + headR * 0.3 * Math.sin(bt) }
  dot(ctx, headPos.x, headPos.y, headR, colors.near, colors.outline, ol)
  const ba = bt + deg(frame.headTilt)
  dot(ctx, headPos.x + headR * Math.cos(ba), headPos.y + headR * Math.sin(ba), headR * 0.45, colors.near, colors.outline, ol * 0.7)
  dot(ctx, headPos.x + headR * 0.25, headPos.y - headR * 0.2, headR * 0.22, colors.joint)

  // NEAR wing last (light membrane, in front).
  drawWing(frame.wingNear, colors.torso, colors.near)
}

export const flyerRig: SpriteRig<FlyerPose> = {
  getFrames: (anim) => ANIMS[anim] ?? IDLE,
  drawMannequin,
}
