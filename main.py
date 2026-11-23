"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the entrant's honest count of open browser tabs as a single
digits-only number to $MAKEFUN_OUTPUT_DIR/entry.txt.

The count is 137: far above the handful of tabs most people keep open,
so it reads as surprising, yet still a number a real tab hoarder could
have open right now -- specific, not round, and not picked to shock.
"""

import os

# Honest count of browser tabs open at the moment of entry.
TAB_COUNT = 137


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
