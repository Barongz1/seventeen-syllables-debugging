"""Seventeen Syllables of Debugging — haiku entry for make.fun.

Writes the haiku to /output/entry.txt.
The haiku is 5-7-5 syllables, three lines, at most 200 characters.
"""
import os

HAIKU = """Red breakpoint blinks twice
log lines scroll past midnight rain
bug was a typo"""

def main():
    lines = HAIKU.splitlines()
    assert len(lines) == 3, "haiku must have three lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")

if __name__ == "__main__":
    main()
