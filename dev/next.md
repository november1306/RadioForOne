# What's next — as of 2026-10-26

State: the skill package, claim grading (must / strong / confirmed / tentative) and
the MIT license are merged to `master` (PR #5). DM's dossier is distilled and
graded; 16 queues logged. Not published — that waits for the founder's word.

## 1. M0 dogfood (the current gate)

1. Package with `bash dev/package-skill.sh` and hand it privately to the two
   friends (no public release).
2. Each friend runs Onboarding end to end: interview → dossier → first queue
   (house rule: DakhaBrakha — "Specially for You" opens it). Save their dossiers to
   `dossiers/<name>.md`.
3. A few days of queues each, with reactions logged.
4. **Gate:** blind-match the three dossiers to their humans (`prd.md` §11). Until
   it passes: no Telegram, hosting, resolver or embeddings.

Watch during dogfood: does onboarding stay within 6–10 questions, does the
dossier format hold for a non-metal listener, and does the founder-specific
material in `references/` leak into their queues.

## 2. DM loose ends

- Per-track scores pending for Q14, Q15, Q16 (Q16 was a whole-queue hit).
- Re-listen rights open: San Salvador, 1914, Orbit Culture, Shining.
- Open question 1: spend 1–2 slots per queue deliberately breaking a rule,
  tagged, to test which rules over-filter (open question 2).

## 3. Eval debt

The skill changed without suites. These suites would have covered the changes:
- Claim grading + conflict resolution by weight → **L2** (golden dossiers with
  conflicting claims; does the curator pick the heavier one?).
- Interviewer formative-path move → **L1** (see `evals/personas/README.md`).
Build L1/L2 minimal versions before the next round of skill edits, not before
the dogfood.

## 4. After the gate

Click-to-listen radio link inside the skill (prototype:
`dev/tools/make_listen_link.py`; it takes `Artist|Title` lines, then shorten the
link). Then the M1 items in `prd.md` §11.
