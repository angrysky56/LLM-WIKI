/**
 * quadruped.ts — four-legged creature pose rig (wolves, horses, big cats…).
 *
 * Anatomy: a horizontal SPINE from hip (rear) to shoulder (front), four legs
 * (front-near/front-far, hind-near/hind-far), a neck + head at the front, and
 * a tail at the rear. Faces RIGHT (+x). Near-side legs are drawn lighter, far
 * side darker, so the two overlapping legs in a pair stay individually
 * readable — exactly the depth cue the image model is told to reproduce.
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
  projDown,
} from '@/app/utils/rigCore'

export interface QuadPose {
  /** Whole-body vertical offset, fraction of figure height, + = up. */
  bodyY: number
  /** Spine tilt, deg, + = front end raised (rearing), - = front lowered. */
  backTilt: number
  frontNear: Limb2
  frontFar: Limb2
  hindNear: Limb2
  hindFar: Limb2
  /** Neck angle from horizontal +x, deg, + = head down, - = head up. */
  neck: number
  /** Extra head tilt of the snout, deg. */
  headTilt: number
  /** Tail angle from horizontal-back, deg, + = down, - = raised. */
  tail: number
}

// Proportions as fractions of figure height H (standing shoulder height).
const P = {
  backLen: 1.0,
  thigh: 0.27,
  shin: 0.27,
  neckLen: 0.38,
  headR: 0.15,
  tailLen: 0.52,
  bodyW: 0.32,
  legW: 0.075,
} as const

const LEG_LEN = P.thigh + P.shin

const qpose = (
  bodyY: number,
  backTilt: number,
  front: [number, number],
  hind: [number, number],
  neck: number,
  headTilt: number,
  tail: number,
  depth = 6
): QuadPose => ({
  bodyY,
  backTilt,
  frontNear: { base: front[0], flex: front[1] },
  frontFar: { base: front[0] - depth, flex: front[1] },
  hindNear: { base: hind[0], flex: hind[1] },
  hindFar: { base: hind[0] - depth, flex: hind[1] },
  neck,
  headTilt,
  tail,
})

// A single walking-leg stride over 8 frames as [hipAngle, kneeFlex] pairs.
const WALK_LEG: Array<[number, number]> = [
  [22, 12],
  [8, 18],
  [-10, 16],
  [-24, 20],
  [-18, 50],
  [-2, 62],
  [14, 42],
  [24, 18],
]

function buildWalk(): QuadPose[] {
  const frames: QuadPose[] = []
  for (let i = 0; i < 8; i++) {
    // 4-beat gait: hind leads, front lags by a quarter cycle; near/far halves
    // offset by half a cycle so the pair is never perfectly overlapped.
    const hN = WALK_LEG[i]
    const hF = WALK_LEG[(i + 4) % 8]
    const fN = WALK_LEG[(i + 2) % 8]
    const fF = WALK_LEG[(i + 6) % 8]
    const theta = (i / 8) * Math.PI * 2
    frames.push({
      // Two small vertical bobs per stride (shoulders dip as forelegs plant).
      bodyY: 0.02 * Math.cos(2 * theta),
      // Spine rocks a hair as weight shifts fore/aft — adds life without noise.
      backTilt: 1.5 * Math.sin(theta),
      hindNear: { base: hN[0], flex: hN[1] },
      hindFar: { base: hF[0], flex: hF[1] },
      frontNear: { base: fN[0], flex: fN[1] },
      frontFar: { base: fF[0], flex: fF[1] },
      // Head bobs with the gait — neck dips forward/down on the forefoot plant.
      neck: -40 + 5 * Math.sin(theta + Math.PI / 2),
      headTilt: 2 * Math.sin(theta),
      tail: 18 + 6 * Math.sin(theta),
    })
  }
  return frames
}

const IDLE: QuadPose[] = [
  qpose(0.0, 0, [6, 12], [-6, 20], -42, 0, 18),
  qpose(0.004, 0, [6, 11], [-6, 19], -43, -1, 16),
  qpose(0.008, 0, [6, 10], [-6, 18], -44, -1, 14),
  qpose(0.01, 0, [6, 10], [-6, 18], -44, 0, 16),
  qpose(0.008, 0, [6, 11], [-6, 19], -43, 0, 18),
  qpose(0.004, 0, [6, 12], [-6, 20], -42, 1, 20),
  qpose(-0.004, 0, [6, 13], [-6, 21], -41, 2, 22),
  qpose(0.0, 0, [6, 12], [-6, 20], -42, 0, 18),
]

const WALK = buildWalk()

