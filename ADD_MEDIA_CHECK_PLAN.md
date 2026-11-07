# Check plan — additive v15 45-second-pitch-video (7 Nov 2026)

Saved before copying the transferred file into the git tree. Cleanup already
happened; this does not redo the private backup or rewrite history. Repo stays
PRIVATE. STOP before changing visibility. No submission.

## Approval (this add)

Peter via creator 15:10 AEDT: add v15 as **45 second pitch video**, file
`45-second-pitch-video.mp4`, after history cleanup verification. Additive only.

## Do not

- Replace `demo.mp4` or `pitch.mp4` (canonical v11 hashes stay fixed).
- Claim exact 45.000s; user title is a label. If duration is mentioned, use 42.1s.
- Claim visual/audio QA. Incoming check is hash + ffprobe metadata only.
- Change visibility, submit, post, or produce other videos.
- Reintroduce `API_DATA.json` or weaken secret/raw-dump scans.

## Incoming (verify before git add)

- Path: `/cursor/stores/self/incoming-v15/45-second-pitch-video.mp4`
- SHA256 `e34a6fbbe5e7dd59964631bc4963e0146bd7cc27a84f659d92dfb03d07c94fa9`
- 30997081 bytes; ffprobe 42.100s 1080x1920 h264/aac; not a Git LFS pointer.

## After copy

1. Working-tree SHA256 and `git hash-object` recorded; match incoming.
2. README links the file with the title **45 second pitch video**.
3. Allowlist + strict `python3 scripts/verify.py` include the extra asset;
   v11 demo/pitch expected hashes unchanged.
4. Push the additive branch. Leave the GitHub repo PRIVATE.
