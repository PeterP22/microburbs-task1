# Verification report — README + pipeline diagram (7 Nov 2026)

Additive docs on private `main`. Not publication or submission.
`API_DATA.json` and v11 media were not modified.

Model: Cursor Grok 4.5

## README

- Collaborator opening lines kept verbatim.
- Word count: 347 (target about 250–450).
- Sections: What we built, Who it helps, Data, How to run, Status.
- Diagram: `docs/pipeline.png` (3552×3588 PNG) + `docs/pipeline.tldraw.json`.
- Human-led today; calendar/feedback not built; virality not guaranteed.
- Unresolved score kept in `report.html`, not headlined in README.

## Commands

```sh
python3 scripts/verify.py
python3 scripts/verify.py --allow-pending
```

- strict → exit **0**
- Hide `docs/pipeline.png` → exit **1** (`README image resolves` fail); restore → **0**
- demo SHA256 `99d3ed08f48f101c7025e524efb3cb3bb3b0538759aa9ccc564795c2a5aca4c1`
- pitch SHA256 `f322bb0ed0f0cc3abff56e5457c3f9010a64fa7294325712b507406ebb4af9a8`

Report factual/safety checks unchanged. Secret/forbidden scan ran (values not printed).