// Gallop: two suspensions (extended + collected), front and hind pairs work
// together. Strong bodyY bob with airborne peaks.
const RUN: QuadPose[] = [
  qpose(-0.04, -4, [10, 70], [-20, 64], -34, 6, 28, 8), // gather, tucked under
  qpose(0.02, -8, [-18, 30], [-40, 30], -28, 4, 6, 8), // hind push, front reach
  qpose(0.16, 2, [34, 18], [-46, 22], -36, 0, -18, 6), // extended suspension (air)
  qpose(0.05, 6, [40, 22], [-22, 40], -42, -2, -6, 6), // front reach down
  qpose(-0.05, 4, [26, 16], [4, 26], -40, 2, 12, 8), // front plant, hind swings up
  qpose(0.14, -2, [4, 64], [18, 70], -32, 4, 24, 8), // collected suspension (air)
  qpose(0.02, -6, [-6, 40], [30, 40], -30, 4, 20, 8), // hind reach forward
  qpose(-0.04, -4, [14, 60], [-6, 58], -34, 6, 26, 8), // regather → loop
]

const JUMP: QuadPose[] = [
  qpose(0.0, 0, [6, 12], [-6, 20], -42, 0, 18), // stand
  qpose(-0.08, -6, [16, 60], [-22, 64], -30, 8, 30), // crouch, gather
  qpose(0.04, 8, [-14, 28], [-30, 26], -50, -6, -4), // launch, front up
  qpose(0.2, 6, [10, 36], [-28, 40], -48, -4, -16), // ascend, tuck
  qpose(0.27, 2, [22, 30], [-26, 34], -46, -2, -20), // peak, compact
  qpose(0.12, -2, [30, 24], [-10, 30], -44, 0, -6), // descend, reach down
  qpose(-0.07, 4, [20, 56], [4, 60], -34, 6, 22), // land impact
  qpose(0.0, 0, [6, 14], [-6, 22], -42, 0, 18), // recover
]

const POUNCE: QuadPose[] = [
  qpose(-0.02, -2, [8, 18], [-8, 24], -40, 2, 16), // alert stance
  qpose(-0.12, -10, [20, 72], [-26, 78], -22, 14, 34), // crouch low, coil
  qpose(-0.06, -6, [26, 50], [-34, 48], -30, 8, 20), // load, weight back
  qpose(0.1, 10, [-30, 18], [-40, 22], -52, -8, -10), // explosive launch fwd/up
  qpose(0.22, 8, [-40, 14], [-30, 28], -50, -6, -22), // airborne, front paws reach fwd
  qpose(0.12, 4, [-20, 12], [-10, 34], -44, -2, -16), // descend, paws lead
  qpose(-0.05, -4, [30, 30], [10, 40], -32, 10, 18), // strike down / land
  qpose(-0.02, 0, [10, 18], [-6, 24], -40, 2, 16), // recover crouch
]

const HURT: QuadPose[] = [
  qpose(0.0, 0, [6, 12], [-6, 20], -42, 0, 18), // neutral
  qpose(-0.03, 10, [22, 24], [-22, 26], -20, 18, 8), // jolt: front rears, head up/back
  qpose(-0.05, 14, [28, 28], [-26, 22], -14, 22, 2), // peak recoil
  qpose(-0.03, 8, [18, 26], [-16, 26], -26, 12, 10), // stagger
  qpose(-0.01, 3, [10, 20], [-10, 22], -36, 6, 16), // settling
  qpose(0.0, 0, [6, 14], [-6, 20], -40, 2, 18), // nearly back
  qpose(0.0, 0, [6, 12], [-6, 20], -42, 0, 18), // neutral
  qpose(0.0, 0, [6, 12], [-6, 20], -42, 0, 18), // hold
]

const DEATH: QuadPose[] = [
  qpose(0.0, 0, [6, 12], [-6, 20], -42, -4, 16), // hit, shock
  qpose(-0.06, -6, [18, 40], [-18, 46], -22, 10, 22), // legs buckle
  qpose(-0.16, -10, [30, 78], [-26, 84], -8, 20, 18), // sinking, front collapsing
  qpose(-0.26, -8, [44, 110], [10, 110], 8, 30, 10), // chest hits ground
  qpose(-0.34, -4, [70, 130], [40, 128], 22, 42, 4), // rolling onto side
  qpose(-0.4, 0, [95, 140], [80, 138], 40, 56, -2), // legs splayed out
  qpose(-0.43, 0, [108, 146], [98, 144], 58, 70, -4), // settling flat
  qpose(-0.45, 0, [112, 150], [104, 148], 70, 78, -6), // motionless rest
]

const SLEEP: QuadPose[] = [
  qpose(-0.36, 0, [96, 138], [92, 140], 64, 60, -40), // curled, tail wrapped, breathing
  qpose(-0.355, 0, [96, 137], [92, 139], 63, 60, -40),
  qpose(-0.35, 0, [95, 136], [91, 138], 62, 59, -39), // gentle inhale
  qpose(-0.348, 0, [95, 136], [91, 137], 62, 59, -39),
  qpose(-0.35, 0, [95, 137], [91, 138], 63, 60, -39), // exhale
  qpose(-0.355, 0, [96, 137], [92, 139], 63, 60, -40),
  qpose(-0.36, 0, [96, 138], [92, 140], 64, 61, -40), // settle
  qpose(-0.36, 0, [96, 138], [92, 140], 64, 60, -40),
]

