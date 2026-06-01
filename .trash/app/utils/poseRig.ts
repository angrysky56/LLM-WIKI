/**
 * poseRig.ts — deterministic 2D pose engine for sprite animation (dispatch).
 *
 * WHY THIS EXISTS
 * ----------------
 * Asking an image model to *invent* an animation across 8 panels is the single
 * least reliable thing you can ask a diffusion model to do: it has no notion of
 * biomechanics or temporal continuity. The fix is to stop asking the model to
 * invent motion — we author it here, in code, as a rig that renders a clean
 * grey "mannequin" in the exact pose each frame must hold. That rendered figure
 * becomes a POSE MAP the model only has to *skin*. It's a from-scratch,
 * dependency-free analogue of ControlNet/OpenPose conditioning.
 *
 * BODY PLANS
 * ----------
 * A bipedal skeleton can't drive a quadruped, a snake, a bird, or a blob, so
 * the rig is selected per BODY PLAN. Each plan's anatomy + motion lives in its
 * own module under utils/rigs/; this file just dispatches to the right one and
 * renders the full pose-map sheet. Shared primitives live in utils/rigCore.ts.
 */
import {
  BodyPlanId,
  DEFAULT_COLORS,
  MannequinColors,
  SpriteRig,
  SubjectBounds,
} from '@/app/utils/rigCore'
import { bipedRig } from '@/app/utils/rigs/biped'
import { blobRig } from '@/app/utils/rigs/blob'
import { flyerRig } from '@/app/utils/rigs/flyer'
import { quadrupedRig } from '@/app/utils/rigs/quadruped'
import { serpentRig } from '@/app/utils/rigs/serpent'

// Re-export shared types/helpers so existing importers keep working.
export type { SubjectBounds, MannequinColors, BodyPlanId } from '@/app/utils/rigCore'
export { measureSubjectBounds, DEFAULT_COLORS } from '@/app/utils/rigCore'

export const RIGS: Record<BodyPlanId, SpriteRig> = {
  biped: bipedRig as SpriteRig,
  quadruped: quadrupedRig as SpriteRig,
  serpent: serpentRig as SpriteRig,
  flyer: flyerRig as SpriteRig,
  blob: blobRig as SpriteRig,
}

export interface PoseGuideOptions {
  anim: string
  /** Which body plan's rig to render (defaults to biped). */
  bodyPlan?: BodyPlanId
  cols: number
  rows: number
  cellSize: number
  frameCount: number
  subject: SubjectBounds
  colors?: MannequinColors
}

/**
 * Render the full pose-map sheet: a `cols`×`rows` grid where each cell shows
 * the selected body plan's mannequin in that frame's pose, on a flat key-color
 * background. This is the image fed to the model as the structural POSE
 * reference.
 */
export function drawPoseGuideSheet(
  ctx: CanvasRenderingContext2D,
  opts: PoseGuideOptions
) {
  const { anim, cols, rows, cellSize, frameCount, subject } = opts
  const colors = opts.colors ?? DEFAULT_COLORS
  const rig = RIGS[opts.bodyPlan ?? 'biped'] ?? RIGS.biped
  const frames = rig.getFrames(anim)

  ctx.fillStyle = colors.key
  ctx.fillRect(0, 0, cols * cellSize, rows * cellSize)

  for (let i = 0; i < frameCount; i++) {
    const c = i % cols
    const r = Math.floor(i / cols)
    const frame = frames[i % frames.length]
    rig.drawMannequin(ctx, frame, {
      cellX: c * cellSize,
      cellY: r * cellSize,
      cellSize,
      subject,
      colors,
    })
  }
}
