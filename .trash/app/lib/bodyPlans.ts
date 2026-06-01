'use client'

import { SPRITE_CHARACTER_PRESETS, SpriteAnimType, SpritePreset } from '@/app/lib/sprite'

/**
 * bodyPlans.ts — the "body plan" registry for Sprite mode.
 *
 * Sprite mode animates characters by handing the image model a deterministic
 * skeletal POSE MAP it only has to skin (see utils/poseRig). That rig is
 * anatomy-specific: a bipedal humanoid skeleton can't drive a quadruped, a
 * snake, a bird, or a blob. Rather than fork Sprite mode into a second
 * standalone mode (which would duplicate the entire anchor → key → align →
 * export → QA pipeline), we keep ONE Sprite mode and branch only the layers
 * that depend on anatomy: the rig, the per-animation choreography, the anchor
 * pose, and the QA expectations.
 *
 * This file is the single source of truth the CLIENT uses for: which body
 * plans exist, which animations each one supports, the per-plan starter
 * presets, and the per-plan UI copy. The matching anatomy logic lives in:
 *   • utils/poseRig.ts + utils/rigs/*   — the deterministic pose rigs
 *   • api/generate/route.ts             — choreography + anchor + guide text
 *   • api/sprite-review/route.ts        — QA expectations + acceptance rules
 * all keyed by the same `BodyPlan` id string.
 */
export type BodyPlan = 'biped' | 'quadruped' | 'serpent' | 'flyer' | 'blob'

export interface BodyPlanSpec {
  id: BodyPlan
  /** Short label shown on the body-plan chip. */
  label: string
  /** One-line description shown on hover / under the picker. */
  hint: string
  /** Ordered animation set this plan supports (drives the anim chip strip). */
  anims: SpriteAnimType[]
  /** Animation selected when the user first switches to this plan. */
  defaultAnim: SpriteAnimType
  /** Animations with intentional airborne frames — baseline alignment must
   *  preserve their vertical motion instead of planting every frame. */
  airborneAnims: SpriteAnimType[]
  /** Starter creature archetypes for this plan. */
  presets: SpritePreset[]
}

export const BODY_PLAN_ORDER: BodyPlan[] = [
  'biped',
  'quadruped',
  'serpent',
  'flyer',
  'blob',
]

const QUADRUPED_PRESETS: SpritePreset[] = [
  {
    id: 'wolf',
    label: 'Grey wolf',
    prompt:
      'Lean grey wolf on all fours, thick fur, pointed ears, bushy tail, side profile. Agile predator, game creature art.',
  },
  {
    id: 'boar',
    label: 'Wild boar',
    prompt:
      'Stocky wild boar, dark bristly fur, tusks, short legs, snout low. Heavy four-legged enemy, side profile.',
  },
  {
    id: 'panther',
    label: 'Black panther',
    prompt:
      'Sleek black panther, muscular feline body on all fours, long tail, glowing yellow eyes. Stealthy predator, side profile.',
  },
  {
    id: 'warhorse',
    label: 'Warhorse',
    prompt:
      'Armored warhorse, muscular body, flowing mane and tail, barding plate on the chest. Noble four-legged mount, side profile.',
  },
  {
    id: 'hellhound',
    label: 'Hellhound',
    prompt:
      'Demonic hellhound on all fours, charred black hide, glowing ember cracks, smoking maw, spiked spine. Aggressive beast, side profile.',
  },
  {
    id: 'giant-spider',
    label: 'Giant spider',
    prompt:
      'Large quadruped-stance giant spider, bulbous abdomen, sturdy legs planted, cluster of red eyes, fanged maw. Cave enemy, side profile.',
  },
  {
    id: 'dog',
    label: 'Dog',
    prompt:
      'Friendly medium-sized dog on all fours, short brown-and-white fur, floppy ears, wagging tail, tongue out. Cute companion animal, side profile facing right.',
  },
  {
    id: 'cat',
    label: 'Cat',
    prompt:
      'Domestic house cat on all fours, sleek orange tabby fur, pointed ears, long curling tail, whiskers. Agile small feline, side profile facing right.',
  },
  {
    id: 'cow',
    label: 'Cow',
    prompt:
      'Spotted dairy cow on all fours, black-and-white hide, broad body, small horns, swishing tail, udder. Calm farm animal, side profile facing right.',
  },
  {
    id: 'deer',
    label: 'Deer',
    prompt:
      'Slender forest deer on all fours, tan coat, white spots, thin legs, branching antlers, short tail, large ears. Graceful woodland animal, side profile facing right.',
  },
  {
    id: 'brown-bear',
    label: 'Brown bear',
    prompt:
      'Large brown bear on all fours, thick shaggy fur, heavy shoulders, rounded ears, broad snout, stubby tail. Powerful forest beast, side profile facing right.',
  },
  {
    id: 'red-fox',
    label: 'Red fox',
    prompt:
      'Red fox on all fours, orange coat, white belly, pointed black-tipped ears, sharp snout, bushy white-tipped tail. Quick cunning animal, side profile facing right.',
  },
  {
    id: 'pig',
    label: 'Pig',
    prompt:
      'Pink farm pig on all fours, round plump body, short legs, curly tail, snout, floppy ears. Chubby barnyard animal, side profile facing right.',
  },
  {
    id: 'goat',
    label: 'Goat',
    prompt:
      'Mountain goat on all fours, shaggy white coat, curved backswept horns, short beard, thin legs, hooves. Hardy hooved animal, side profile facing right.',
  },
]

