# Check plan — README + pipeline diagram (7 Nov 2026)

Saved before this docs edit. Additive commit to private `main` only. No force
push, no history rewrite, no visibility change, no publication, no submission.
`API_DATA.json` and v11 `demo.mp4` / `pitch.mp4` stay untouched.

## Intended change

- Add `docs/pipeline.png` (inspected PNG, 3552×3588, no overlaps) and
  `docs/pipeline.tldraw.json`.
- Short README (about 250–450 words) with collaborator opening lines verbatim.
- Sections: What we built, Who it helps, Data, How to run, Status.
- Diagram prominent with meaningful alt text. Human-led today; calendar feed and
  feedback are future, not built. Virality is a design goal, not measured.
- Score 94 vs 91.0 stays in `report.html`, not as README headlines.
- Adapt `scripts/verify.py` README assertions; keep report factual/safety checks.

## Verify after edits

1. Markdown relative image/links resolve (`docs/pipeline.png`, `report.html`).
2. PNG signature + dimensions recorded.
3. `python3 scripts/verify.py` exit 0.
4. Hide `docs/pipeline.png` once: strict verify fails; restore; pass again.
5. demo/pitch SHA256 unchanged.
6. Secret/forbidden scan still runs; allowlisted `docs/pipeline.tldraw.json`.
7. Rebuild history-free ZIP (no `.git` / `API_DATA.json`); export README
   distinguishes export vs source repo. Fresh unzip + strict verify.
8. Push additive commit to `main`.
