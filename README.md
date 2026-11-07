# Where to Go for a Running Date

We use Microburbs data to find Sydney neighbourhoods that are better suited to running dates.
Watch our reel from [here🔗](https://www.instagram.com/reel/DfbTA9tvH8t/?utm_source=ig_web_copy_link&cplk=MzRlODBiNWFlZA==&srtk=MzRlODBiNWFlZA==)

[Read the report](report.html) · [Strategy](docs/STRATEGY.md) · [Concept and methods](docs/CONCEPT.md) · [35 candidate hooks](docs/hook-bank.md)

## What we did

- Investigated Microburbs rent, sales, property and demographic data for the API's 29 City of Sydney suburbs. We combined it with the census, Inside Airbnb, council trees, Revenue NSW camera notices and liquor licences.
- Built a bank of 35 hooks and assessed surprise, local identity, Microburbs relevance, data strength, timing, political sensitivity and reuse rights.
- Chose run clubs as the flagship. Census neighbourhood context and Microburbs rent comparisons give the social hook a local reason to exist.
- Matched the strongest ideas to the cultural calendar. Same suburb, different moment: timing turns a fact into a post.

## How we validated

Every number on screen traces back to a source table, with denominators checked and dates and geography labelled. The full claim register is in the report's validation section.

## Timing makes the post

| Moment | Proposed post | Why Microburbs matters |
|---|---|---|
| Sydney Marathon, 30 Aug 2026, retrospective | Run clubs and social connection | Young-singles catchments plus Microburbs rent context. |
| Spring, Sep–Nov 2026, retrospective | "It's not the maples": about 24 plane trees per maple | A fun fact from council tree data; supporting research. |
| Lunar Streets, 6 Feb 2027 | "In Haymarket, more locals were born in Thailand than in Australia." | Microburbs birthplace shares: Thailand 19.2%, Australia 14.2%, China 23.4%. Haymarket unit rent median $1,200/week. |
| USyd Welcome Program, 8–19 Feb 2027 | "About 1 in 4 Darlington locals is 20–24. Its recorded unit rent median rose 63%." | Microburbs age share 27.0%; unit rent median $445 (Feb 2015) to $725 (Oct 2026). |

**Backup:** NYE, 31 Dec 2026 — Barangaroo's unit median is $2,000/week. **Sequel:** Songkran (Thai New Year), 13–15 Apr 2027, brings Thaitown back.

Birthplace and age figures are **census-based, via Microburbs**. Lunar New Year leads because it's a celebration of the suburb itself.

## Deliverables

| File | Purpose | Status on this branch |
|---|---|---|
| [45 second pitch video](45-second-pitch-video.mp4) | Currently delivered root video (v15). Filename is Peter's label, not exact 45.000s | PRESENT. ffprobe 42.1s (metadata only). Sole root `.mp4`. |
| Judges walkthrough | Extra 3-minute walkthrough | PENDING. Not in this tree. |
| [report.html](report.html) | Idea, investigation, validation and cultural calendar | Static report with five recording-friendly sections. |
| `docs/` | Strategy, concept, hook bank, charts and aggregate tables | Supporting evidence. |

## Details for AI readers

### File map

- `docs/STRATEGY.md`: narrative and future post choices.
- `docs/CONCEPT.md`: original design, pipeline and prototype methods. Some early proposed ideas and policies are superseded by the report, especially timing and cultural coverage.
- `docs/hook-bank.md`: exactly 35 candidates, source-note names and H/M/L confidence labels. No saved per-criterion numeric scores.
- `docs/data/hook_review_summary.csv`: machine-readable transcription of the bank, with missing numeric totals explicit.
- `docs/data/events_angles_summary.csv`: selected aggregate birthplace, age and rent figures verified from local API responses. No raw responses.
- `docs/data/singles_suburbs.csv`: ABS 2021 Census summaries for 31 selected SALs. This is not identical to the API's 29-suburb scope.
- `docs/data/runclub_catchment_prototype.csv`: illustrative percentile-weighted score, not a validated attendance or relationship model.
- `docs/data/parking_comparison.csv`, `studio_comparison.csv`: filtered, deduplicated asking-rent comparisons.
- `docs/data/airbnb_by_suburb.csv`, `airbnb_vs_bond_1bed_postcode.csv`: Inside Airbnb aggregates and separate NSW bond-rent comparison.
- `docs/data/census_suburb_metrics.csv`, `food_drink_by_suburb.csv`, `hayfever_by_suburb.csv`: supporting investigations.
- `docs/charts/`: source-linked research charts and the hook-confidence summary.

### Methods and scoring

Pipeline: source data → normalise suburb or postcode → investigate hook → check claim and rights → match calendar → script → human approval → reel.

The design rubric has seven criteria, each proposed at 0–3: surprise, local identity, Microburbs tie-in, data strength, timing, non-political framing and licence clarity. Original release gates require Microburbs relevance ≥2, political-sensitivity clearance and verified reuse rights. We do not present a fictional 35-row numerical ranking. Birthplace and age shares are census-based via Microburbs; the response does not state the census reference year and birthplace lists only the top ten countries. Birthplace describes residents, not festival attendance. The calendar is hand-curated, not a live trend detector. Nearby residents are not run-club members; advertised rent gaps are not causal effects; tree counts are not pollen exposure. Darlington's rent rise compares different dates and housing mix, not a matched student-rent index. NYE accommodation prices were not measured; Songkran is a cultural-calendar sequel, not a confirmed Sydney event. Final video captions need a frame-by-frame check against these sources.

Run-club context sums published ABS G06 person counts for ages 20–24 and 25–34. Four whole suburbs inside a 1.5 km straight-line circle near Kings Cross sum to 3,631. Haymarket plus Ultimo sum to 4,844 near Darling Dash. Partial suburbs are excluded. Counts describe 2021 residents not living with a partner, not current singles, sexual orientation or club attendees. ABS perturbation means person totals need not equal male plus female cells.

Rental comparisons use the latest advert per `gnaf_pid`, dated from 1 Jan 2025, numeric weekly rent $100–$10,000. Parking comparisons restrict to one-bedroom, one-bathroom units with explicit zero or one space. Studio comparisons use recorded zero bedrooms, not missing values. These are different homes and asking rents, not signed leases. Market snapshots are dated 25 Oct 2026 and have undisclosed sample sizes. Historical medians are nominal and composition-sensitive.

Airbnb-versus-rent uses Sep 2026 NSW bond rents, not Microburbs rents. The equivalent nights calculation is weekly bond rent divided by nightly Airbnb price: $860 / $349.50 = 2.46 nights in postcode 2000. It is a price equivalence, not average stay length or a measured NYE surge. Prices exclude fees; 750 of 5,024 listings lack prices and locations are jittered.

Trees are council inventory records, not all trees or pollen measurements. Liquor counts are licence records, not independently verified open restaurants. Camera values are issued notices' face value, not money collected or resident behaviour.

### Sources and rights

- [Microburbs API](https://api-ht.microburbs.com.au/docs)
- [ABS 2021 Census DataPacks](https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=SAL&header=S)
- [ABS social marital status definition](https://www.abs.gov.au/census/guide-census-data/census-dictionary/2021/variables-topic/household-and-families/social-marital-status-mdcp)
- [Inside Airbnb data](https://insideairbnb.com/get-the-data/)
- [Inside Airbnb reuse policy](https://insideairbnb.com/data-policies/)
- [NSW rental bond data](https://www.nsw.gov.au/housing-and-construction/renting-a-place-to-live/rental-bonds/rental-bond-data)
- [City of Sydney tree inventory](https://data.cityofsydney.nsw.gov.au/datasets/15c4713a688a48fcb604fc343118af05_0/explore)
- [Revenue NSW camera notices](https://www.revenue.nsw.gov.au/help-centre/resources-library/statistics/all-speeding-and-red-light-camera-detected-offences-dsf010.xlsx)
- [Liquor & Gaming NSW premises list](https://www.nsw.gov.au/sites/default/files/noindex/2026-10/premises-list-oct-2026.xlsx)
- [Strava Year in Sport 2024](https://press.strava.com/articles/strava-releases-annual-year-in-sport-trend)
- [Sydney Marathon 2026](https://www.tcssydneymarathon.com/post/reigning-world-champions-lead-a-landmark-marathon-field-for-tcs-sydney-marathon)
- [Sydney Lunar Streets 2027](https://www.cityofsydney.nsw.gov.au/opportunities/join-sydney-lunar-festival-community-performance-program)
- [Thaitown events](https://www.thaitownsydney.com.au/whatson)
- [University of Sydney Welcome Program](https://welcome.sydney.edu.au/)
- [Songkran independent guide](https://www.songkranfestival.org/)
- [Kings Cross Track Club schedule](http://www.kingscrosstrackclub.com/weekly-schedule)
- [Darling Dash listing](https://whatson.cityofsydney.nsw.gov.au/events/the-run-club-at-darling-harbour)

Credit ABS, Inside Airbnb and City of Sydney under CC BY 4.0. Credit Liquor & Gaming NSW, © State of New South Wales 2026, CC BY 4.0. Revenue NSW's catalogue specifies Creative Commons Attribution without a version. Event pages supply paraphrased facts; their imagery and text are not assumed open-licensed. Strava supplies global survey context, not Sydney estimates.

Microburbs public redistribution terms require confirmation before public release, including for aggregate tables. Do not publish keys, raw API responses, `.env`, `mb_raw/`, `API_DATA.json`, NSW VG sales records or personal host information. Publication and submission need Peter's approval. Published branch/tag history was rewritten to drop `API_DATA.json`; GitHub pull-request refs and caches can still serve old SHAs.

### What is built and what is proposed

Built: research packs, 35-hook bank, aggregate tables, prototype score, manual cultural calendar and report. Video source and versions are on the creator branch. Proposed: live search-interest ingestion, automated ranking, scheduled weekly drafts, network-distance catchments and engagement validation. No view, conversion or dating-success result is claimed.

---

# The shipped reel: Are run clubs the new Love Island? (Team Sake)

The reel report lives at [docs/reel-report.html](docs/reel-report.html); the Where to Go for a Running Date report is [report.html](report.html).


> Repo stays **private** until a separate visibility gate. Published history was rewritten
> to remove `API_DATA.json`. GitHub pull-request refs and caches can still serve old SHAs;
> that is not erasure. Do not reintroduce raw API payloads. This update is not submission.

![Diagram of how Microburbs neighbourhood metrics, external club and place sources, and cultural calendar or trend inputs feed a human-led pick of a timely angle, then source checks, a shareable reel, and review. Calendar automation and watch-time feedback are labelled future and are not built. Designed for relevance and shareability, not guaranteed virality.](docs/pipeline.png)

Editable diagram: [docs/pipeline.tldraw.json](docs/pipeline.tldraw.json).

## What we built

A short vertical reel ([45 second pitch video](45-second-pitch-video.mp4), v15, **PRESENT**) that uses a run-club dating-culture hook
to teach what Microburbs' *lifestyle* score measures: access to cafes, restaurants, bars,
parks and recreation. Today this is **human-led**: one handmade video, not a live app or a
working content engine.

The diagram is the intended path: Microburbs metrics, external local sources, and cultural
or trend inputs into a timely, relevant, shareable video. A **repeatable** cultural-calendar
feed and a watch-time feedback loop are **future vision, not built**. Virality is a design
goal, not a guaranteed or measured result.

## Data

Illustrative social-club example (not the subject of the existing current pitch video):
[One Drop Brewing Run Club](https://onedropbrewingco.com.au/pages/whats-on) in Botany.
Botany is a different place from the Surry Hills lifestyle metric used in the lesson; do
not join them. Video club evidence stays in [report.html](docs/reel-report.html). An API
figure and a public ranking page disagree, so the exact score is omitted from the video
and is not treated as settled.

## Status

Sole currently delivered root video: [45 second pitch video](45-second-pitch-video.mp4)
(v15). ffprobe duration is **42.1s** (metadata only, not visual/audio QA); the title is
a label, not a claim of exact 45.000s. Obsolete root `demo.mp4` and `pitch.mp4` were
removed from the latest tree; private originals remain in backup. A judges walkthrough
is **PENDING** and is not in this tree. Content approval, organiser clearance,
publication, and submission remain **PENDING**. Limits, AI-scene labels, and media
metadata: [report.html](docs/reel-report.html).
