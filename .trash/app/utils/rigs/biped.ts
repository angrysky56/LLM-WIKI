/**
 * biped.ts — the bipedal humanoid pose rig (the original Sprite-mode rig).
 *
 * A small humanoid skeleton (torso, neck, head, 2 arms, 2 legs) driven by
 * hand-tuned gait curves. For each frame we render a clean grey "mannequin"
 * in the exact pose that frame should hold; the image model only has to skin
 * it. This is a from-scratch analogue of ControlNet/OpenPose conditioning.
 */
import {
  Limb2,
  MannequinColors,
  MannequinOpts,
  SpriteRig,
  capsule,
  DEFAULT_COLORS,
  dot,
  projDown,
  projUp,
} from '@/app/utils/rigCore'

export interface FramePose {
  /** Torso lean from vertical, deg, + = forward. */
  lean: number
  /** Hip vertical offset as a fraction of figure height, + = up. */
  bodyY: number
  /** Near leg (drawn on top, lighter). */
  legA: Limb2
  /** Far leg (drawn behind, darker). */
  legB: Limb2
  /** Near arm. */
  armA: Limb2
  /** Far arm. */
  armB: Limb2
  /** Optional head tilt, deg, + = forward/down. */
  headTilt?: number
}

// --- Figure proportions, as fractions of total figure height H -------------
const P = {
  thigh: 0.245,
  shin: 0.245,
  torso: 0.3,
  neck: 0.05,
  headR: 0.075,
  upperArm: 0.16,
  foreArm: 0.15,
  hipSepX: 0.03,
  shoulderSepX: 0.03,
} as const

const LEG_LEN = P.thigh + P.shin // 0.49 H

const WALK_LEG: Array<[number, number]> = [
  [25, 5],
  [10, 18],
  [-8, 12],
  [-22, 6],
  [-20, 40],
  [-2, 55],
  [18, 35],
  [27, 12],
]

const RUN_LEG: Array<[number, number]> = [
  [28, 30],
  [5, 18],
  [-26, 35],
  [-34, 95],
  [-8, 110],
  [26, 88],
  [40, 52],
  [33, 36],
]

function armFromLeg(legHip: number, swingScale: number, elbowBase: number): Limb2 {
  const base = -swingScale * legHip
  return { base, flex: elbowBase + 0.25 * Math.abs(base) }
}

function buildLocomotion(
  legCurve: Array<[number, number]>,
  opts: {
    lean: number
    bobAmp: number
    bobPhase?: number
    armSwing: number
    elbowBase: number
  }
): FramePose[] {
  const { lean, bobAmp, bobPhase = 0, armSwing, elbowBase } = opts
  const frames: FramePose[] = []
  for (let i = 0; i < 8; i++) {
    const a = legCurve[i]
    const b = legCurve[(i + 4) % 8]
    const theta = (i / 8) * Math.PI * 2
    const bodyY = bobAmp * Math.cos(2 * theta + bobPhase)
    frames.push({
      lean,
      bodyY,
      legA: { base: a[0], flex: a[1] },
      legB: { base: b[0], flex: b[1] },
      armA: armFromLeg(a[0], armSwing, elbowBase),
      armB: armFromLeg(b[0], armSwing, elbowBase),
    })
  }
  return frames
}

function pose(
  lean: number,
  bodyY: number,
  legHip: number,
  legKnee: number,
  armShoulder: number,
  armElbow: number,
  overrides: Partial<FramePose> = {}
): FramePose {
  return {
    lean,
    bodyY,
    legA: { base: legHip, flex: legKnee },
    legB: { base: legHip, flex: legKnee },
    armA: { base: armShoulder, flex: armElbow },
    armB: { base: armShoulder, flex: armElbow },
    ...overrides,
  }
}

const WALK = buildLocomotion(WALK_LEG, {
  lean: 6,
  bobAmp: 0.018,
  armSwing: 0.7,
  elbowBase: 18,
})

