"""Seventeen Syllables of Debugging — haiku entry for make.fun.

Writes the haiku to /output/entry.txt
"""
import os

HAIKU = """Red breakpoint blinks twice
log lines scroll past midnight rain
bug was a typo"""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")

if __name__ == "__main__":
    main()
