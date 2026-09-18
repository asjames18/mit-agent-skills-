# Review Tiers

Choose one working tier, state it in the brief, and do not pad to look more thorough than the evidence.

## Quick Scan

Use for orientation, low switching cost, a clearly bounded question, or an explicit request for a scan.

Cover:

- What the product is and who officially offers it
- The stated problem and whether public materials suggest a fit
- The strongest confirmed capability and the strongest confirmed limitation
- Pricing or limits only when a current official source is in hand
- Top risks, unknowns, and one recommendation

Hard cap: 1,200 words, including the required ending. Prefer fewer words when the evidence is thin.

A Quick Scan may recommend `TEST`, `DEFER`, or `REJECT`. Recommend `ADOPT` only when official sources confirm the needed capability, residual risk is small and named, and the user did not describe production, sensitive-data, or high-cost stakes.

## Standard Review

Default tier for choosing a tool, vendor, or implementation option for a real workflow.

Cover every evaluation dimension. Cite sources for material claims. Include a comparison table when the user named alternatives or a current tool. Record check dates. Do not add sections that lack evidence.

No word target. Stop when the dimensions, evidence labels, and required ending are complete.

## Deep Assessment

Use when the decision would affect production systems, sensitive data, significant spend, architectural lock-in, or when a shallower tier found material conflict or missing official evidence.

In addition to the Standard Review bar, include:

- Implementation path and operational effort
- Security and privacy surface area grounded in official documentation
- Alternatives matrix with the same dimensions for each option
- What a time-boxed test would need to prove or disprove
- What remains unknown even after the deeper pass

## Escalate-if-insufficient

If the current or requested tier cannot support a responsible recommendation, do not guess.

Escalate when any of the following is true:

- Official documentation cannot confirm a capability the problem requires
- Independent or authoritative sources contradict official claims on a material point
- The user describes production use, sensitive data, material cost, or lock-in during a Quick Scan
- Pricing, limits, data handling, or access terms are gated and those facts would change the recommendation

When no depth override was given, continue at the next sufficient tier and label the tier actually used.

When the user locked the tier, do not exceed it. Return `DEFER` or `REJECT`, name the insufficiency, and state the smallest additional input or authorized deeper tier that could change the recommendation.
