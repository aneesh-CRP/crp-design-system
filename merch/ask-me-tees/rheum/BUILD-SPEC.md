# Ask Me Tees — Rheumatology set (approved direction 2026-10-01)

Three concepts (Sjögren's gets two copy variants, so 4 shirts), each in two finishes: **soft** (navy #072061 medium-thin outlines, one flat light-blue #a2dceb fill, white elsewhere, no hatching) and **full color** (kawaii, thick dark outlines, soft shading).
Same character design language as the liver set: simple closed-line happy eyes, tiny eyebrows, blush cheeks, thick clean outlines. Sash labels on characters. No sparkles/stars. All text on the front. CTA + long CRP logo at the bottom.
Page size 3600×3720. Layout = liver pages: art at left 400 / top 880 / 2800×2100, bubble(s) above, punchline at top 3000 (170–190px), CTA at 3245 (110px), logo at 1128/3390 1344×280.

## 1. Joints — "Stiff competition" (covers RA M25-056 + PsA CDDY391A12201)
Art: two knee-joint characters (reuse `assets/characters/psoriatic-arthritis.png` as style ref: bone knee with red swollen joint, sneakers) racing on a track. Left one sprinting ahead, grinning; right one stiff, squeak lines, grimacing. Sashes: "RA" on one, "PsA" on the other (or "ARTHRITIS" on both if two labels feel busy). Finish line ribbon.
Copy: punchline **STIFF COMPETITION.** CTA **FIND A CLINICAL TRIAL TODAY.**
Alt copy: JOINT EFFORT. (two joints high-fiving)

## 2. Lupus — "The great imitator" (Janssen SLE3001)
Art: reuse `assets/characters/lupus.png` style (purple blob, blanket, coffee). Blob wearing a fake-nose-glasses-mustache disguise, sash "LUPUS", holding coffee. Optional: a tiny lineup of other "diseases" it's imitating is too much — keep it to the one blob.
Copy: punchline **THE GREAT IMITATOR.** small explainer **LUPUS LOOKS LIKE EVERYTHING ELSE.** CTA.
Alt copy: RUNNING ON COFFEE AND SUNSCREEN.

## 3. Sjögren's — "It's pronounced SHOW-grins" (Vor RC18G007)
Art: cute cactus character in a small pot, big grin, sash "SJÖGREN'S", holding eye drops in one arm and a water bottle in the other. Tiny teardrop trying to fall and failing.
Copy (Leticia 10/1, build BOTH as separate pages): 
  3a. bubble **IT'S PRONOUNCED SHOW-GRINS.** explainer **DRY EYES. DRY MOUTH. TIRED ALL THE TIME.** CTA.
  3b. punchline **DRY EYES. DRIER HUMOR.** explainer **SJÖGREN'S: DRY EYES, DRY MOUTH, TIRED.** CTA. Art for 3b: same cactus, deadpan half-smile instead of big grin, one tiny teardrop failing to fall, eye drops in hand.

## Generation prompts (Canva generate-image, reference = existing character)
Soft: "Draw in a soft two-color illustration style: medium-thin deep navy (#072061) outlines, NO hatching, one flat light-blue (#a2dceb) fill, white everywhere else, plain white background, kawaii faces (simple closed-line happy eyes, tiny eyebrows, blush). Scene: …  Leave empty space above heads for speech bubbles. No text except sashes."
Color: "Draw in full-color kawaii style matching the reference (thick dark outlines, soft shading, same eyes/eyebrows/blush), white background. Scene: … No text except sashes."
Then remove-background → new pages in a new Canva design "Ask Me Tees - Rheum shirts" (import blank 6-page HTML like characters/canva-import.html), text via add_text + format_text, bubbles via insert_shape.
