# Check plan — Task 1 docs/verify update (7 Nov 2026)

Saved before first documentation edit. Scope is docs and verification only. No media copy, no producer-branch edits, no force push, no visibility change, no history rewrite, no deploy, no submit.

## Repo facts observed before edits

- Branch base: `main` at `e20fdfa`. Files: `README.md`, `API_DATA.json`.
- No `AGENTS.md` or `CLAUDE.md` in any branch.
- Existing `README.md` collaborator notes to preserve: Instagram account line; `jthk` and `jthk's Grok Bot are in`.
- `API_DATA.json` is already on `main` and in history. It is private source. New docs must not reproduce it. Do not delete it.
- `origin/creator/runclub-reel` holds producer media. Do not touch. Current `pitch.mp4` is stale. Final paths pending. Do not copy videos.

## Derived facts allowed in docs (pointers only, no raw payloads)

- API path `/v1/suburbs/{suburb_name}/lifestyle/livability`, Surry Hills, scores list item `key=lifestyle`, value `94`, level `Very high`. Inspection date 7 Nov 2026. Sample has no source vintage date.
- API path `/v1/suburbs/{suburb_name}/lifestyle/livability-map` dimension `lifestyle` description: access to cafes, restaurants, bars, parks and recreation. Unit is a rescaled 0–100 score.
- Public page https://www.microburbs.com.au/People-Lifestyle/Top-suburbs-for-Lifestyle-Score/Sydney lists Surry Hills at 91.0 (fetched 7 Nov 2026). No version/vintage on the page sufficient to reconcile with 94.
- She Runs https://www.sheruns.com.au/sheruns : Wednesday 6:30am, 6 km, start St Mary's Cathedral, finish A.P. Bakery rooftop, Surry Hills. Publisher schedule, not observed.

## Explicitly unresolved / excluded

- 94 vs 91.0 is a failed independent cross-check, not a passed validation. Do not treat either figure as settled. Omit the exact score from videos. Do not substitute 91.0 for 94.
- No attendee ages, singles, dating odds, observed attendance, café/park counts, or rent comparison.
- No held-out predictive dataset. No audience/engagement tests. Do not invent them.
- No automatic content engine. Built artefact is a produced video (pending), not a live app.

## Checks to run after edits (this plan's pass/fail list)

1. Diff limited to docs/verify: `README.md`, `report.html`, `AGENTS.md`, `CHECK_PLAN.md`, `VERIFICATION.md`, `scripts/verify.py`. Optional `.gitignore`. No producer media, no `API_DATA.json` rewrite.
2. Preserve collaborator README lines.
3. Parse `report.html` with `html.parser`: required headings; no `<script>`; no remote CSS/fonts/assets; relative `demo.mp4`/`pitch.mp4` links may be absent (PENDING).
4. Source ledger: every numeric claim in README/report is on the verify allowlist.
5. Wording regressions: both 94 and 91.0 with sources; PROVISIONAL; failed independent cross-check; fictional AI dramatisation; `withoutMicroburbs` / `withMicroburbsAPI`; media PENDING; no exact-score-in-video recommendation; original music / Jono narration / map-not-generated-cathedral as planned final-reel notes, not as completed files.
6. Secret/raw-file scan of **introduced** files only. Do not print values. Do not dump `API_DATA.json`. Fail if new docs link to or embed raw API output.
7. `python3 scripts/verify.py --allow-pending` must exit 0 (docs-only).
8. `python3 scripts/verify.py` (strict) must exit non-zero while videos are missing.
9. Deliberate forbidden dummy file must fail verify; then remove the dummy.
10. Open `report.html` in headless Chrome and capture screenshots if Chrome is present; otherwise mark browser not checked.
11. No external integration/auth changes.
12. Land via normal commit/PR; merge/push `main` only as a non-force fast-forward/merge. Repo stays private.