const RUN = buildLocomotion(RUN_LEG, {
  lean: 20,
  bobAmp: 0.05,
  armSwing: 0.55,
  elbowBase: 75,
})

const IDLE: FramePose[] = [
  pose(3, 0.0, 4, 11, -4, 15, { headTilt: 0 }),
  pose(3, 0.004, 4, 10, -5, 15, { headTilt: -1 }),
  pose(4, 0.009, 4, 9, -6, 16, { headTilt: -2 }),
  pose(4, 0.013, 4, 8, -7, 16, { headTilt: -2 }),
  pose(4, 0.009, 4, 9, -6, 16, { headTilt: -1 }),
  pose(3, 0.004, 4, 10, -5, 15, { headTilt: 0 }),
  pose(2, -0.005, 4, 13, -3, 14, { headTilt: 2 }),
  pose(3, 0.0, 4, 11, -4, 15, { headTilt: 0 }),
]

const JUMP: FramePose[] = [
  pose(2, 0.0, 2, 8, 2, 14),
  pose(14, -0.09, 18, 62, -42, 30),
  pose(6, 0.02, 6, 26, 70, 22),
  pose(-4, 0.15, -8, 48, 120, 18),
  pose(-6, 0.23, -4, 82, 140, 16, { headTilt: -4 }),
  pose(2, 0.12, 2, 44, 90, 22),
  pose(12, -0.07, 14, 66, -20, 28),
  pose(4, 0.0, 4, 16, 6, 16),
]

const ATTACK: FramePose[] = [
  { lean: 6, bodyY: 0, legA: { base: 14, flex: 14 }, legB: { base: -16, flex: 18 }, armA: { base: 30, flex: 60 }, armB: { base: -10, flex: 30 } },
  { lean: -2, bodyY: 0.005, legA: { base: 8, flex: 16 }, legB: { base: -20, flex: 22 }, armA: { base: -50, flex: 80 }, armB: { base: -20, flex: 25 } },
  { lean: -8, bodyY: 0.01, legA: { base: 4, flex: 18 }, legB: { base: -26, flex: 28 }, armA: { base: -95, flex: 95 }, armB: { base: -28, flex: 20 } },
  { lean: 10, bodyY: 0.0, legA: { base: 20, flex: 16 }, legB: { base: -18, flex: 24 }, armA: { base: 10, flex: 50 }, armB: { base: 0, flex: 28 } },
  { lean: 22, bodyY: -0.01, legA: { base: 32, flex: 18 }, legB: { base: -24, flex: 12 }, armA: { base: 70, flex: 12 }, armB: { base: 20, flex: 30 } },
  { lean: 16, bodyY: 0.0, legA: { base: 28, flex: 18 }, legB: { base: -22, flex: 16 }, armA: { base: 95, flex: 18 }, armB: { base: 18, flex: 30 } },
  { lean: 8, bodyY: 0.0, legA: { base: 18, flex: 16 }, legB: { base: -18, flex: 20 }, armA: { base: 55, flex: 45 }, armB: { base: 0, flex: 28 } },
  { lean: 6, bodyY: 0, legA: { base: 14, flex: 14 }, legB: { base: -16, flex: 18 }, armA: { base: 30, flex: 60 }, armB: { base: -10, flex: 30 } },
]

const HURT: FramePose[] = [
  pose(4, 0, 4, 10, 4, 16),
  pose(-22, -0.02, -10, 30, -50, 35, { headTilt: -18 }),
  pose(-30, -0.03, -16, 42, -70, 45, { headTilt: -24 }),
  pose(-18, -0.02, -8, 30, -40, 35, { headTilt: -14 }),
  pose(-8, -0.01, 0, 20, -20, 25, { headTilt: -6 }),
  pose(-2, 0, 4, 14, -6, 18),
  pose(2, 0, 4, 12, 2, 16),
  pose(4, 0, 4, 10, 4, 16),
]

