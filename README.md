# microburbs-task1
Microburbs Hackathon Task 1: evidence, social creative and team delivery tracking

we'll use a instagram account today

jthk and jthk's Grok Bot are in.

# Are run clubs the new Love Island? (Team Sake, Task 1)

> **Repo status: PRIVATE.** `API_DATA.json` is already in git history. This is not a public
> clean repository. Visibility change and history rewrite are not authorised.

> **Hand-in status: files PRESENT, approval PENDING.** Repo-root `demo.mp4` and `pitch.mp4`
> are the reconstructed producer originals (v11). ffprobe metadata matches the handoff.
> That is not visual/audio QA and not Peter's final content approval. Publication and
> submission are still not approved. Older producer-branch pitch files were stale and
> were not copied.

> **Score status: PROVISIONAL.** The Surry Hills lifestyle score from the supplied API (94)
> does not match Microburbs' public Sydney ranking page (91.0). The independent cross-check
> failed and the discrepancy is unresolved. See [Score discrepancy](#score-discrepancy).

## What we built

A short vertical social video (`demo.mp4`, **PRESENT** at repo root) that uses the
run-club-as-dating-scene trend as a hook to teach one thing about a Sydney neighbourhood:
what Microburbs' *lifestyle* score measures, which is access to cafes, restaurants, bars,
parks and recreation.

The v11 reel in this repo has original music, Jono narration, a map in place of a wrongly
generated cathedral image, and a fictional AI dating contrast (friendzone vs mutual
flirting). It describes the metric and its "very high" band in Surry Hills, and **omits the
exact score** (no disputed 94). Final user approval of that content is still **PENDING**.

The finished deliverable is that produced video. It is **not** a web app, an automated
pipeline, or a working content engine. No live app is required.

## Who it helps

People new to Sydney, or thinking about moving, who scroll past dry suburb profiles but will
watch a short reel about dating culture. They come away knowing what one neighbourhood
metric means and where to look it up. The video is general public education. It gives no
personal dating advice.

## Data

| Source | What we used | Notes |
|---|---|---|
| Microburbs hackathon API, `/v1/suburbs/{suburb_name}/lifestyle/livability` (Surry Hills) | scores list item with `key` `lifestyle`: 94, level "Very high" | Private supplied export, inspected 7 Nov 2026. No source vintage date in the sample; 7 Nov 2026 is our inspection date. Raw response is **not** included in these docs. |
| Microburbs hackathon API, `/v1/suburbs/{suburb_name}/lifestyle/livability-map` | Definition of the `lifestyle` dimension | "Access to the things people go out for — cafes, restaurants, bars, parks and recreation." Rescaled 0–100 score. |
| Microburbs public page, https://www.microburbs.com.au/People-Lifestyle/Top-suburbs-for-Lifestyle-Score/Sydney | Independent cross-check | Lists Surry Hills at 91.0. Fetched 7 Nov 2026. No version or vintage detail on the page sufficient to compare. |
| She Runs, https://www.sheruns.com.au/sheruns | Setting for the hook | Publisher describes a Wednesday 6:30am, 6 km social run that starts at St Mary's Cathedral (CBD) and finishes at the A.P. Bakery rooftop in Surry Hills. Publisher-described schedule, not observed. |

### Claim ledger

| Claim | Value | Source | Status | What it is not |
|---|---|---|---|---|
| Surry Hills lifestyle score | API: 94, "Very high". Public page: 91.0 | API `/lifestyle/livability` scores item `key=lifestyle`; public page URL above; definition from `/lifestyle/livability-map` | **PROVISIONAL, unresolved.** Failed independent cross-check. Recommend omitting the exact score from final videos. | Not a percentage, not a venue count, not a dating or relationship-quality score, not a Census count, not attendee ages or singles rates |

Neither value is treated as the correct or current one. Everything else in the reel is framing.

### Score discrepancy

- The supplied API export says 94. The public Sydney ranking page says 91.0.
- Same suburb and broadly the same metric name, but neither source gives enough vintage or
  version detail to say which is newer, or whether they are computed the same way.
- This is a **failed independent cross-check**, not a passed validation.
- Recommendation: omit the exact score from `demo.mp4` and `pitch.mp4` until organiser
  clarification. We do not substitute 91.0 for 94; it is not known to be current or correct either.

## The clever step

We join a cultural hook to an exact metric definition. Instead of quoting a number alone, we
looked up what Microburbs says `lifestyle` measures, so the line "great for going out" is the
metric's own definition, not our interpretation. Checking the value against a second
Microburbs source exposed a mismatch before it went into a public video.

Future vision (not built): the same hook → primary source → metric definition → editorial
review → reel format could repeat across topics and cities. Today it is one hand-made video.

## Excluded on purpose

- **Age share of young adults.** Age arrays in the sample were truncated, so we could not verify it.
- **Cafe and park counts.** Totals conflicted across endpoints.
- **Rent figures.** These belonged to a rejected rent story.
- **"Single" residents.** "Not married" does not mean "single".
- **Club demographics.** Neighbourhood characteristics are not attendee demographics. We have no
  data on attendee age, sexuality or relationship status.
- **Dating odds and outcomes.** Club participation and dating outcomes were never measured. No
  statement in the video or these docs, with or without a number, claims dating odds or causal effects.
- **No assertion that Microburbs changes romance outcomes.**

## How it was made

Production tools reported by the creator for this v11 cut: Remotion (layout and motion),
ElevenLabs narration (a voice clone of team member Jono; the voice ID is deliberately not
published), original music, Higgsfield AI-generated b-roll, ffmpeg for encoding. Root files
were reconstructed from lossless ZIP transport parts in scratch; those parts were not
committed. Older producer-branch pitch files were stale and were not copied.

### AI scenes

- All b-roll is **AI illustration**, not documentary footage of She Runs or any real club.
- Comedic scenes are labelled **withoutMicroburbs** (friendzone) and **withMicroburbsAPI**
  (mutual flirting). These are a **fictional AI dramatisation** played for laughs. They are
  **not a promised outcome** of using Microburbs, and not evidence of what happens at any
  real run club.
- The v11 reel uses a **map** rather than a wrongly generated cathedral image. The She Runs
  start is still the publisher's St Mary's Cathedral location; the map is illustration, not a
  surveyed route.

Rights, organiser clearance, and final user content approval are **PENDING**. We do not
claim every licence is cleared, and we do not claim visual/audio QA from ffprobe.

## Assets status

| File | Requirement | Status |
|---|---|---|
| `demo.mp4` | Finished social post, 15–45 s, 1080x1920 vertical, under 95,000,000 bytes | **PRESENT** at repo root. ffprobe: 39.900 s, 1080x1920, H.264/AAC. Metadata only, not approval. |
| `pitch.mp4` | Pitch, 45 s or shorter, under 95,000,000 bytes | **PRESENT** at repo root. ffprobe: 45 s, 1080x1920, H.264/AAC. Metadata only, not approval. |

A longer 3-minute walkthrough was requested separately. It is extra and does not replace `demo.mp4`.

Official references: [hackathon guide](https://www.microburbs.com.au/p/hackathon-guide),
[Task 1 social post](https://www.microburbs.com.au/p/hackathon-task-social-post).
No claims CSV is required for this task.

## How to run

No app to run. Open the report and verify the hand-in:

```sh
python3 -m http.server 8000      # then open http://localhost:8000/report.html
python3 scripts/verify.py                   # strict metadata check (not visual/audio QA)
python3 scripts/verify.py --allow-pending   # same docs checks; missing media would be PENDING
```

You can also open `report.html` straight from disk. It loads no remote scripts, fonts or assets.

## Limits

- The lifestyle score is PROVISIONAL: the API value and the public page value disagree, and the
  cause is unresolved.
- No independent audience or engagement validation yet. No view counts.
- No measurement of dating outcomes, and no causal evidence.
- Not a predictive model; the held-out check is a manual cross-endpoint definition check plus a
  value cross-check that failed (see `report.html`).
- Source code in this repo is documentation and a docs verifier. Producer Remotion/media work
  lives on a separate branch and is not the submitted engine.
