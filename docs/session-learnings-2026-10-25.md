# General agent learnings — 2026-10-25 (DM curator session 5, queue 9)

User-agnostic lessons. Curator rules 8/8c folded under live founder
authorization (see `agents/curator.md` header); the rest NOT folded — eval debt
gates agent revisions. DM-specific facts live in `dossiers/dm.md`.

## Curator (numbering continues from the 2026-06-13 file)

13. **Log a prediction per track before serving, on the user's own scale.** The
    first calibrated run (queue 9) got the hit COUNT right (≈5/10) and the
    RANKING at chance (Brier 0.244 vs 0.250 coin flip). A dossier that explains
    past verdicts can still fail to predict new ones; only the prediction log
    shows which. Predict the quantity the user rates — not P(hit) against a
    threshold chosen afterwards.
14. **Similarity isn't the failure mode; typicality is.** Distance to the genre
    centroid predicts "all the same"; nearness to a distinctive exemplar predicts
    "reminds me of X, cool." Tag every discovery slot (rule 8c).
15. **Don't apply a dossier prior against its own recorded exception.** Queue 9
    under-predicted a stage-persona act by running the poser prior, though the
    dossier explicitly carves stage persona out of fakeness. Read the carve-outs
    before the rule.
16. **Pre-check familiarity; don't infer it from absence.** A track scored as a
    discovery probe was by a composer the user is a fan of — absent from notes,
    not absent from life. A 30-second artist-list check before the queue costs
    less than a void probe.
17. **Surface genre labels mislead adjacency.** "Dark electronic" ≠ the user's
    synthwave affinity; the carried feature was melodic, riff-driven writing.
    Match on the carrier, not the shelf.

## Interviewer

18. **Get the rating scale's anchors from the user.** DM: 0.1 immediate skip /
    0.5 meh / 0.9 add to playlist *or* good old memory. Pair the score with a
    new-to-me flag so discovery value is derivable without a second judgment.
19. **Rap scope (pattern, likely general for 2000s-metal listeners):** rap
    *delivery inside rock/metal* is era identity; rap as the *carrying genre* is
    the separate, low-affinity case. Scope genre vetoes to the carrier, not the
    vocal technique.
