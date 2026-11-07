# Verification report — Team Sake Task 1 (7 Nov 2026)

Docs + reconstructed root media. **Not** Peter final content approval, **not** publication,
**not** submission, **not** visual/audio QA.

Model in this run: Cursor Grok 4.5.

## Reconstruction (scratch only)

Transport ZIPs were unzipped under `/tmp/video-scratch/`. Concatenation:

```sh
cat demo.mp4.part00 demo.mp4.part01 > /workspace/demo.mp4
cat pitch.mp4.part00 pitch.mp4.part01 pitch.mp4.part02 > /workspace/pitch.mp4
```

ZIP parts, manifests, and scratch files were **not** committed.

## Hashes and sizes

| File | Bytes | SHA256 |
|---|---|---|
| `demo.mp4` | 33815279 | `99d3ed08f48f101c7025e524efb3cb3bb3b0538759aa9ccc564795c2a5aca4c1` |
| `pitch.mp4` | 36459899 | `f322bb0ed0f0cc3abff56e5457c3f9010a64fa7294325712b507406ebb4af9a8` |

Both match the producer handoff. Both are ISO MP4 blobs (`file(1)`), not Git LFS pointers.
Each is under 95,000,000 bytes.

## ffprobe (metadata only)

```sh
ffprobe -v error -show_entries stream=codec_name,codec_type,width,height:format=duration,size -of json demo.mp4
ffprobe -v error -show_entries stream=codec_name,codec_type,width,height:format=duration,size -of json pitch.mp4
```

| File | Duration | Size | Video | Audio |
|---|---|---|---|---|
| `demo.mp4` | 39.900 s | 1080x1920 | h264 | aac |
| `pitch.mp4` | 45.000 s | 1080x1920 | h264 | aac |

These checks do **not** assert picture, sound, pace, or user content approval.
v11 producer notes recorded in docs: original music, fictional AI dating contrast, no disputed 94.

## Docs verifier

```sh
python3 scripts/verify.py --allow-pending
python3 scripts/verify.py
```

Recorded after this file was written:

- `python3 scripts/verify.py --allow-pending` → exit **0**
- `python3 scripts/verify.py` → exit **0** (metadata only; approval still PENDING)
- Dummy `secret-dummy.csv` (added then removed): `--allow-pending` exit **1**
  (`unexpected file` + `forbidden file name`). Dummy was deleted.

## Other checks

- `CHECK_PLAN.md` saved before first docs edit.
- No `AGENTS.md`/`CLAUDE.md` existed in the repo; `AGENTS.md` was added.
- Existing README collaborator lines preserved (Instagram; jthk / Grok Bot).
- `API_DATA.json` left untouched; not copied into docs; repo stays PRIVATE.
- Score 94 vs 91.0 remains PROVISIONAL / failed independent cross-check.
- Headless Chrome rendered `file:///workspace/report.html` at 1280px and 390px.
  Screenshots confirmed the dual 94 vs 91.0 figures, PRESENT media status, and
  PENDING approval banners. Those PNG files are not in the repo.

## Blockers remaining

- Final user / Peter **content** approval: still pending.
- Publication and hackathon **submission**: still not approved.
- Visibility change and history rewrite: not authorised (`API_DATA.json` in history).
- 3-minute walkthrough: extra, not this hand-in.
