# Task 1: Is your run club the new Love Island?

Draft only. Not published or submitted. Silent, burned-in text, no faces, no generated footage. First frame doubles as a text-free cover. Hook appears immediately after that frame.

## Files and reproduction

- `demo-v1.mp4`: 30-second, 1080 × 1920, 30 fps H.264 reel with no audio stream.
- `review/`: four sampled frames plus the text-free opening frame.
- `remotion/`: reproducible Task1Reel source and exact props. Run `npm ci`, then `bash render-task1.sh` inside that directory.
- Source project on box: `/workspace/remotion`; output: `/workspace/hackathon-video/task1/demo-v1.mp4`.

## Every figure and factual claim

1. **Nearly 1 in 5 Gen Z survey respondents had dated someone they met through exercise.** Source: [Strava Year in Sport 2024 press release](https://press.strava.com/articles/strava-releases-annual-year-in-sport-trend). Source wording is "went on a date". Global survey of active people, exercise overall, not Sydney, not run clubs specifically, not a life-partner outcome or an individual probability. Reopened and checked 7 November 2026 (Sydney AEDT).
2. **13 clubs.** Source: 13 distinct `name` values in [run-clubs.csv](run-clubs.csv), which includes repeat session rows for Redfern and Inner West. This is a sourced shortlist, not an exhaustive census. Each club's source URL and verification caveats are in [run-clubs-sources.md](run-clubs-sources.md). We do not display club turnout, audience demographics or schedules as findings.
3. **6am alarm.** Comedic line, not an attendance time or a claim every club runs at that hour. The on-screen caveat says to check the club.
4. **2024.** Strava report year, from the press release above. Video format/duration and club index labels are production metadata, not demographic findings.

## Map and scope limits

- The Sydney map is an original vector **schematic**, not an accurate boundary/navigation basemap. All club markers are **approximate suburb/locality areas**, explicitly labelled on-screen. No club has been geocoded, so no exact meeting-location pin is asserted. Coordinates in `task1.json` are layout pixels, not latitude/longitude.
- Bondi, Bronte and Centennial Park clubs are grey, labelled outside City of Sydney when featured. Kirribilli/Milsons Point is likewise grey and outside City of Sydney.
- Pink means local-area shortlist, not a verified LGA boundary intersection. Inner West's alternating Camperdown/Glebe venue is unresolved. Club labels must not be joined to suburb demographics without resolving the venue and LGA boundaries.
- She Runs is labelled with its CBD start and Surry Hills finish in the source data. No finish is asserted as an exact meeting pin.
- No Microburbs local values, age beat, relationship-status inference or invented dating score. No restricted organiser CSV or credentials are included. The CSV here is the independently researched club shortlist.
- Love Island is a joke only. No numerical comparison to the programme.

## Timeline

- 0–3s: Sydney and locked hook (opening frame has no text).
- 3–8s: qualified Strava signal.
- 8–22s: sequential approximate-area markers for the 13 unique clubs.
- 22–27s: unknown soulmate odds / alarm punchline.
- 27–30s: sources and limitations.

## Visual review

Four samples at 1.5s, 5s, 18s and 28s checked for text clipping, source qualification, map caveats and source card. Opening frame checked separately for no text. Typography is burned in; no face imagery exists to obscure. `ffprobe` verification is recorded in `review/ffprobe.json`.
