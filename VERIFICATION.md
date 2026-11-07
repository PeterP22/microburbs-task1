# Verification report — root media now V15 only (7 Nov 2026)

Private repo. Not publication or submission. Visibility stays private.
Obsolete root `demo.mp4` and `pitch.mp4` removed from the latest tree only.
No history rewrite. Private backup untouched. Judges-walkthrough not present.

Incoming/current V15 check is hash + ffprobe metadata only, not visual/audio QA.

## Media

- 45-second-pitch-video.mp4 SHA256 `e34a6fbbe5e7dd59964631bc4963e0146bd7cc27a84f659d92dfb03d07c94fa9`
  30997081 bytes; ffprobe 42.100s 1080x1920 h264/aac
  git blob `d965df13d4b6c267e227694908b04cfe5ea5b1aa`
- Removed from latest tree (originals in private backup / git history):
  - demo `99d3ed08f48f101c7025e524efb3cb3bb3b0538759aa9ccc564795c2a5aca4c1`
  - pitch `f322bb0ed0f0cc3abff56e5457c3f9010a64fa7294325712b507406ebb4af9a8`

## Commands

```sh
python3 scripts/verify.py
```
