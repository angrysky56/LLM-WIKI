/**
 * blob.ts — amorphous-creature rig (slimes, oozes, elementals, ghosts).
 *
 * No skeleton at all: motion is pure SQUASH & STRETCH of a rounded body that
 * rests on the ground. `squash` widens/flattens the body (height compensates
 * so volume reads constant); `reach` stretches it forward (+x) for a lunge;
 * `skewX` leans it for direction. Eyes sit toward the upper RIGHT for facing.
 */
import {
  MannequinColors,
  MannequinOpts,
  SpriteRig,
  DEFAULT_COLORS,
  dot,
} from '@/app/utils/rigCore'

export interface BlobPose {
  /** Vertical offset of the body, fraction of cell, + = up (airborne). */
  bodyY: number
  /** Width multiplier; >1 = wide/flat, <1 = tall/narrow. Height ~ 1/squash. */
  squash: number
  /** Horizontal lean as a fraction of radius, + = leaning right. */
  skewX: number
  /** Forward (+x) stretch as a fraction of radius (lunge). */
  reach: number
  /** Eye tilt, deg. */
  eyeTilt: number
}

const bp = (
  bodyY: number,
  squash: number,
  skewX = 0,
  reach = 0,
  eyeTilt = 0
): BlobPose => ({ bodyY, squash, skewX, reach, eyeTilt })

// Idle / pulse: a slow breathing squash that loops.
const IDLE: BlobPose[] = [
  bp(0.0, 1.0),
  bp(0.0, 1.02),
  bp(0.0, 1.05),
  bp(0.0, 1.03),
  bp(0.0, 1.0),
  bp(0.0, 0.98),
  bp(0.0, 0.97),
  bp(0.0, 1.0),
]

// Hop: anticipate (squash) → launch (stretch up) → floaty apex → land (squash).
// Squash & stretch peak at the contacts; the apex is near-neutral and floaty.
const HOP: BlobPose[] = [
  bp(0.0, 1.0), // rest
  bp(0.0, 1.32, 0.03, 0, -4), // deep anticipation squash
  bp(0.06, 0.74, 0.05, 0, 8), // explosive launch — tall & narrow
  bp(0.17, 0.9, 0, 0, 5), // rising
  bp(0.2, 0.97, 0, 0, 0), // apex — near-neutral, floaty hang
  bp(0.1, 0.86, 0, 0, -3), // descending, stretched toward ground
  bp(0.0, 1.34, -0.03, 0, -6), // landing impact squash
  bp(0.0, 1.04), // settle → loops to frame 1
]

// Bounce: higher, snappier hop with stronger squash & stretch and a big apex.
const BOUNCE: BlobPose[] = [
  bp(0.0, 1.0), // rest
  bp(0.0, 1.52, 0.05, 0, -7), // deep crouch anticipation
  bp(0.08, 0.6, 0.08, 0, 12), // explosive launch — very tall & narrow
  bp(0.27, 0.82, 0, 0, 7), // rising fast
  bp(0.35, 0.93, 0, 0, 0), // high apex
  bp(0.14, 0.74, 0, 0, -5), // fast stretched descent
  bp(0.0, 1.56, -0.05, 0, -9), // hard landing squash
  bp(0.0, 1.1), // rebound settle → loop
]

// Lunge: pull back & compress, stretch forward (+x) hard, then snap back. The
// reach drives a directional teardrop silhouette. One-shot.
const LUNGE: BlobPose[] = [
  bp(0.0, 1.0), // neutral
  bp(0.0, 1.24, -0.12, 0, 4), // load, lean back and compress
  bp(0.0, 1.34, -0.18, 0, 6), // peak wind-up — coiled back
  bp(0.0, 0.92, 0.12, 0.6, -4), // burst — stretch forward
  bp(0.0, 0.78, 0.2, 1.2, -10), // FULL lunge forward, body flung out (+x)
  bp(0.0, 0.88, 0.13, 0.7, -6), // overshoot easing back
  bp(0.0, 1.14, -0.03, 0.1, 2), // recoil squash on return
  bp(0.0, 1.0), // settle
]

