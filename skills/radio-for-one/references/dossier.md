# Dossier format

One markdown file per listener, owned by them. Two halves:

- **Profile** — *claims*: what you believe about their taste, distilled to current
  form. This is what the curator reads.
- **Evidence** — *what happened*: favorites, every served queue with its whys and
  verdicts, raw imports. Append-only.

## Claims

Every claim carries its weight and its evidence:

```
- [{must|strong|confirmed|tentative}] {claim} — {low|med|high} — "{verbatim quote}" — {untested|survived-probe|user-confirmed|user-corrected}
```

**Confidence** (low/med/high) is how sure you are the claim is true. High
confidence requires a surviving disconfirmation probe or a read-back confirmation.
Keep quotes in the listener's original language and spelling.

**Weight** is how hard the claim binds when it conflicts with something else:

| Weight      | Meaning                                                      | Who can set it |
| ----------- | ------------------------------------------------------------ | -------------- |
| `must`      | Never broken, not even by a request.                         | Only the listener, stated as absolute ("never", a veto, "I don't like X at all"). |
| `strong`    | Holds unless today's request explicitly overrides it.        | The listener's emphasis, or repeated verdicts pointing one way. |
| `confirmed` | The default for a supported claim; yields to the above.      | Evidence. |
| `tentative` | A tiebreaker only; legal to test on purpose.                 | Anything low-confidence, or a minor preference. |

The two are independent: "likes strong openers" can be certain yet `tentative`,
and a `strong` claim can be young. A low-confidence claim is at most `tentative`.
Grade the claims that steer selection: Modes, Queue rules, Exploration lanes,
Vetoes, Cultural position.

## Updating

- **Evidence sections**: append, dated. Never edit a logged verdict.
- **Profile sections**: keep each claim in its current, distilled form. When a claim
  changes, rewrite it and add one dated Session log line with the verbatim
  correction, so the history survives without the profile turning into a changelog.
- **Lexicon entries and read-back corrections**: write them the moment they happen.
- **Rewrite a whole dossier** only when the listener asks; keep the old version
  (git, or a dated copy).

## Template

```markdown
# Taste dossier — {name}
updated: {date} · sessions: {n} · language: {UA/EN/...} · coverage: {domains touched}

## Portrait
{one paragraph, plain language — the curator's primer}

## Lexicon
{the listener's vibe vocabulary — the curator reads this first on every request}
- "{term, verbatim}" = {what it means for this listener: acoustic / structural / mood} — {conf} — "{quote}"

## Affect carriers (ranked)
1. {carrier} — {conf} — "{quote}" — {status}
composition-first: {yes | no | untested}

## Modes
- [{weight}] **{name}** — function · tolerances (vocals, language, energy) · novelty dial · queue rules

## Queue rules
- [{weight}] {listener-specific queue construction: discovery floor %, spread, pacing, two-tier vocabulary} — {conf} — "{quote}"

## Exploration profile
shape: {nearby | barbell} · chills profile: {deep-miner | explorer | low-chills}
register / complexity ceiling: {...}
live lanes:
- [{weight}] {lane} — {conf} — "{quote}"
weak lanes:
- [{weight}] {lane} — {conf} — "{quote}"

## Vetoes & filters
- [{weight}] {rule} — {acoustic | identity | burnout | register | artist} — {conf} — "{quote}"

## Cultural position
framing_style: {distinction | autonomous | scene-navigator | pure-sound}
artist-relationship: {parasocial | autonomous} · goodwill rules: {...}

## Core / satellites / frontier / archive
center: {formative scene} ({age window}) · home: {parents' music}
core: {...}
satellites: {zone — entry mechanism}
frontier: {zone — pull mechanism}
archive: {demoted eras} · nostalgia: {abandoned-but-missed}

## Token tracks
{context-bound, identity-central tracks — recognition material, never similarity seeds}

## Semantic weight
{high | low} · per-language slots: {...}

## Aspirations
{directions the listener asked to be pulled — consent-gated}

## Rating scale
{the listener's anchors, e.g. 0.1 skip / 0.5 meh / 0.9 add to playlist}

## Open questions
{next interview agenda, highest value first}

## Session log
- {date}: {branch} — {what was learned; verbatim corrections}

---

# Evidence

## Favorites
- **{Artist — Title}** — {why it's a favorite, with quote}

## Queue log
### Q{n} — {type} · {mode} · {date}
Request: "{verbatim}"
| # | Track | Why | Tag | Pred | Score | Verdict (verbatim) |
|---|---|---|---|---|---|---|

## Raw listening data
### {date} — {source}
{imports verbatim, with source and method}
```

**Tag** holds the slot's job and hypothesis (`special`, `filler`, `deep cut`,
`discovery · exemplar-near: <band>`, `discovery · typical`). **Pred** is your
prediction on the listener's rating scale, written before they listen.
