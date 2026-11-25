import os

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
