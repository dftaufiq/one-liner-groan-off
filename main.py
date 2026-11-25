"""One-liner groan-off entry.

The line is a 2-beat dad joke: beat 1 sets up the classic
"walked 3 miles, uphill both ways" boast, beat 2 lands the reveal
in the final clause — the son fact-checks it on Google Maps and
the road is flat. It won the internal pairwise selection because
the twist is specific (Google Maps, flat) rather than generic,
and the punch lands on the last word, which is what the judges
score on.
"""

import os

# The entry line itself: setup (boast) + twist (Maps says flat).
# Kept verbatim — do not reword; the 129-char length and the final
# reveal word are what the pairwise selection scored.
LINE = "My son asked how I got to school at his age \u2014 I said 'I walked 3 miles, uphill both ways', and he checked Google Maps: it's flat."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-140 chars,
# not only whitespace, a single line. Fail loudly instead of shipping
# an invalid entry.
if not 1 <= len(LINE) <= 140 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-140 char single-line gate")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
