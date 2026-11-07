# Sydney social run clubs: source notes

Checked 7 November 2026 (Sydney time). 13 distinct clubs, 15 meeting/session rows. This is a sourced shortlist, not an exhaustive or popularity-ranked census. Every CSV row is supported by a page actually retrieved with WebFetch, except Frontrunners retrieved successfully with curl after a fetch-provider 403. Published schedules are not live attendance confirmation. All schedule times are Sydney local time (AEDT on check date; recurring schedules follow local daylight saving).

## Coverage and mapping
Redfern, South Eveleigh, Pyrmont, CBD/Darling Harbour, Darlinghurst, Surry Hills, Centennial Park, Bondi Beach, Bronte, Camperdown, Glebe, St Peters and Kirribilli/Milsons Point. Kings Cross is retained as a locality, not invented as a suburb. Inner West Run Club is listed as Newtown by its directory, but its actual meeting points are Camperdown/Glebe and St Peters. No Newtown-suburb meeting point was verified. She Runs meets in CBD and finishes in Surry Hills. Do not map the finish as the start. Nearby suburbs are intentionally included; this file does not assert exact LGA membership or geocoded boundaries. Geocode landmarks and intersect LGA boundaries before Microburbs joins.

## Sources and confidence
High = direct club/organiser schedule or club-managed event page; Medium = secondary directory/guide, stale dates, or incomplete recurrence. High does not mean independently observed turnout.

- Redfern Run Club: https://www.redfern-run.club/
  Confidence: High. 5km; site counters render as zero and are not attendance evidence. 5km; finishes at YohoLoco.
- The Sydney Run Club: https://thesydneyrunclub.com.au/
  Confidence: High. 6km Bondi to Bronte. Size is self-reported club-wide weekly total, NOT Bondi attendance.
- Sydney Frontrunners: https://www.sydneyfrontrunners.org/our-runs-2/saturday-runs/
  Confidence: High. Official page read via curl after WebFetch 403. Visitors welcome.
- Monday Run Club: https://www.runhub.co/clubs/monday-run-club
  Confidence: Medium. Directory only; 6–8km social run; confirm current venue with club.
- Inner West Run Club: https://rundais.org/run-clubs/inner-west-run-club/
  Confidence: Medium. Directory labels club Newtown; meeting locations differ. Which venue applies this week is not stated. Directory labels club Newtown; this meeting address is St Peters. Runs around Sydney Park.
- Midnight Runners Sydney: https://www.heylo.com/g/8a9462a8-80f9-46b7-9ab6-f76192cde5d6
  Confidence: High. Club-managed Heylo About text explicitly says Wednesday nights 6.15PM. Machine event preview has ambiguous timezone; ignored. Active members/check-ins are not attendance.
- Kings Cross Track Club: http://www.kingscrosstrackclub.com/weekly-schedule
  Confidence: High. Official schedule. Kings Cross is a locality, not a suburb/LGA assignment; geocode landmark before demographic join. Thursday track session excluded.
- She Runs: https://www.sheruns.com.au/sheruns
  Confidence: High. 6km social run. Surry Hills is finish, not meeting point. No participant demographics or attendance inferred.
- The Shop Run - Sydney (Up There Athletics): https://upthereathletics.com/pages/the-shop-run
  Confidence: Medium. Official 2026 recurrence; listed Sydney dates stop at 12 October and include exceptions. Next date not confirmed; do not extrapolate calendar.
- 440 Run Club Bronte: https://www.runhub.co/clubs/440-run-club-bronte
  Confidence: Medium. Directory confirmed broad meeting landmark; exact assembly spot not established from this page.
- Unofficial Run Club: https://www.unofficialrunclub.com/
  Confidence: High. Official footer says Kirribilli; FAQ calls steps Milsons Point. Preserve both until exact boundary checked. Nearby, not City of Sydney LGA.
- A.P. Run Club, Bondi Beach Run Club: https://reyourrun.com.au/blogs/running/best-run-clubs-sydney-nsw
  Confidence: Medium. Secondary commercial guide dated 15 July 2026. No next date or street address given; route around Moore Park. Secondary commercial guide dated 15 July 2026; confirm current club schedule. Distinct from The Sydney Run Club.

## Limits and uncertain details
- Monday Run Club, Inner West Run Club, 440, A.P. and Bondi Beach Run Club are secondary-source schedules; confirm club announcements before filming or attending.
- Inner West Tuesday venue alternates; no current-week choice established.
- Shop Run page gives fortnightly Mondays but stale/exceptional dated examples. Next date unverified.
- A.P. runs only selected Sundays; no next event or street address established.
- 440 source gives Bronte Beach, not an exact assembly point.
- Unofficial site uses both Kirribilli and Milsons Point labels; resolve location boundary before suburb comparison.
- No per-session turnout was established. Only Sydney Run Club supplies a weekly club-wide 1,000-runner claim, explicitly labelled as such in the CSV. Instagram followers, membership, cumulative check-ins and event-preview member counts are not attendance and are excluded.
- Redfern site’s zero counters appear unpopulated; not used as size data.
- Re. is a commercial running-eyewear guide, not a neutral audit. Its Thursday KXTC time differs from the official schedule; official page takes precedence. That Thursday session is not included.
- No claim about attendees’ age, relationship status, sexuality or likelihood of finding a partner is supported by these sources. Area demographics are not club demographics. No dating-probability score should be derived from these meeting points.
