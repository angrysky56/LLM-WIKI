/**
 * serpent.ts — limbless undulator rig (snakes, eels, fish).
 *
 * No skeleton: the body is a poly-line SPINE that follows a traveling sine
 * wave. The head is at the RIGHT (+x) end. Animations advance the wave phase
 * (slither/swim), pull the head back and lunge it (strike), tighten the wave
 * into a coil, or flatten it out (death). Sized to the cell, since a wave's
 * vertical bbox is a poor proxy for body length.
 */
import {
  MannequinColors,
  MannequinOpts,
  SpriteRig,
  DEFAULT_COLORS,
  capsule,
  deg,
  dot,
  polyTube,
} from '@/app/utils/rigCore'

export interface SerpentPose {
  /** Wave phase, radians. */
  phase: number
  /** Wave amplitude as a fraction of the cell size. */
  amp: number
  /** Number of full waves along the body. */
  freq: number
  /** Vertical offset of the body midline, fraction of cell, + = up. */
  bodyY: number
  /** Head forward extension as a fraction of body length (+ lunge / - coil). */
  reach: number
  /** Extra head tilt, deg. */
  headTilt: number
  /** Jaw opening, 0 = closed, 1 = gaping bite (drives the strike). */
  mouth: number
}

const sp = (
  phase: number,
  amp: number,
  freq: number,
  bodyY: number,
  reach: number,
  headTilt = 0,
  mouth = 0
): SerpentPose => ({ phase, amp, freq, bodyY, reach, headTilt, mouth })

const TWO_PI = Math.PI * 2

// Idle: a slow, low-amplitude breathing undulation that loops.
const IDLE: SerpentPose[] = Array.from({ length: 8 }, (_, i) =>
  sp((i / 8) * TWO_PI * 0.5, 0.05 + 0.008 * Math.sin((i / 8) * TWO_PI), 1.4, 0, 0)
)

// Slither / swim: a full traveling wave; phase advances one loop over 8 frames.
const SLITHER: SerpentPose[] = Array.from({ length: 8 }, (_, i) =>
  sp((i / 8) * TWO_PI, 0.13, 2, 0, 0)
)

// Strike: coil back and load (head drawn back, body tightens), then lunge the
// head forward FAST with jaws gaping, then retract. Plays once.
const STRIKE: SerpentPose[] = [
  sp(0.0, 0.1, 1.6, 0, 0, 0, 0), // ready
  sp(0.4, 0.18, 2.2, 0, -0.1, -8, 0), // draw head back, coil tightens
  sp(0.85, 0.24, 2.7, 0, -0.2, -14, 0.18), // tight coil, loaded, jaw parts
  sp(0.55, 0.14, 1.8, 0, 0.12, 4, 0.5), // uncoil drives head out, mouth opening
  sp(0.12, 0.06, 1.0, 0, 0.44, -12, 1.0), // FULL LUNGE forward, jaws WIDE
  sp(0.22, 0.08, 1.2, 0, 0.34, -6, 0.7), // overshoot, jaws closing
  sp(0.42, 0.12, 1.6, 0, 0.1, 0, 0.18), // retract
  sp(0.0, 0.11, 1.6, 0, 0, 0, 0), // back to ready coil
]

// Coil: tighten from a loose wave into a compact, high-frequency defensive coil
// with the head raised and ready over the body, then hold.
const COIL: SerpentPose[] = [
  sp(0.0, 0.1, 1.4, 0, 0),
  sp(0.3, 0.14, 1.9, 0, -0.05, -4),
  sp(0.6, 0.17, 2.6, -0.02, -0.12, -8),
  sp(0.9, 0.2, 3.3, -0.03, -0.18, -12),
  sp(1.1, 0.22, 4.0, -0.04, -0.24, -16),
  sp(1.2, 0.23, 4.5, -0.05, -0.28, -18, 0.12),
  sp(1.26, 0.24, 4.8, -0.05, -0.3, -20, 0.12),
  sp(1.26, 0.24, 4.8, -0.05, -0.3, -20, 0.12),
]

// Hurt: a sharp recoil wave that spikes then settles.
const HURT: SerpentPose[] = [
  sp(0.0, 0.1, 1.6, 0, 0),
  sp(1.2, 0.24, 2.6, 0.02, -0.08, -10), // violent jolt
  sp(2.0, 0.28, 3.0, 0.01, -0.1, -14), // peak thrash
  sp(1.4, 0.2, 2.4, 0, -0.04, -8),
  sp(0.8, 0.15, 2.0, 0, 0, -4),
  sp(0.4, 0.12, 1.7, 0, 0),
  sp(0.1, 0.1, 1.6, 0, 0),
  sp(0.0, 0.1, 1.6, 0, 0),
]

