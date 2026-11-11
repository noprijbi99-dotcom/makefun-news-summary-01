# make.fun bounty: Write the best summary of 11 November's world news

Bounty: https://make.fun/bounty/news-summary-01
Reward: $200 USDC (escrowed), top 20 entries share it; 1st place $40.
Deadline: **Fri 13 Nov 2026, 01:30 WIB** (Thu Nov 12, 18:30 UTC).
Status: BUILD COMPLETE, submission-ready. **Not submitted — awaiting the user's gas.**

## Fix note (independent pre-submit verification, 02:31 WIB)
A second agent re-checked the entry live and found one factual error in the Hormuz sentence: the 37-attack figure was October's total (not November's), and the tanker mine-strike was an Iranian claim, not independently verified. Fixed: "Iran said three tankers…" + "in October" (+2 chars net with two polish fixes: Rubio quote de-quoted to a paraphrase, "agreed on"). Re-ran determinism twice — new SHA-256 `e9860ccab19214ddb89e3d76f63a06c2883fcc23396d51229436269d52417726`, 1,922 chars. Commit amended (still exactly 1 commit).

## What this is
`main.py` (Python 3.13, standard library only) writes a fixed, researched
summary of world news of Wednesday 11 November 2026 to `/output/entry.txt`.
No network, no clock, no randomness — the program is a deterministic writer;
the value is the summary text itself, verified against 9 independent news
sources (see `SOURCES.md`).

## Files
| File | Contents |
|---|---|
| `main.py` | The entry program (root file required by the brief) |
| `summary.txt` | The exact summary text (1,922 chars, 5 paragraphs) |
| `SOURCES.md` | Source list + fact-to-source map + verified-but-cut items |
| `LICENSE` | MIT (OSI-approved, as the brief requires) |
| `brief.html` | The official brief page, saved for reference |

## Verified checks (2026-11-12 ~02:20 WIB; re-verified + fixed 02:31 WIB — see fix note)
- Summary: **1,922 characters** (limit 1–2,000), UTF-8, non-whitespace.
- Determinism: `python3 main.py` run twice → identical SHA-256 both runs:
  `e9860ccab19214ddb89e3d76f63a06c2883fcc23396d51229436269d52417726`
- Output byte-identical to `summary.txt` (`cmp` clean).

## How to run
```bash
python3 main.py        # writes /output/entry.txt
```

## Submission checklist (needs the user's hand)
1. Create a **public GitHub repo under the user's own account**
   (`noprijbi99-dotcom`), created after the competition opened, MIT license,
   with `main.py` at the repo root — **single commit**.
2. Upload the AI coding-agent session transcripts with the submission.
3. Submit at make.fun/bounty/news-summary-01 (Discord login + SOL wallet
   needed to enter/claim; entry itself is free).
4. Limits: max 10 submissions/day, 30 total; the **last submission before
   the deadline is the final entry**.
5. Judging: pairwise AI-judge ranking (Bradley-Terry); 718 entries were
   competing at last check — this entry competes on text quality alone.

## The summary (1,922 chars)
> The U.S.-Iran war dominated the day. Secretary of State Marco Rubio said in
> Paris the economic pressure campaign was working so well there was no need for
> major combat operations any longer, though force remained possible if Iran
> crossed "certain red lines." Tehran's security chief Mohsen Rezaei said Iran
> still awaited a U.S. answer to its seven conditions, that Hormuz would stay
> closed until they were met, and that no enriched uranium would leave Iran.
> Iran said three tankers caught fire Tuesday after hitting naval mines, and
> monitors counted 37 attacks on ships near Hormuz in October, the most since
> the war began.
>
> In Abu Dhabi, day one of Ukraine-Russia-U.S. talks was "constructive and quite
> substantive," President Zelenskyy said, and the sides agreed on the war's
> biggest prisoner exchange, U.S. envoy Jared Kushner said. NATO scrambled jets
> after at least four drones strayed into Baltic airspace; no one was hurt. In
> Gaza, Israeli strikes killed at least seven people, including a father and his
> 13-year-old son, health officials said.
>
> At COP31 in Antalya, U.N. chief Antonio Guterres warned the slow response had
> put the world "on a path to destruction," while five nations backed doubling
> rooftop solar by 2030.
>
> Markets rebounded as CoreWeave's results calmed AI-bubble fears: revenue
> jumped 168% to $3.7 billion, and its shares rose about 15%. Nvidia recovered
> after losing $430 billion in two days; the Nasdaq rose 1.2%. But hot October
> inflation pushed the 10-year Treasury yield above 5%, with traders pricing a
> possible half-point Fed rise in December. OpenAI's quarterly revenue topped
> $10 billion.
>
> The House voted 211-204 to bury a bid to impeach Defense Secretary Pete
> Hegseth, and the Justice Department charged three Iran-backed operatives over
> plots including one at a British air base. Congo's Ebola outbreak reached
> 11,042 cases and at least 5,387 deaths, the second-deadliest on record.
