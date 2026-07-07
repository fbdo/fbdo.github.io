#!/usr/bin/env python3
"""Readability scorer for Hugo Markdown posts.

Strips the parts of a Markdown file that would skew readability metrics
(TOML front matter, fenced code, tables, images, citation markers, link
URLs, and the References section), then reports common readability scores
with best-practice targets.

Usage:
    python readability.py content/posts/my-post.md [more.md ...]
"""

import argparse
import re
import sys

import textstat


def extract_prose(md: str) -> str:
    """Reduce a Markdown document to plain prose for scoring."""
    # Drop TOML/YAML front matter delimited by +++ or --- at the top.
    md = re.sub(r"\A\s*(\+\+\+|---)\s*\n.*?\n(\+\+\+|---)\s*\n", "", md, flags=re.DOTALL)

    # Drop everything from the References heading onward.
    md = re.split(r"(?im)^\s*#{1,6}\s+references\s*$", md)[0]

    # Remove fenced code blocks.
    md = re.sub(r"```.*?```", " ", md, flags=re.DOTALL)

    # Remove HTML comments and raw tags.
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.DOTALL)
    md = re.sub(r"<[^>]+>", " ", md)

    # Remove images: ![alt](url)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", md)

    # Remove citation-style links such as [\[S19\]](url) -> nothing.
    md = re.sub(r"\[\\?\[[^\]]*\\?\]\]\([^)]*\)", " ", md)

    # Collapse remaining links [text](url) -> text
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)

    lines = []
    for line in md.splitlines():
        stripped = line.strip()
        # Drop table rows and separators.
        if stripped.startswith("|"):
            continue
        # Drop horizontal rules.
        if re.fullmatch(r"[-*_]{3,}", stripped):
            continue
        # Drop heading lines (no terminal punctuation -> corrupts sentence counts).
        if stripped.startswith("#"):
            continue
        # Strip blockquote and list markers, keep the text.
        stripped = re.sub(r"^>\s?", "", stripped)
        stripped = re.sub(r"^([-*+]|\d+\.)\s+", "", stripped)
        lines.append(stripped)

    text = "\n".join(lines)

    # Strip inline emphasis / code markers.
    text = text.replace("`", "")
    text = re.sub(r"\*\*|__|\*|_", "", text)

    # Normalise whitespace.
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


# (metric label, textstat fn, target text, pass predicate)
METRICS = [
    (
        "Flesch Reading Ease",
        lambda t: textstat.flesch_reading_ease(t),
        "50-70 (higher = easier; 60-70 = plain English)",
        lambda v: v >= 50,
    ),
    (
        "Flesch-Kincaid Grade",
        lambda t: textstat.flesch_kincaid_grade(t),
        "8-12 (US school grade)",
        lambda v: v <= 12,
    ),
    (
        "Gunning Fog",
        lambda t: textstat.gunning_fog(t),
        "<= 12 ideal, <= 14 for professional",
        lambda v: v <= 14,
    ),
    (
        "SMOG Index",
        lambda t: textstat.smog_index(t),
        "10-12",
        lambda v: v <= 12,
    ),
    (
        "Coleman-Liau Index",
        lambda t: textstat.coleman_liau_index(t),
        "8-12 (grade)",
        lambda v: v <= 12,
    ),
    (
        "Automated Readability Index",
        lambda t: textstat.automated_readability_index(t),
        "8-12 (grade)",
        lambda v: v <= 12,
    ),
    (
        "Dale-Chall",
        lambda t: textstat.dale_chall_readability_score(t),
        "< 8 (8-9 = college level)",
        lambda v: v < 8.0,
    ),
]


def score_file(path: str) -> bool:
    try:
        with open(path, encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as err:
        print(f"! Could not read {path}: {err}", file=sys.stderr)
        return False

    prose = extract_prose(raw)
    words = textstat.lexicon_count(prose, removepunct=True)
    sentences = textstat.sentence_count(prose)

    print(f"\n=== {path} ===")
    print(f"Words (prose only): {words}    Sentences: {sentences}")
    if words < 100:
        print("  (warning: very little prose extracted; scores may be unreliable)")
    print(f"{'Metric':<30}{'Score':>9}   {'Target':<40}{'Flag'}")
    print("-" * 92)

    for label, fn, target, ok in METRICS:
        value = fn(prose)
        flag = "ok" if ok(value) else "review"
        print(f"{label:<30}{value:>9.1f}   {target:<40}{flag}")

    print(f"\nConsensus grade (text_standard): {textstat.text_standard(prose)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Score Markdown readability.")
    parser.add_argument("files", nargs="+", help="Markdown files to score")
    args = parser.parse_args()

    ok = True
    for path in args.files:
        ok = score_file(path) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
