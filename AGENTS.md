# Agent notes (Team Sake, Task 1)

Do not edit `creator/runclub-reel`. Do not force-push, change visibility, rewrite
history, deploy, or submit. Do not commit ZIP transport parts or manifests.

Repo remains **PRIVATE** because `API_DATA.json` is in history. Do not reproduce that
file in new docs. Do not delete it as a visibility fix.

Root `demo.mp4` and `pitch.mp4` are reconstructed producer originals. Commit them as
normal Git blobs, never Git LFS pointers. Final user approval and publication remain
PENDING. ffprobe is metadata only, not visual/audio QA.

## Commands

```sh
python3 -m http.server 8000
python3 scripts/verify.py
python3 scripts/verify.py --allow-pending
```

## Facts that must stay honest

- Lifestyle score 94 (API) vs 91.0 (public ranking) is **PROVISIONAL** and unresolved.
- Omit the exact score from videos until organiser clarification. v11 has no disputed 94.
- AI friendzone / mutual-flirting clips are fictional dramatisation labels
  `withoutMicroburbs` and `withMicroburbsAPI`, not a promised Microburbs outcome.
- Built artefact: one produced reel plus pitch, files PRESENT, approval PENDING.
  Future vision: repeatable format. No working content engine exists here.
- Preserve the existing README collaborator notes (Instagram; jthk / Grok Bot).
