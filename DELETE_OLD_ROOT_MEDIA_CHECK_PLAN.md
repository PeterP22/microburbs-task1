# Check plan — delete obsolete root demo.mp4 / pitch.mp4 (7 Nov 2026)

Saved before removing those two files from the latest tree. No history rewrite.
Do not touch the private backup bundle or `creator/runclub-reel` producer sources.
Repo stays PRIVATE. No visibility change, GitHub Support contact, or submission.

## Approval

Peter 15:17 AEDT (private chat): delete old ones, screenshot of main file list with
`demo.mp4` / `pitch.mp4` / V15. Scoped to remove obsolete root `demo.mp4` and
`pitch.mp4` only. Retain `45-second-pitch-video.mp4` (V15) and private originals.
This supersedes the earlier keep-v11-at-root instruction. Main-file push authorised.

## Private originals (availability / hashes — do not modify backups)

Agent Store bundle (verified, not modified this run):
`/cursor/stores/self/microburbs-task1-pre-sanitize-backup/`
- `all-refs.bundle` sha256 `f3ec47c26865a7214b7cc1c4ebb41a97d5fa7fef3e9dfb5e000d2951e5f753e4`
- `MEDIA_HASHES_AT_BACKUP.txt`:
  - demo.mp4 33815279 `99d3ed08f48f101c7025e524efb3cb3bb3b0538759aa9ccc564795c2a5aca4c1`
  - pitch.mp4 36459899 `f322bb0ed0f0cc3abff56e5457c3f9010a64fa7294325712b507406ebb4af9a8`
Peter’s owner-only box copy:
`/home/box/.local/share/microburbs-private-backups/2026-11-07-pre-sanitize`
(not mounted on this VM). Current main `5a6096f` tree hashes match the bundle
record. After deletion, v11 bytes remain in git history (no rewrite) and in those
private copies. Creator-branch draft videos are untouched.

## Do

1. Remove only root `demo.mp4` and `pitch.mp4`.
2. Keep `45-second-pitch-video.mp4` name and bytes. Validate SHA256
   `e34a6fbbe5e7dd59964631bc4963e0146bd7cc27a84f659d92dfb03d07c94fa9`,
   42.1s, 1080x1920, h264/aac.
3. Point current reel links at V15 or drop obsolete hrefs so demo/pitch links
   do not 404. Judges-walkthrough: pending, do not claim it exists.
4. Update README / AGENTS / reel-report current media status and the strict
   verifier allowlist. Do not rewrite historical research (`docs/STRATEGY.md`
   etc.) or audit plans.
5. Strict `python3 scripts/verify.py`. Root `*.mp4` is only V15 unless a
   separately approved judges-walkthrough is already on live main (preserve it).

## Do not

Rename V15, regenerate media, delete other evidence/docs, rewrite history,
change visibility, submit, or contact GitHub Support.
