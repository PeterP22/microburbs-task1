# Agent notes (Team Sake, Task 1)

Do not change visibility, deploy, or submit without a separate explicit approval after
independent verification of the cleaned refs. Do not commit ZIP transport parts.

Published history was rewritten to drop `API_DATA.json`. Do not reintroduce that file,
raw API payloads, `.env`, keys, or personal data. GitHub pull-request refs and caches
can still serve old SHAs; a refs audit is not complete erasure.

Unique producer work on `creator/runclub-reel` (Remotion source and draft videos) is
retained on that branch. Do not edit that branch in this deletion.

Root currently delivered videos are `45-second-pitch-video.mp4` (v15, Peter's
"45 second pitch video" label; ffprobe 42.1s) and `judges-walkthrough-v2.mp4`
(3 minute judges walkthrough, corrected v2; ffprobe 180.0s 1920x1080). Do not
rename them. Peter 15:17 AEDT removed obsolete root `demo.mp4` and `pitch.mp4`
from the latest tree; do not restore them without a new approval. Originals remain
in the private pre-sanitize backup.

Commit videos as normal Git blobs, never Git LFS pointers. Final user approval and
publication remain PENDING. ffprobe is metadata only, not visual/audio QA.

## Commands

```sh
python3 -m http.server 8000
python3 scripts/verify.py
python3 scripts/verify.py --allow-pending
```

## Facts that must stay honest

- Lifestyle score 94 (API) vs 91.0 (public ranking) is **PROVISIONAL** and unresolved.
- Omit the exact score from videos until organiser clarification.
- AI friendzone / mutual-flirting clips are fictional dramatisation labels
  `withoutMicroburbs` and `withMicroburbsAPI`, not a promised Microburbs outcome.
- Built artefact: one produced pitch video at root, files PRESENT, approval PENDING.
  Future vision: repeatable format. No working content engine exists here.
- Latest `main` README (post 8aa4664 / 4e353b7) dropped the older collaborator opening
  lines; those lines remain in the private pre-sanitize backup at `ae354e4`.