const ANIMS: Record<string, QuadPose[]> = {
  idle: IDLE,
  walk: WALK,
  run: RUN,
  jump: JUMP,
  pounce: POUNCE,
  hurt: HURT,
  death: DEATH,
  sleep: SLEEP,
}

function drawMannequin(
  ctx: CanvasRenderingContext2D,
  frame: QuadPose,
  opts: MannequinOpts
) {
  const { cellX, cellY, subject, cellSize } = opts
  const colors: MannequinColors = opts.colors ?? DEFAULT_COLORS
  // Quadrupeds are long, so the anchor bbox height is a bad direct scale
  // input: a wolf can be short in height but very wide nose-to-tail. Cap the
  // rig by the cell width so the full tail/body/head footprint stays inside a
  // single 512px cell with a magenta gutter. Otherwise the model learns a pose
  // guide that crosses the implicit grid and sliced frames contain parts of
  // neighbouring creatures.
  const H = Math.min(subject.height * 0.82, cellSize * 0.34)

  const legW = H * P.legW
  const bodyW = H * P.bodyW
  const headR = H * P.headR
  const ol = H * 0.012

  // Seat the spine so a near-vertical standing leg reaches the baseline.
  const half = (P.backLen * H) / 2
  const cx = cellX + cellSize / 2
  const baseline = Math.min(subject.baseline, cellSize * 0.9)
  const cy = cellY + baseline - LEG_LEN * H * 0.92 - frame.bodyY * H
  const a = deg(frame.backTilt)
  const shoulder = { x: cx + half * Math.cos(a), y: cy - half * Math.sin(a) }
  const hip = { x: cx - half * Math.cos(a), y: cy + half * Math.sin(a) }

  const depthDX = H * 0.045

  const drawLeg = (px: number, py: number, limb: Limb2, color: string) => {
    const knee = projDown(px, py, P.thigh * H, limb.base)
    const foot = projDown(knee.x, knee.y, P.shin * H, limb.base - limb.flex)
    capsule(ctx, px, py, knee.x, knee.y, legW, color, colors.outline, ol)
    capsule(ctx, knee.x, knee.y, foot.x, foot.y, legW * 0.85, color, colors.outline, ol)
    dot(ctx, knee.x, knee.y, legW * 0.42, colors.joint)
    dot(ctx, foot.x, foot.y, legW * 0.5, color, colors.outline, ol * 0.8)
  }

  // FAR legs first (dark, behind), offset slightly back into the scene.
  drawLeg(hip.x - depthDX, hip.y, frame.hindFar, colors.far)
  drawLeg(shoulder.x - depthDX, shoulder.y, frame.frontFar, colors.far)

  // Tail (off the rear, behind the body).
  const ta = deg(frame.tail)
  const tail1 = { x: hip.x - P.tailLen * H * 0.5 * Math.cos(ta), y: hip.y + P.tailLen * H * 0.5 * Math.sin(ta) }
  const tail2 = { x: tail1.x - P.tailLen * H * 0.5 * Math.cos(ta + 0.25), y: tail1.y + P.tailLen * H * 0.5 * Math.sin(ta + 0.25) }
  capsule(ctx, hip.x, hip.y, tail1.x, tail1.y, legW * 0.8, colors.far, colors.outline, ol)
  capsule(ctx, tail1.x, tail1.y, tail2.x, tail2.y, legW * 0.5, colors.far, colors.outline, ol)

  // Spine / barrel body.
  capsule(ctx, hip.x, hip.y, shoulder.x, shoulder.y, bodyW, colors.torso, colors.outline, ol)
  dot(ctx, hip.x, hip.y, bodyW * 0.5, colors.torso)
  dot(ctx, shoulder.x, shoulder.y, bodyW * 0.52, colors.torso)

  // Neck + head off the front.
  const na = deg(frame.neck)
  const neckEnd = {
    x: shoulder.x + P.neckLen * H * Math.cos(na),
    y: shoulder.y + P.neckLen * H * Math.sin(na),
  }
  capsule(ctx, shoulder.x, shoulder.y, neckEnd.x, neckEnd.y, bodyW * 0.55, colors.torso, colors.outline, ol)
  dot(ctx, neckEnd.x, neckEnd.y, headR, colors.near, colors.outline, ol)
  // Snout nub pointing roughly forward (RIGHT) for facing.
  const sa = deg(frame.neck + 70 + frame.headTilt)
  dot(ctx, neckEnd.x + headR * 0.9 * Math.cos(sa), neckEnd.y + headR * 0.9 * Math.sin(sa), headR * 0.42, colors.near, colors.outline, ol * 0.6)

  // NEAR legs last (light, in front).
  drawLeg(hip.x + depthDX, hip.y, frame.hindNear, colors.near)
  drawLeg(shoulder.x + depthDX, shoulder.y, frame.frontNear, colors.near)
}

export const quadrupedRig: SpriteRig<QuadPose> = {
  getFrames: (anim) => ANIMS[anim] ?? IDLE,
  drawMannequin,
}
