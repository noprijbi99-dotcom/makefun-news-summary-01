"""
make.fun news-summary-01 entry script.

This script implements a deterministic news summary generator for 11 November 2026.
It adheres to the following contract:
- No network access.
- No clock or time-based dependencies.
- No randomness or non-deterministic behavior.
- Embedded summary text is written exactly as-is to /output/entry.txt.
- Output is encoded in UTF-8.
"""

import os

# Locked 11 November 2026 world-news summary
SUMMARY = (
    "The U.S.-Iran war dominated the day. Secretary of State Marco Rubio said in "
    "Paris the economic pressure campaign was working so well there was no need for "
    "major combat operations any longer, though force remained possible if Iran "
    "crossed \"certain red lines.\" Tehran's security chief Mohsen Rezaei said Iran "
    "still awaited a U.S. answer to its seven conditions, that Hormuz would stay "
    "closed until they were met, and that no enriched uranium would leave Iran. "
    "Iran said three tankers caught fire Tuesday after hitting naval mines, and "
    "monitors counted 37 attacks on ships near Hormuz in October, the most since "
    "the war began.\n\n"
    "In Abu Dhabi, day one of Ukraine-Russia-U.S. talks was \"constructive and quite "
    "substantive,\" President Zelenskyy said, and the sides agreed on the war's "
    "biggest prisoner exchange, U.S. envoy Jared Kushner said. NATO scrambled jets "
    "after at least four drones strayed into Baltic airspace; no one was hurt. In "
    "Gaza, Israeli strikes killed at least seven people, including a father and his "
    "13-year-old son, health officials said.\n\n"
    "At COP31 in Antalya, U.N. chief Antonio Guterres warned the slow response had "
    "put the world \"on a path to destruction,\" while five nations backed doubling "
    "rooftop solar by 2030.\n\n"
    "Markets rebounded as CoreWeave's results calmed AI-bubble fears: revenue "
    "jumped 168% to $3.7 billion, and its shares rose about 15%. Nvidia recovered "
    "after losing $430 billion in two days; the Nasdaq rose 1.2%. But hot October "
    "inflation pushed the 10-year Treasury yield above 5%, with traders pricing a "
    "possible half-point Fed rise in December. OpenAI's quarterly revenue topped "
    "$10 billion.\n\n"
    "The House voted 211-204 to bury a bid to impeach Defense Secretary Pete "
    "Hegseth, and the Justice Department charged three Iran-backed operatives over "
    "plots including one at a British air base. Congo's Ebola outbreak reached "
    "11,042 cases and at least 5,387 deaths, the second-deadliest on record.\n"
)

def main():
    """Main execution function to write the summary to the output directory."""
    output_dir = "/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "entry.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(SUMMARY)

if __name__ == "__main__":
    main()
