#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You -- make.fun entry (Account A).

One sentence of apology for a real failure, built phrase by phrase:
the sorry, the urgent question, expert confidence, horoscope accuracy.
Stdlib only; run: python3 main.py
"""
import os

PHRASES = (
    "I'm sorry I answered",
    "your urgent question",
    "with the confidence of an expert",
    "and the accuracy of a horoscope.",
)


def compose():
    line = ""
    for phrase in PHRASES:
        line = f"{line} {phrase}" if line else phrase
    return line


def validate(line):
    checks = [
        (bool(line.strip()), "entry is empty"),
        (1 <= len(line) <= 200, "entry length outside 1..200"),
        ("\n" not in line and "\r" not in line, "entry must be one line"),
    ]
    failed = [msg for ok, msg in checks if not ok]
    if failed:
        raise ValueError("; ".join(failed))
    line.encode("utf-8")
    return line


def main():
    line = validate(compose())
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(base, exist_ok=True)
    target = os.path.join(base, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as out:
        out.write(line)
    print(f"Wrote {len(line)} characters to {target}")


if __name__ == "__main__":
    main()
