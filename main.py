"""The One-Line Laugh: writes one funny line to /output/entry.txt, deterministically."""

import os

# Revision: the anxiety stops being a passive condition and becomes a rival
# doing the same exercise back, better. The turn lands on "only better".
LINE = "I've been doing breathing exercises for my anxiety, and now my anxiety is doing them back, only better."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
