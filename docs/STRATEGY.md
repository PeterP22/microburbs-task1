# Suburb Secrets: strategy

> Working title. Alternatives: "Know Your Postcode", "Postcode Gossip", "Sydney, Decoded".
> This strategy drives the design of `report.html` and the final `demo.mp4`. It is also the draft README.

We built a small engine that turns Microburbs data and open data into timely, shareable insights into Sydney's suburbs, culture and life, and used it to make a short reel: *Is your run club the new Love Island?*

## What we did

- Pulled Microburbs rent, sales and property data for the City of Sydney's 29 suburbs, and joined it with open data from the census, Inside Airbnb, the council's tree register, Revenue NSW and liquor licences.
- Generated and scored 35 candidate hooks for surprise, local identity, Microburbs tie-in, data strength, timing, staying out of politics and clean licensing.
- Picked run clubs and singles as the flagship. Census figures on young singles plus Microburbs signals for young renters show which suburbs are "run club catchments".
- Checked every on-screen number back to its source, with caveats shown on screen.
- Matched hooks to the cultural calendar, because timing is part of the attention game.

## Timing: what would have landed

- **Sydney Marathon, 30 Aug 2026:** the run club reel, with record marathon demand driving the run-club wave.
- **Spring hay fever, Sep–Nov 2026:** "It's not the maples", 24 plane trees for every maple, with Darlinghurst the plane-tree capital.

## Timing: future posts worth considering

- **New Year's Eve, 31 Dec 2026:** "Rent vs rent", where 2.5 Airbnb nights cost a week's rent, as harbourside stays spike.
- **Mardi Gras, 6 Mar 2027:** the parade runs down Oxford St through Darlinghurst and Surry Hills, which leads into what living there really costs, using Microburbs rent data.

## What's in the repo

- `pitch.mp4`: the 45-second reel.
- `demo.mp4`: a walkthrough of the report.
- `report.html`: the idea, method, validation and next steps.
- `docs/`: the concept, the hook bank, charts and summary tables.

---

## Details for AI readers

- Event dates verified on official pages, 7 Nov 2026: [TCS Sydney Marathon](https://www.tcssydneymarathon.com/post/reigning-world-champions-lead-a-landmark-marathon-field-for-tcs-sydney-marathon) (Sun 30 Aug 2026), [Mardi Gras Parade](https://www.mardigras.org.au/event/parade/) (Sat 6 Mar 2027, Oxford St, Flinders St and Anzac Pde).
- "Record marathon demand": Destination NSW described Sydney as the world's fastest-growing marathon, targeting 40,000 finishers in 2026. No Sydney run-club growth figure is claimed.
- Figures and sources: `docs/hook-bank.md` (24 planes per maple: 4,017 plane vs 167 maple trees, City of Sydney tree inventory, CC BY 4.0; 2.5 nights: median whole 1-bed Airbnb nightly price vs median 1-bed bond rent, 2.2–3.2 nights across 15 postcodes, Inside Airbnb CC BY 4.0 and NSW bond data).
- The Mardi Gras post needs a fresh Microburbs pull of Darlinghurst and Surry Hills rents before any number is shown.
- Demo structure: (1) hook, about 20 s of the reel; (2) pipeline diagram from `docs/CONCEPT.md`; (3) validation, tracing each on-screen number to its source; (4) timing layer and next episodes.