const DEATH: FramePose[] = [
  pose(-6, 0.0, 4, 12, -10, 30, { headTilt: -10 }),
  pose(18, -0.05, 16, 45, 10, 35, { headTilt: 12 }),
  pose(40, -0.16, 30, 75, 35, 50, { headTilt: 28 }),
  pose(62, -0.26, 55, 100, 60, 60, { headTilt: 45 }),
  pose(78, -0.34, 80, 120, 80, 70, { headTilt: 60 }),
  pose(88, -0.4, 95, 130, 95, 80, { headTilt: 72 }),
  pose(94, -0.44, 100, 135, 100, 85, { headTilt: 80 }),
  pose(96, -0.45, 100, 138, 102, 88, { headTilt: 84 }),
]

const ANIMS: Record<string, FramePose[]> = {
  idle: IDLE,
  walk: WALK,
  run: RUN,
  jump: JUMP,
  attack: ATTACK,
  hurt: HURT,
  death: DEATH,
}

function drawMannequin(
  ctx: CanvasRenderingContext2D,
  frame: FramePose,
  opts: MannequinOpts
) {
  const { cellX, cellY, subject } = opts
  const colors: MannequinColors = opts.colors ?? DEFAULT_COLORS
  const H = subject.height

  const legW = H * 0.085
  const armW = H * 0.055
  const torsoW = H * 0.15
  const headR = H * P.headR

  const baseHipY =
    cellY + subject.baseline - LEG_LEN * H * 0.96 - frame.bodyY * H
  const hipX = cellX + subject.centerX
  const hipNearX = hipX + P.hipSepX * H * 0.5
  const hipFarX = hipX - P.hipSepX * H * 0.5

  const shoulder = projUp(hipX, baseHipY, P.torso * H, frame.lean)
  const headBase = projUp(
    shoulder.x,
    shoulder.y,
    (P.neck + P.headR) * H,
    frame.lean + (frame.headTilt ?? 0)
  )
  const shNearX = shoulder.x + P.shoulderSepX * H * 0.5
  const shFarX = shoulder.x - P.shoulderSepX * H * 0.5

  const ol = H * 0.012

  const drawLeg = (hx: number, limb: Limb2, w: number, color: string) => {
    const knee = projDown(hx, baseHipY, P.thigh * H, limb.base)
    const foot = projDown(knee.x, knee.y, P.shin * H, limb.base - limb.flex)
    capsule(ctx, hx, baseHipY, knee.x, knee.y, w, color, colors.outline, ol)
    capsule(ctx, knee.x, knee.y, foot.x, foot.y, w, color, colors.outline, ol)
    dot(ctx, knee.x, knee.y, w * 0.45, colors.joint)
  }

  const drawArm = (sx: number, sy: number, limb: Limb2, w: number, color: string) => {
    const elbow = projDown(sx, sy, P.upperArm * H, limb.base)
    const hand = projDown(elbow.x, elbow.y, P.foreArm * H, limb.base + limb.flex)
    capsule(ctx, sx, sy, elbow.x, elbow.y, w, color, colors.outline, ol)
    capsule(ctx, elbow.x, elbow.y, hand.x, hand.y, w, color, colors.outline, ol)
    dot(ctx, elbow.x, elbow.y, w * 0.45, colors.joint)
  }

  drawArm(shFarX, shoulder.y, frame.armB, armW, colors.far)
  drawLeg(hipFarX, frame.legB, legW, colors.far)

  capsule(ctx, hipX, baseHipY, shoulder.x, shoulder.y, torsoW, colors.torso, colors.outline, ol)
  dot(ctx, hipX, baseHipY, torsoW * 0.5, colors.torso)

  drawLeg(hipNearX, frame.legA, legW, colors.near)

  dot(ctx, headBase.x, headBase.y, headR, colors.torso, colors.outline, ol)
  dot(ctx, headBase.x + headR * 0.85, headBase.y, headR * 0.28, colors.near)

  drawArm(shNearX, shoulder.y, frame.armA, armW, colors.near)
}

export const bipedRig: SpriteRig<FramePose> = {
  getFrames: (anim) => ANIMS[anim] ?? IDLE,
  drawMannequin,
}