const SERPENT_PRESETS: SpritePreset[] = [
  {
    id: 'green-snake',
    label: 'Green serpent',
    prompt:
      'Long green serpent, smooth scales, slender tapering body, small head with flicking tongue. Side profile, head to the right.',
  },
  {
    id: 'sea-eel',
    label: 'Sea eel',
    prompt:
      'Dark blue sea eel, finned ridge along the back, sleek elongated body, sharp small teeth. Side profile, head to the right.',
  },
  {
    id: 'koi-fish',
    label: 'Koi fish',
    prompt:
      'Orange-and-white koi fish, flowing fins and tail, round body, big eye. Side profile facing right, swimming.',
  },
  {
    id: 'desert-viper',
    label: 'Desert viper',
    prompt:
      'Sand-colored desert viper, diamond pattern, broad triangular head, fangs. Coiled muscular body, side profile, head to the right.',
  },
  {
    id: 'frost-wyrm',
    label: 'Frost wyrm',
    prompt:
      'Pale icy frost wyrm, crystalline scales, frill behind the head, long sinuous body glowing faint blue. Side profile, head to the right.',
  },
  {
    id: 'shark',
    label: 'Shark',
    prompt:
      'Grey reef shark, streamlined torpedo body, tall triangular dorsal fin, crescent tail, gills, rows of teeth. Sleek ocean predator, side profile facing right, swimming.',
  },
  {
    id: 'clownfish',
    label: 'Clownfish',
    prompt:
      'Bright orange clownfish, white bands with black edging, rounded body, fan-like fins, big eye. Cheerful reef fish, side profile facing right, swimming.',
  },
  {
    id: 'pufferfish',
    label: 'Pufferfish',
    prompt:
      'Inflated yellow pufferfish, round spiny body, small fins, big round eyes, tiny mouth. Comical spiky fish, side profile facing right, swimming.',
  },
  {
    id: 'anglerfish',
    label: 'Anglerfish',
    prompt:
      'Deep-sea anglerfish, dark bulbous body, huge fanged jaw, glowing lure dangling over the head, tiny eyes. Menacing abyssal fish, side profile facing right.',
  },
  {
    id: 'swordfish',
    label: 'Swordfish',
    prompt:
      'Silver-blue swordfish, long pointed bill, streamlined muscular body, tall sickle dorsal fin, forked tail. Fast ocean fish, side profile facing right, swimming.',
  },
  {
    id: 'dolphin',
    label: 'Dolphin',
    prompt:
      'Grey bottlenose dolphin, smooth streamlined body, curved dorsal fin, flippers, beak-like snout, horizontal tail fluke. Playful marine mammal, side profile facing right, swimming.',
  },
  {
    id: 'sea-serpent',
    label: 'Sea serpent',
    prompt:
      'Mythical teal sea serpent, long sinuous scaled body, finned crest along the spine, horned head, glowing eyes. Aquatic monster, side profile, head to the right.',
  },
  {
    id: 'piranha',
    label: 'Piranha',
    prompt:
      'Red-bellied piranha, compact silver body, jutting lower jaw with sharp teeth, fan fins, big eye. Aggressive river fish, side profile facing right, swimming.',
  },
]

const FLYER_PRESETS: SpritePreset[] = [
  {
    id: 'hawk',
    label: 'Hawk',
    prompt:
      'Brown hawk with broad feathered wings, hooked beak, fanned tail, sharp talons. Side profile facing right, in flight.',
  },
  {
    id: 'bat-swarm',
    label: 'Giant bat',
    prompt:
      'Giant bat, leathery membranous wings, small furry body, big ears, fanged mouth. Side profile facing right, in flight.',
  },
  {
    id: 'fairy',
    label: 'Fairy',
    prompt:
      'Tiny winged fairy, translucent insect wings, glowing aura, slender body. Side profile facing right, hovering.',
  },
  {
    id: 'wyvern',
    label: 'Wyvern',
    prompt:
      'Small wyvern, scaled body, large leathery dragon wings, horned head, barbed tail. Side profile facing right, in flight.',
  },
  {
    id: 'phoenix',
    label: 'Phoenix',
    prompt:
      'Fiery phoenix, feathered wings wreathed in orange flame, long trailing tail feathers, glowing crest. Side profile facing right, in flight.',
  },
]

