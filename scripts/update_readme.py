#!/usr/bin/env python3
"""Auto-update README.md: repo structure tree, progress table, and progress badge.

Markers in README.md:
  <!-- STRUCTURE:START --> ... <!-- STRUCTURE:END -->
  <!-- PROGRESS:START -->  ... <!-- PROGRESS:END -->

Folder naming:  Day-03-Conditional-Statements  ->  Day 03 | Conditional Statements
Optional first line in any .py:  # Topic: Custom Topic Name
"""
import re
from pathlib import Path

ROOT = (
    Path(__file__).resolve().parent.parent
    if Path(__file__).parent.name == "scripts"
    else Path(__file__).resolve().parent
)
README = ROOT / "README.md"
STRUCTURE_START, STRUCTURE_END = "<!-- STRUCTURE:START -->", "<!-- STRUCTURE:END -->"
PROGRESS_START, PROGRESS_END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
DAY_RE = re.compile(r"^Day[-_ ]?(\d+)[-_ ]*(.*)$", re.IGNORECASE)

KNOWN_DESCRIPTIONS = {
    1: "Variables, data types & type casting",
    2: "Arithmetic, logical & comparison operators",
    3: "If/elif/else decision control",
    4: "For, while loops & loop control statements",
    5: "Functions, arguments, return values & scope",
    6: "Dynamic arrays, list operations & indexing",
    7: "Immutable sequences & tuple unpacking",
    8: "Unique collections & set operations",
    9: "Key-value mapping & hash tables",
    10: "String manipulation, slicing & formatting",
    11: "Robust error management & input validation",
    12: "Persistent file I/O & record storage",
    13: "Custom & built-in modules, namespaces & CLI",
    14: "Classes, objects, constructors & methods",
}

NAME_OVERRIDES = {
    "OOP": "Object-Oriented Programming (OOP)",
    "Oop": "Object-Oriented Programming (OOP)",
    "Modules Packages": "Modules & Packages",
    "Modules And Packages": "Modules & Packages",
}


def topic_for(folder: Path, fallback: str) -> str:
    # 1. Look for "# Topic: ..." or "# topic: ..." in python files
    for py in sorted(folder.rglob("*.py")):
        first = py.read_text(encoding="utf-8", errors="ignore").splitlines()[:1]
        if first and first[0].lower().startswith("# topic:"):
            return first[0].split(":", 1)[1].strip()

    # 2. Check if fallback matches any overrides
    if fallback.upper() in NAME_OVERRIDES:
        return NAME_OVERRIDES[fallback.upper()]
    if fallback in NAME_OVERRIDES:
        return NAME_OVERRIDES[fallback]

    return fallback or "Practice"


def build_structure(day_dirs: list[tuple[int, Path]]) -> str:
    lines = [
        "```text",
        f"{ROOT.name}/",
        "├── .github/".ljust(49) + "# Automated workflows & CI/CD",
        "│   └── workflows/",
        "│       └── update-readme.yml".ljust(49) + "# Automated GitHub Actions tracker workflow",
        "├── assets/".ljust(49) + "# Banners, roadmaps, and visual documentation",
        "│   ├── banner-code-to-creation.png",
        "│   ├── banner-roadmap.jpg",
        "│   └── banner-collection.png",
        "├── scripts/".ljust(49) + "# Automation scripts",
        "│   └── update_readme.py".ljust(49) + "# Automation script to rebuild progress table",
    ]

    for num, d in day_dirs:
        desc = KNOWN_DESCRIPTIONS.get(num, topic_for(d, d.name))
        lines.append(f"├── {d.name}/".ljust(49) + f"# {desc}")

    lines.append("└── README.md".ljust(49) + "# Master repository documentation")
    lines.append("```")
    return "\n".join(lines)


def build_table(day_dirs: list[tuple[int, Path]]) -> str:
    rows = []
    for num, d in day_dirs:
        raw_name = DAY_RE.match(d.name).group(2).replace("-", " ").replace("_", " ").strip()
        fallback_name = NAME_OVERRIDES.get(raw_name.upper(), raw_name.title())
        topic = topic_for(d, fallback_name)
        files = len(list(d.rglob("*.py")))
        rows.append(f"| {num:02d} | [{topic}]({d.name}/) | {files} | ✅ |")

    header = "| Day | Topic | Programs | Status |\n|:---:|:---|:---:|:---:|"
    total = f"\n\n**Total days completed: {len(day_dirs)}**"
    return header + "\n" + "\n".join(rows) + total


def update_badge(text: str, max_day: int) -> str:
    return re.sub(
        r"(https://img\.shields\.io/badge/Progress-Day%20)\d+(%20Active-brightgreen)",
        rf"\g<1>{max_day}\g<2>",
        text,
    )


def patch_section(text: str, start_marker: str, end_marker: str, content: str) -> str:
    block = f"{start_marker}\n{content}\n{end_marker}"
    if start_marker in text and end_marker in text:
        return re.sub(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            lambda _: block,
            text,
            flags=re.S,
        )
    return text


def main() -> None:
    text = README.read_text(encoding="utf-8")

    day_dirs = []
    for d in ROOT.iterdir():
        if d.is_dir():
            m = DAY_RE.match(d.name)
            if m:
                day_dirs.append((int(m.group(1)), d))
    day_dirs.sort()

    max_day = day_dirs[-1][0] if day_dirs else 0

    # 1. Update structure tree
    structure_content = build_structure(day_dirs)
    text = patch_section(text, STRUCTURE_START, STRUCTURE_END, structure_content)

    # 2. Update progress table
    progress_content = build_table(day_dirs)
    text = patch_section(text, PROGRESS_START, PROGRESS_END, progress_content)

    # 3. Update active badge
    if max_day > 0:
        text = update_badge(text, max_day)

    README.write_text(text, encoding="utf-8")
    print(f"Successfully updated README.md for {len(day_dirs)} days (Max Day: {max_day}).")


if __name__ == "__main__":
    main()
