# Run club reel: Microburbs data beat

## For humans

Add a 5–8 second data beat to the run club reel (branch `creator/runclub-reel`), after the Strava line and before the club map. It gives the reel a Microburbs reason to exist.

**Locked lines**
1. "Haymarket and Ultimo: 4,844 single 20–34s live right where Darling Dash runs on Mondays."
2. "3,631 more live within 1.5 km of Kings Cross's Tuesday social run."
3. Punchline: "Surry Hills: 123.5 single men for every 100 single women."

**Microburbs frame:** one quick chart showing that the suburbs full of studio and one-bed rental ads are the run club suburbs.

**End card:** "Find your suburb's run club catchment on Microburbs."

---

## Details for AI readers

**On-screen caveats (required, small text):**
- Lines 1 and 3: "2021 Census, aged 20–34, not living with a partner."
- Line 2: "2021 Census, approximate 1.5 km catchment."
- Line 3 also: "Residents, not runners."

**Rules**
- Never say "single" without the census caveat. "Single" here means a person aged 20–34 not living with a spouse or de facto partner (ABS social marital status). It is not dating status.
- Don't claim run clubs replace dating apps. The Strava line stays qualified as it already is.
- Don't show the run club catchment score; its weights are illustrative only.
- Every number must match `docs/hook-bank.md` exactly. No rounding beyond what's written here.

**Sources and files**
- Census figures: ABS 2021 Census, General Community Profile (G05/G06), CC BY 4.0, credit "Australian Bureau of Statistics". Aggregated table: `docs/data/singles_suburbs.csv`.
- Catchment method: run start points from public club pages; suburbs wholly inside an approximate 1.5 km circle were summed (Kings Cross, Tuesday, four suburbs: 3,631). Darling Dash figure is Haymarket + Ultimo combined (4,844).
- Microburbs frame: `docs/charts/studio_vs_bedroom.png` (median weekly asking rent, studio vs one-bed, from Microburbs rent-history listings) or `docs/charts/singles_runclubs.png`.
- Microburbs endpoints behind the full version: `/suburbs/{S}/listings/rent-history` (bedrooms, weekly_rent, car_spaces), `/suburbs/{S}/market/all` (house vs unit medians). See `docs/CONCEPT.md`, run club section.

**Timing slot in the current v2 reel (`creative/reel-vo.json`):** insert after the segment ending at about 15.5 s ("...not just running.") and before "So we mapped 13 Sydney run clubs" (about 16.1 s). Re-time the following segments; keep the total ≤45 s.
