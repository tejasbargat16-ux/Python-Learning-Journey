#!/usr/bin/env python3
"""Regenerate the progress table in README.md from Day-XX folders.

Folder naming:  Day-03_Conditionals  ->  Day 03 | Conditionals
Optional: put a first-line comment in any .py file:  # Topic: If/Else practice
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent if Path(__file__).parent.name == "scripts" else Path(__file__).resolve().parent
README = ROOT / "README.md"
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
DAY_RE = re.compile(r"^Day[-_ ]?(\d+)[-_ ]*(.*)$", re.IGNORECASE)


def topic_for(folder: Path, fallback: str) -> str:
    for py in sorted(folder.rglob("*.py")):
        first = py.read_text(encoding="utf-8", errors="ignore").splitlines()[:1]
        if first and first[0].lower().startswith("# topic:"):
            return first[0].split(":", 1)[1].strip()
    return fallback or "Practice"


def build_table() -> str:
    rows = []
    for d in ROOT.iterdir():
        m = DAY_RE.match(d.name)
        if d.is_dir() and m:
            num = int(m.group(1))
            name = m.group(2).replace("-", " ").replace("_", " ").strip().title()
            files = len(list(d.rglob("*.py")))
            rows.append((num, f"| {num:02d} | [{topic_for(d, name)}]({d.name}/) | {files} | ✅ |"))
    rows.sort()
    header = "| Day | Topic | Programs | Status |\n|:---:|:---|:---:|:---:|"
    total = f"\n\n**Total days completed: {len(rows)}**"
    return header + "\n" + "\n".join(r for _, r in rows) + total


def main() -> None:
    text = README.read_text(encoding="utf-8")
    block = f"{START}\n{build_table()}\n{END}"
    if START in text and END in text:
        text = re.sub(f"{START}.*?{END}", block, text, flags=re.S)
    else:
        text += f"\n\n## 📈 Progress Tracker\n\n{block}\n"
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
