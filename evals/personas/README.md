# L1 — Interviewer eval personas (TODO, M0)

Each persona = one file with two sections:
1. **Ground-truth dossier** (hidden from the interviewer) — filled per the schema
   in agents/taste-interviewer.md: carriers, framing_style, vetoes, modes.
2. **Roleplay instructions** — how this listener talks: vocabulary, language (UA/EN),
   verbosity, evasions.

Required coverage (per docs/prd.md §9): 5–8 personas including
- one terse / low-effort persona
- one eager-to-please persona (agrees with every synthesis)
- at least one UA-language persona
- distinct affect carriers and framing_styles across the set

Runner (to build): interviewer vs persona, unattended, 1 session → extracted
dossier → field assertions + LLM-as-judge vs ground truth → report.
