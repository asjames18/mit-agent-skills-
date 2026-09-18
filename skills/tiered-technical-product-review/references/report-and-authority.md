# Report and Authority

## Required ending

Every completed brief ends with these headings, in this order, with no others substituted:

### OUTCOME

One short paragraph: the product, the problem, the tier used, and what the evidence can and cannot support.

### EVIDENCE

The material confirmed facts, vendor claims, inferences, and unknowns that drive the recommendation. Cite sources. Do not repeat the full body.

### RECOMMENDATION

Exactly one of:

- `ADOPT` — official sources confirm the needed capability, named risks are acceptable for the stated problem, and a bounded rollout is the next discussion, not an authorized action.
- `TEST` — the product is promising, but a time-boxed evaluation must still prove or disprove a named uncertainty.
- `DEFER` — evidence, timing, access, or readiness is insufficient; name the unknown that would unlock a later review.
- `REJECT` — poor fit, unacceptable documented risk, or a better-supported option for the stated problem.

Do not emit combinations, scores-as-decisions, or a different verb.

### RISKS AND UNKNOWNS

The residual risks that survive the recommendation, plus facts that were not established. Include gated sources and unverified vendor claims that could change the decision.

### NEXT ACTION

The smallest safe next step for the user, such as authorizing a deeper tier, supplying missing context, or reviewing a proposed test plan. The next action is not an instruction for the agent to execute an external change.

## Comparison mode

When the user names alternatives or asks which option to choose:

- Evaluate each option against the same dimensions and evidence labels.
- Prefer a compact matrix plus a short narrative of material differences.
- Do not downgrade an option for missing marketing copy or upgrade one for a stronger landing page.
- Still emit exactly one `RECOMMENDATION` for the decision the user asked about. Rank the other options only as supporting evidence.

## Failure handling

Stop with a structured failure instead of a confident brief when:

| Condition | Return | Required content |
| --- | --- | --- |
| Missing product or problem | `INSUFFICIENT INPUT` | The exact missing inputs. |
| Official sources cannot support a material capability | `INSUFFICIENT EVIDENCE` | What was searched, what remains unknown, and `DEFER` or `REJECT` if a partial brief is still useful. |
| Locked tier cannot support a responsible recommendation | `TIER INSUFFICIENT` | Why, and the smallest deeper tier or input that could help. |
| Material official and independent sources conflict | `SOURCE CONFLICT` | Both accounts, dates, and why the conflict blocks `ADOPT`. |
| Needed facts are login-gated or paid | `ACCESS GATED` | The gated fact, recorded as **Unknown**, with no account creation. |

High-stakes legal, medical, safety, or regulated-use questions require narrowed wording and an explicit note that the brief is not professional advice.

If a completed brief is still possible, keep the required ending. Put the failure label in `OUTCOME` and avoid `ADOPT`.

## Proposed external action

If the user asks to purchase, sign up, connect a tool, send a message, publish, deploy, or change a live system, do not do it. Present only:

```
PROPOSED ACTION:
DESTINATION:
CONTENT OR CHANGE:
RISKS:
```

Wait for an explicit approval of that packet. A prior `ADOPT` or `TEST` recommendation does not fill any of these fields.

## After-delivery stop rules

- Stop after delivering the brief or structured failure.
- Do not implement, configure, message a vendor, open a ticket, create an account, or start a follow-on review on implied authority.
- Do not chain this skill into deployment, procurement, or publishing skills.
- Resume only when the user provides new inputs or explicitly requests another tier or a proposed-action packet.
