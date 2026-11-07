# microburbs-task1
Microburbs Hackathon Task 1: evidence, social creative and team delivery tracking

we'll use a instagram account today

jthk and jthk's Grok Bot are in.

# Are run clubs the new Love Island? (Team Sake, Task 1)

> **Private repo.** `API_DATA.json` is in git history. Do not make this public or rewrite
> history. This docs update does not publish or submit the entry.

![Diagram of how Microburbs neighbourhood metrics, external club and place sources, and cultural calendar or trend inputs feed a human-led pick of a timely angle, then source checks, a shareable reel, and review. Calendar automation and watch-time feedback are labelled future and are not built. Designed for relevance and shareability, not guaranteed virality.](docs/pipeline.png)

Editable diagram: [docs/pipeline.tldraw.json](docs/pipeline.tldraw.json).

## What we built

A short vertical reel (`demo.mp4`, v11, **PRESENT**) that uses a run-club dating-culture hook
to teach what Microburbs' *lifestyle* score measures: access to cafes, restaurants, bars,
parks and recreation. Today this is **human-led**: one handmade video, not a live app or a
working content engine.

The diagram is the intended path: Microburbs metrics, external local sources, and cultural
or trend inputs into a timely, relevant, shareable video. A **repeatable** cultural-calendar
feed and a watch-time feedback loop are **future vision, not built**. Virality is a design
goal, not a guaranteed or measured result.

## Who it helps

People new to Sydney who will watch a short dating-culture reel more readily than a dry
suburb profile. General public education only. No personal dating advice.

## Data

Illustrative social-club example (not the subject of the existing v11 video):
[One Drop Brewing Run Club](https://onedropbrewingco.com.au/pages/whats-on) in Botany.
Botany is a different place from the Surry Hills lifestyle metric used in the lesson; do
not join them. Frozen v11 media is unchanged and is documented in [report.html](report.html)
(including that video's original club evidence). An API figure and a public ranking page
disagree, so the exact score is omitted from the video and is not treated as settled.

## How to run

No app. Open [report.html](report.html), or:

```sh
python3 -m http.server 8000
python3 scripts/verify.py
python3 scripts/verify.py --allow-pending
```

## Status

v11 `demo.mp4` and `pitch.mp4` are present and were **not** remade for One Drop. Content
approval, organiser clearance, publication, and submission remain **PENDING**. Do not swap
in v12 or later. Limits, AI-scene labels, and media metadata: [report.html](report.html).
