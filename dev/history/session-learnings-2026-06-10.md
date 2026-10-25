# General agent learnings — 2026-06-10 (DM live session)

User-agnostic lessons extracted from the first real interview + first curator
queue. **Folded into `agents/*.md` on 2026-06-10 with explicit founder
authorization, bypassing the eval-before-merge rule** (curator was an empty stub;
interviewer received additive probes only). Debt: L1 interviewer evals and L2
curator golden-dossier evals must backfill before the *next* agent revision —
the bypass was a one-time founder call, not a precedent.
DM-specific facts stay in `dossiers/dm.md`; nothing here is about one user.

## Curator (for the `agents/curator.md` draft)

1. **Queues are two-tier.** "Special attention" slots (2–3 per queue) vs "queue
   filler". Distinctiveness requirements apply to attention slots; filler must
   only hold mood and violate no veto. Serving a filler-grade track in the
   highlight/gift slot reads as a miss even when the taste match is correct
   (observed twice).
2. **Pace on two axes.** Emotional intensity (heavy peaks need calm valleys) and
   attention (benders need filler between them). Also avoid *style saturation* —
   three dark-folk-adjacent tracks in one queue degraded the third regardless of
   quality.
3. **The vibe request constrains the peaks, not the playlist.** Open with an
   unmistakably on-request track (proof of listening), then widen. Users judge
   "did the DJ hear me" by the opener and the peaks, not the average track.
4. **Why-lines are the trust mechanism.** An explained deviation reads as craft;
   an unexplained one reads as ignoring the request. Annotate breathers as
   breathers.
5. **Exploration placement may be bimodal (barbell).** For idiom-saturated
   listeners, "new band that sounds like bands you like" (the collaborative-
   filtering middle) is the dead zone. Live lanes: reinterpretations of proven
   material (covers, acoustic/instrumental/orchestral versions — MusicBrainz
   work-level "cover of"/"arrangement of" relations make this queryable) and
   far-field out-of-category picks. Validate per user; size by the novelty dial.
6. **Popularity is not a default ranking signal** in either direction; treat it
   as a per-user empirical question.
7. **Per-track feedback is gold; collect it verbatim.** Including what the user's
   *autoplay* served next and whether it beat the rec — free probe data that
   found a whole zone (dark-acoustic) the interview missed.

## Interviewer (for the next `agents/taste-interviewer.md` revision)

1. **Ask the novelty dial per mode in session 1.** Its absence forced the first
   queue to guess and overfit; it was the costliest gap.
2. **Probe reinterpretation affinity as a standard question** (instrumental /
   acoustic / piano / orchestral / cross-idiom cover versions). It cleanly
   separates composition-driven taste from production/timbre-driven taste —
   high diagnostic value per question.
3. **Ask about idiom saturation directly** ("inside your home genre, does new
   material still surprise you?") plus years-in-genre. Explains the exploration
   profile and predicts the dead zone.
4. **Elicit queue-level preferences, not only track-level** (session length,
   mixing tolerance, combo-breaker appetite). Queue architecture preferences
   proved as articulable as track preferences.
5. **"Filler vs special attention" is natural user vocabulary** — adopt the
   two-tier frame in read-backs.
6. **The recommendation loop is a probe instrument.** Both major dossier
   corrections of the day ("emotionally pale", the barbell) came from served
   tracks, not from questions. Treat every queue as a batch of falsifiable
   hypotheses with named targets, and log which hypothesis each track tests.

8. **Far-field exploration must preserve the user's register.** "Out of category"
   is not a license for high-art material: a user whose far-field hits are
   2-minute viral pop-rap wants strangeness that stays *song-form, playful,
   visceral*. Avant-garde austerity and classical-adjacent reinterpretations are
   a different axis (register), and "respect but don't like" is the typical
   verdict when it's crossed. Elicit a complexity/register ceiling before
   spending exploration slots (queue 2: all 3 art-register picks missed, both
   song-form picks hit).

## Interviewer (addendum)

7. **Probe the complexity ceiling and the classical relationship explicitly** —
   "experimental" in user vocabulary often means playful genre collision, not
   art music. Asking for examples of "weird music you love" disambiguates
   cheaply; queue misses disambiguate expensively.

## Session 2 addendum (same day — NOT folded into agents; eval debt gates that)

9. **A gift rec that re-derives a known peak is validation, not waste.** The
   user already knowing (and following) the recommended artist confirms the
   formula against ground truth — score it as a model win, log "already a fan"
   as the verdict, and don't apologize for non-novelty.
10. **Users volunteer natural experiments — take them.** Asked "is X also
   [formula]?", the user is handing you a falsification test designed in their
   own vocabulary. Analyze the candidate honestly against the hypothesis
   (including "this case LACKS ingredient Y, so it cleanly tests Y's
   necessity") and ask for the verdict. Both major confirmations of session 2
   came this way.
11. **Offering a precise vocabulary for a felt quality is itself a probe.**
   Defining "conviction" in audible terms ("the performance costs the
   performer something") got an enthusiastic confirm + a biographical anchor
   the question list would never have reached. When the user says "you said it
   better than my word" — record both words and prefer theirs in read-backs.

## 2026-06-11 addendum (NOT folded into agents; eval debt gates that)

12. **First-listen verdicts on complex material are provisional.** User-stated:
   complex compositions "open up gradually on 2,3,5 listen". The verdict loop
   needs a re-serve mechanism: a complex track scored "ok/respect" keeps
   re-listen rights and may be re-queued after a gap; only repeated neutral
   verdicts close it. Quick-skip verdicts on *simple* material stay final.

## Process

- Dossier hygiene: track verdicts and raw listening data live in a companion
  `dossiers/{user}-favorites.md`; the dossier holds claims only.
- Mid-session claim chains (claim → REFINED → REFINED) should be distilled into
  final form at session close; git history preserves the intermediate states.