// Hurt: sharp squash + jitter, then settle.
const HURT: BlobPose[] = [
  bp(0.0, 1.0),
  bp(0.0, 1.45, -0.16, 0, -14), // slammed flat & back
  bp(0.02, 0.8, 0.1, 0, 12), // rebound wobble
  bp(0.0, 1.28, -0.08, 0, -8),
  bp(0.0, 0.92, 0.05),
  bp(0.0, 1.08, -0.02),
  bp(0.0, 1.0),
  bp(0.0, 1.0),
]

// Death: collapse — flatten and spread into a motionless puddle.
const DEATH: BlobPose[] = [
  bp(0.0, 1.0, 0, 0, -6),
  bp(0.02, 0.88, 0, 0, -10), // shudder up
  bp(0.0, 1.35, 0, 0.2), // begin to sag/spread
  bp(0.0, 1.7, 0, 0.4), // spreading
  bp(0.0, 2.05, 0, 0.6), // flattening
  bp(0.0, 2.35, 0, 0.8), // wide puddle
  bp(0.0, 2.55, 0, 0.95),
  bp(0.0, 2.65, 0, 1.0), // flat, motionless
]

const ANIMS: Record<string, BlobPose[]> = {
  idle: IDLE,
  hop: HOP,
  bounce: BOUNCE,
  lunge: LUNGE,
  hurt: HURT,
  death: DEATH,
}

function drawMannequin(
  ctx: CanvasRenderingContext2D,
  frame: BlobPose,
  opts: MannequinOpts
) {
  const { cellX, cellY, subject, cellSize } = opts
  const colors: MannequinColors = opts.colors ?? DEFAULT_COLORS

  const r0 = cellSize * 0.28
  const rx = r0 * frame.squash * (1 + frame.reach * 0.5)
  const ry = (r0 / frame.squash) * (1 - frame.reach * 0.18)
  const baseline = cellY + subject.baseline
  // Center: rest on the baseline, lift by bodyY, lean by skew + reach forward.
  const cx = cellX + subject.centerX + frame.skewX * r0 + frame.reach * r0 * 0.6
  const cy = baseline - ry - frame.bodyY * cellSize

  const ol = cellSize * 0.012

  // Body: a rounded blob with a slightly flattened bottom that hugs the floor.
  const drawBlob = (fill: string, scale: number) => {
    ctx.beginPath()
    const steps = 40
    for (let i = 0; i <= steps; i++) {
      const a = (i / steps) * Math.PI * 2
      // Flatten the bottom (a near +90deg) so it sits on the ground.
      const flat = a > 0 && a < Math.PI ? 0.86 : 1.0
      // Slight forward bulge (toward +x) for a directional silhouette.
      const bulge = 1 + 0.06 * Math.cos(a)
      const x = cx + Math.cos(a) * rx * scale * bulge
      const y = cy + Math.sin(a) * ry * scale * flat
      if (i === 0) ctx.moveTo(x, y)
      else ctx.lineTo(x, y)
    }
    ctx.closePath()
    ctx.fillStyle = fill
    ctx.fill()
  }

  // Outline pass then body fill.
  ctx.lineJoin = 'round'
  drawBlob(colors.outline, 1 + ol / r0)
  drawBlob(colors.torso, 1)

  // Top-left highlight (the lit near surface) for volume.
  dot(ctx, cx - rx * 0.35, cy - ry * 0.4, Math.min(rx, ry) * 0.32, colors.near)

  // Eyes toward the upper RIGHT for facing.
  const eyeR = Math.min(rx, ry) * 0.2
  const ex = cx + rx * 0.42
  const ey = cy - ry * 0.28 + Math.sin((frame.eyeTilt * Math.PI) / 180) * eyeR
  dot(ctx, ex, ey, eyeR, colors.near, colors.outline, ol * 0.6)
  dot(ctx, ex + eyeR * 0.2, ey, eyeR * 0.5, colors.joint)
  dot(ctx, ex - rx * 0.3, ey, eyeR * 0.85, colors.near, colors.outline, ol * 0.6)
  dot(ctx, ex - rx * 0.3 + eyeR * 0.1, ey, eyeR * 0.42, colors.joint)
}

export const blobRig: SpriteRig<BlobPose> = {
  getFrames: (anim) => ANIMS[anim] ?? IDLE,
  drawMannequin,
}
