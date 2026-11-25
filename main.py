"""One-Line Office Jokes — make.fun entry.

Writes a single office joke line to entry.txt in MAKEFUN_OUTPUT_DIR.
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = "Our Monday standup is the only meeting where everyone stands, nobody stands for anything, and the printer still jams out of solidarity."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
