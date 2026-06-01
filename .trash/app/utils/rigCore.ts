/**
 * rigCore.ts — shared primitives for every Sprite-mode pose rig.
 *
 * Each body plan (biped, quadruped, serpent, flyer, blob) ships its own rig
 * module under utils/rigs/. They all share the same canvas conventions,
 * colour scheme, drawing helpers, and subject-measurement, which live here so
 * the rigs themselves only have to encode anatomy + motion.
 *
 * CONVENTIONS (identical to the original poseRig):
 * - Canvas space: +x = right, +y = down. Characters face RIGHT (+x).
 * - Limb angles are measured from straight-DOWN, positive = swung FORWARD.
 * - `bodyY` is a vertical offset as a fraction of figure height, + = up.
 */

export type BodyPlanId = 'biped' | 'quadruped' | 'serpent' | 'flyer' | 'blob'

/** Angle of a two-segment limb: proximal base + distal flex (both degrees). */
export interface Limb2 {
  /** Angle of the proximal segment from straight-down, deg, + = forward. */
  base: number
  /** Flex of the distal segment, deg, >= 0. */
  flex: number
}

export interface SubjectBounds {
  /** Height (px) of the character from top to bottom within the cell. */
  height: number
  /** Horizontal center (px) of the character within the cell. */
  centerX: number
  /** Foot / bottom baseline (px, y) of the character within the cell. */
  baseline: number
}

export interface MannequinColors {
  key: string
  torso: string
  /** NEAR-side limbs (closer to camera) — rendered LIGHTER for depth. */
  near: string
  /** FAR-side limbs (behind the body) — rendered DARKER for depth. */
  far: string
  joint: string
  /** Dark separation edge drawn around every limb so parts never merge. */
  outline: string
}

// Strong near/far value split is deliberate: in a side view the two legs (and
// two arms/wings) overlap constantly, and if they share one value they read as
// a single mushy blob. Lighter front + darker back + a dark outline is exactly
// how hand-drawn sprite cycles stay legible, and it tells the image model to
// shade the parts the same way.
export const DEFAULT_COLORS: MannequinColors = {
  key: '#ff00ff',
  torso: '#525a66',
  near: '#9aa2af',
  far: '#2c313a',
  joint: '#1b1e24',
  outline: '#101218',
}

export interface MannequinOpts {
  cellX: number
  cellY: number
  /** Side length (px) of the square cell. Cell-filling rigs (serpent, flyer,
   *  blob) size themselves to this rather than the subject bbox, whose height
   *  is unreliable for non-upright body plans. */
  cellSize: number
  subject: SubjectBounds
  colors?: MannequinColors
}

/** A pose rig for one body plan: a pose table per animation + a renderer. */
export interface SpriteRig<F = unknown> {
  /** Return the per-frame pose table for an animation (with a safe default). */
  getFrames(anim: string): F[]
  /** Draw one posed mannequin into the given cell. */
  drawMannequin(ctx: CanvasRenderingContext2D, frame: F, opts: MannequinOpts): void
}

export const deg = (d: number) => (d * Math.PI) / 180

/** Project a point downward-ish (legs/arms) by `len` at `angleDeg` from down. */
export function projDown(x: number, y: number, len: number, angleDeg: number) {
  const a = deg(angleDeg)
  return { x: x + len * Math.sin(a), y: y + len * Math.cos(a) }
}

/** Project a point upward-ish (torso/head) by `len` at `angleDeg` from up. */
export function projUp(x: number, y: number, len: number, angleDeg: number) {
  const a = deg(angleDeg)
  return { x: x + len * Math.sin(a), y: y - len * Math.cos(a) }
}

/** Project a point rightward-ish (spines/necks/tails) by `len` at `angleDeg`
 *  measured from straight-RIGHT (+x), positive = tilting DOWN. */
export function projRight(x: number, y: number, len: number, angleDeg: number) {
  const a = deg(angleDeg)
  return { x: x + len * Math.cos(a), y: y + len * Math.sin(a) }
}

export function capsule(
  ctx: CanvasRenderingContext2D,
  x1: number,
  y1: number,
  x2: number,
  y2: number,
  width: number,
  color: string,
  outline?: string,
  outlineW = 0
) {
  ctx.lineCap = 'round'
  if (outline && outlineW > 0) {
    ctx.strokeStyle = outline
    ctx.lineWidth = width + outlineW * 2
    ctx.beginPath()
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.stroke()
  }
  ctx.strokeStyle = color
  ctx.lineWidth = width
  ctx.beginPath()
  ctx.moveTo(x1, y1)
  ctx.lineTo(x2, y2)
  ctx.stroke()
}

export function dot(
  ctx: CanvasRenderingContext2D,
  x: number,
  y: number,
  r: number,
  color: string,
  outline?: string,
  outlineW = 0
) {
  if (outline && outlineW > 0) {
    ctx.fillStyle = outline
    ctx.beginPath()
    ctx.arc(x, y, r + outlineW, 0, Math.PI * 2)
    ctx.fill()
  }
  ctx.fillStyle = color
  ctx.beginPath()
  ctx.arc(x, y, r, 0, Math.PI * 2)
  ctx.fill()
}

/** Stroke a smooth poly-line through points as a tapered tube (for spines). */
export function polyTube(
  ctx: CanvasRenderingContext2D,
  pts: Array<{ x: number; y: number }>,
  widthAt: (t: number) => number,
  color: string,
  outline?: string,
  outlineW = 0
) {
  if (pts.length < 2) return
  ctx.lineCap = 'round'
  ctx.lineJoin = 'round'
  const drawPass = (stroke: string, extra: number) => {
    for (let i = 0; i < pts.length - 1; i++) {
      const t = i / (pts.length - 1)
      ctx.strokeStyle = stroke
      ctx.lineWidth = Math.max(1, widthAt(t) + extra)
      ctx.beginPath()
      ctx.moveTo(pts[i].x, pts[i].y)
      ctx.lineTo(pts[i + 1].x, pts[i + 1].y)
      ctx.stroke()
    }
  }
  if (outline && outlineW > 0) drawPass(outline, outlineW * 2)
  drawPass(color, 0)
}

/**
 * Measure the character's bounding box in a chroma-key (magenta) reference by
 * finding all non-key pixels. Returns null when the frame is essentially
 * empty so the caller can fall back to sensible defaults. Body-plan agnostic.
 */
export function measureSubjectBounds(
  data: Uint8ClampedArray,
  w: number,
  h: number
): SubjectBounds | null {
  let minX = w
  let minY = h
  let maxX = -1
  let maxY = -1
  let count = 0
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const i = (y * w + x) * 4
      const r = data[i]
      const g = data[i + 1]
      const b = data[i + 2]
      const alpha = data[i + 3]
      const isKey = alpha < 24 || (r > 180 && g < 95 && b > 180)
      if (isKey) continue
      count++
      if (x < minX) minX = x
      if (x > maxX) maxX = x
      if (y < minY) minY = y
      if (y > maxY) maxY = y
    }
  }
  if (count < (w * h) / 400 || maxY < 0) return null
  return {
    height: maxY - minY + 1,
    centerX: (minX + maxX) / 2,
    baseline: maxY,
  }
}
