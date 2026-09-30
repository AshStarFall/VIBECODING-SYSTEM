# Product and Interface Quality

## Product usefulness

- Name the target user, painful job, existing workaround, and why the proposed outcome is better.
- Validate risky demand assumptions with users or observable behavior; do not present a polished prototype as market evidence.
- Choose a small success measure tied to user value. Define how it is collected without excessive tracking.
- Make the first-use path clear, and make failure, recovery, cancellation, and data export/deletion understandable.
- For a user-facing release, run the scoped [`EXPERIENCE-AUDIT.md`](EXPERIENCE-AUDIT.md) and record findings with evidence, severity, owner, and retest status.

## Design quality

- Start from the real workflow and content. Establish hierarchy, navigation, responsive layout, and states before decoration.
- Use a product-specific type/color system with adequate contrast and readable sizing. Avoid generic layouts that make unrelated products look identical.
- Use motion only to clarify continuity or state; respect reduced-motion settings.
- Use appropriate real assets when they help users inspect the actual product. Avoid misleading placeholders, inaccessible icon-only actions, and unlicensed assets.
- Check keyboard, screen reader semantics, zoom, contrast, touch targets, text overflow, loading, empty, error, and success states.

## Slop check

Before completion ask: Is each screen/action necessary? Is content specific to the user and domain? Are repeated components genuinely shared? Are there fake controls, dead links, placeholder copy, gratuitous gradients/cards/animation, unused code, or overbuilt abstractions? Remove only issues in scope and verify the actual interface.

## Interpretation

“Likability” is one part of desirability and satisfaction, not a substitute for usefulness, task success, accessibility, trust, or reliability. Do not collapse these dimensions into one score or claim that a handful of test sessions represents all users.