const BLOB_PRESETS: SpritePreset[] = [
  {
    id: 'green-slime',
    label: 'Green slime',
    prompt:
      'Classic round green slime, translucent jelly body, two big eyes, tiny mouth. Bouncy gelatinous blob, side profile, eyes to the right.',
  },
  {
    id: 'lava-blob',
    label: 'Lava blob',
    prompt:
      'Molten lava blob, glowing orange-red semi-liquid body, dripping edges, ember eyes. Hot gelatinous creature, side profile facing right.',
  },
  {
    id: 'ooze',
    label: 'Purple ooze',
    prompt:
      'Purple acidic ooze, glossy viscous body, bubbling surface, single large eye. Amorphous blob, side profile facing right.',
  },
  {
    id: 'ghost',
    label: 'Wisp ghost',
    prompt:
      'Pale floating ghost wisp, soft rounded body with a wispy trailing tail, hollow eyes. Amorphous spirit, side profile facing right.',
  },
  {
    id: 'water-elemental',
    label: 'Water elemental',
    prompt:
      'Small water elemental, translucent blue blob of swirling water, glowing core, droplet shape. Amorphous creature, side profile facing right.',
  },
]

export const BODY_PLANS: Record<BodyPlan, BodyPlanSpec> = {
  biped: {
    id: 'biped',
    label: 'Humanoid',
    hint: 'Bipedal humanoid — knights, mages, goblins, bosses (2 arms, 2 legs).',
    anims: ['idle', 'walk', 'run', 'jump', 'attack', 'hurt', 'death'],
    defaultAnim: 'idle',
    // Run is a GROUND gait: the model places the rows at inconsistent heights,
    // and a rigid airborne shift would preserve that "top row high / bottom row
    // low" split. Grounding it plants every frame on the shared floor line.
    // Only jump has a true ballistic arc that must keep its lift.
    airborneAnims: ['jump'],
    presets: SPRITE_CHARACTER_PRESETS,
  },
  quadruped: {
    id: 'quadruped',
    label: 'Quadruped',
    hint: 'Four-legged beasts — wolves, horses, big cats, hounds (spine + 4 legs + tail).',
    anims: ['idle', 'walk', 'run', 'jump', 'pounce', 'hurt', 'death', 'sleep'],
    defaultAnim: 'idle',
    // Run/gallop is a GROUND gait: ground every frame to the shared floor line
    // so the whole cycle plants consistently instead of splitting into a high
    // row and a low row. Jump and pounce keep their real ballistic lift.
    airborneAnims: ['jump', 'pounce'],
    presets: QUADRUPED_PRESETS,
  },
  serpent: {
    id: 'serpent',
    label: 'Serpent / Fish',
    hint: 'Limbless undulators — snakes, eels, fish (a sinuous spine wave).',
    anims: ['idle', 'slither', 'strike', 'coil', 'hurt', 'death'],
    defaultAnim: 'idle',
    airborneAnims: [],
    presets: SERPENT_PRESETS,
  },
  flyer: {
    id: 'flyer',
    label: 'Flyer / Bird',
    hint: 'Winged creatures — birds, bats, wyverns (body + 2 wings + tail).',
    anims: ['idle', 'flap', 'glide', 'dive', 'hurt', 'death'],
    defaultAnim: 'flap',
    // Flyers are airborne by nature — every frame floats, so none should be
    // planted to a ground baseline.
    airborneAnims: ['idle', 'flap', 'glide', 'dive', 'hurt', 'death'],
    presets: FLYER_PRESETS,
  },
  blob: {
    id: 'blob',
    label: 'Blob',
    hint: 'Amorphous creatures — slimes, oozes, elementals (squash & stretch, no limbs).',
    anims: ['idle', 'hop', 'bounce', 'lunge', 'hurt', 'death'],
    defaultAnim: 'idle',
    airborneAnims: ['hop', 'bounce'],
    presets: BLOB_PRESETS,
  },
}

/** Whether the given animation should preserve airborne vertical motion (vs.
 *  being planted to the ground baseline) for the given body plan. */
export function isAirborneAnim(plan: BodyPlan, anim: SpriteAnimType): boolean {
  return (BODY_PLANS[plan]?.airborneAnims ?? []).includes(anim)
}