// Death: thrash once, then go limp and flatten toward a straight resting line.
const DEATH: SerpentPose[] = [
  sp(0.0, 0.14, 1.8, 0, 0, -6),
  sp(1.4, 0.22, 2.4, 0.01, -0.04, -12), // last thrash
  sp(2.2, 0.16, 2.0, 0, 0, 6),
  sp(2.6, 0.1, 1.6, -0.01, 0, 14), // going limp
  sp(2.8, 0.06, 1.2, -0.02, 0, 22),
  sp(2.9, 0.035, 0.9, -0.02, 0, 30),
  sp(3.0, 0.02, 0.6, -0.03, 0, 36),
  sp(3.0, 0.012, 0.4, -0.03, 0, 40), // flat, motionless
]

const ANIMS: Record<string, SerpentPose[]> = {
  idle: IDLE,
  slither: SLITHER,
  strike: STRIKE,
  coil: COIL,
  hurt: HURT,
  death: DEATH,
}

function drawMannequin(
  ctx: CanvasRenderingContext2D,
  frame: SerpentPose,
  opts: MannequinOpts
) {
  const { cellX, cellY, subject, cellSize } = opts
  const colors: MannequinColors = opts.colors ?? DEFAULT_COLORS

  const L = cellSize * 0.82
  const cx = cellX + subject.centerX
  const baseX = cx - L / 2
  // Body midline sits in the lower half so the lowest belly rests near the
  // baseline (downstream alignment plants it).
  const midY = cellY + subject.baseline - cellSize * 0.24 - frame.bodyY * cellSize
  const amp = frame.amp * cellSize
  const N = 28

  const pts: Array<{ x: number; y: number }> = []
  for (let k = 0; k <= N; k++) {
    const t = k / N
    // Reach pushes the head end (t→1) forward (or pulls it back when coiling).
    const stretch = 1 + frame.reach * (t * t)
    const x = baseX + t * L * stretch
    // Wave dampens toward the head so the snout leads cleanly.
    const env = 0.45 + 0.55 * (1 - t)
    const y = midY + amp * Math.sin(frame.freq * TWO_PI * t + frame.phase) * env
    pts.push({ x, y })
  }

  const bodyW = cellSize * 0.12
  // Taper: thin tail (t=0) → thick mid/head.
  polyTube(ctx, pts, (t) => bodyW * (0.32 + 0.78 * t), colors.torso, colors.outline, cellSize * 0.012)

  // Head: a rounded bulge with an eye + snout nub, at the RIGHT end.
  const head = pts[pts.length - 1]
  const neck = pts[pts.length - 3]
  const hr = cellSize * 0.075
  const dx = head.x - neck.x
  const dy = head.y - neck.y
  const len = Math.hypot(dx, dy) || 1
  const ux = dx / len
  const uy = dy / len
  const fwdAng = Math.atan2(uy, ux)
  const ol = cellSize * 0.012
  const mouth = Math.max(0, Math.min(1, frame.mouth))

  // Tongue flick — a thin forked tongue darting forward, strongest when the
  // jaws are open (reads as an aggressive bite/taste).
  if (mouth > 0.05) {
    const base = { x: head.x + ux * hr * 0.6, y: head.y + uy * hr * 0.6 }
    const tipLen = hr * (1.1 + mouth * 1.2)
    const tip = { x: base.x + ux * tipLen, y: base.y + uy * tipLen }
    const fork = hr * 0.5
    capsule(ctx, base.x, base.y, tip.x, tip.y, cellSize * 0.009, colors.joint)
    capsule(ctx, tip.x, tip.y, tip.x + Math.cos(fwdAng - deg(22)) * fork, tip.y + Math.sin(fwdAng - deg(22)) * fork, cellSize * 0.007, colors.joint)
    capsule(ctx, tip.x, tip.y, tip.x + Math.cos(fwdAng + deg(22)) * fork, tip.y + Math.sin(fwdAng + deg(22)) * fork, cellSize * 0.007, colors.joint)
  }

  // Head bulge.
  dot(ctx, head.x, head.y, hr, colors.near, colors.outline, ol)

  if (mouth > 0.05) {
    // Open jaws: an upper snout angled up and a lower jaw angled down from the
    // forward axis, gaping wider as `mouth` → 1.
    const gap = deg(8 + mouth * 42)
    const jawLen = hr * 1.05
    const upAng = fwdAng - gap
    const loAng = fwdAng + gap
    capsule(ctx, head.x, head.y, head.x + Math.cos(upAng) * jawLen, head.y + Math.sin(upAng) * jawLen, hr * 0.5, colors.near, colors.outline, ol * 0.8)
    capsule(ctx, head.x, head.y, head.x + Math.cos(loAng) * jawLen, head.y + Math.sin(loAng) * jawLen, hr * 0.42, colors.torso, colors.outline, ol * 0.8)
  } else {
    // Closed: a single snout nub forward (toward +x) for facing.
    dot(ctx, head.x + ux * hr * 0.7, head.y + uy * hr * 0.7, hr * 0.42, colors.near, colors.outline, cellSize * 0.008)
  }

  // Eye.
  dot(ctx, head.x + hr * 0.1, head.y - hr * 0.35, hr * 0.22, colors.joint)
}

export const serpentRig: SpriteRig<SerpentPose> = {
  getFrames: (anim) => ANIMS[anim] ?? IDLE,
  drawMannequin,
}
