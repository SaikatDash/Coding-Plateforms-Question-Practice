"""Generate the repository progress dashboard from tracked solution files."""

from __future__ import annotations

import subprocess
from collections import Counter
from datetime import date, datetime
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets"
SOURCE_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".go",
    ".java",
    ".js",
    ".py",
    ".rs",
    ".ts",
}
IGNORED_DIRECTORIES = {"__pycache__"}


def git(*arguments: str) -> str:
    result = subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def tracked_solutions() -> list[Path]:
    files = git("ls-files").splitlines()
    return [
        Path(path)
        for path in files
        if Path(path).suffix.lower() in SOURCE_EXTENSIONS
        and not any(part in IGNORED_DIRECTORIES for part in Path(path).parts)
    ]


def added_date(path: Path) -> date:
    output = git(
        "log",
        "--diff-filter=A",
        "--follow",
        "--format=%ad",
        "--date=short",
        "--",
        str(path),
    )
    if output:
        return datetime.strptime(output.splitlines()[-1], "%Y-%m-%d").date()

    output = git("log", "-1", "--format=%ad", "--date=short", "--", str(path))
    return datetime.strptime(output, "%Y-%m-%d").date()


def title(value: str) -> str:
    return value.replace("-", " ").replace("_", " ").title()


def solution_records() -> list[tuple[Path, date]]:
    return [(path, added_date(path)) for path in tracked_solutions()]


def markdown_table(rows: list[tuple[str, int]], headers: tuple[str, str]) -> str:
    lines = [f"| {headers[0]} | {headers[1]} |", "| --- | ---: |"]
    lines.extend(f"| {name} | {count} |" for name, count in rows)
    return "\n".join(lines)


def write_svg_charts(monthly: dict[str, int], skills: Counter[str]) -> None:
    ASSETS.mkdir(exist_ok=True)
    max_month = max(max(monthly.values(), default=1), 1)
    month_bars = []
    for index, (month, count) in enumerate(monthly.items()):
        x = 90 + index * 125
        height = 220 * count / max_month if count else 0
        y = 280 - height
        month_bars.append(
            f'<rect x="{x}" y="{y:.1f}" width="70" height="{height:.1f}" '
            f'rx="6" fill="#58a6ff"/><text x="{x + 35}" y="310" '
            f'text-anchor="middle" fill="#8b949e" font-size="13">{escape(month)}</text>'
            f'<text x="{x + 35}" y="{y - 8:.1f}" text-anchor="middle" '
            f'fill="#f0f6fc" font-size="14">{count}</text>'
        )
    (ASSETS / "progress-by-month.svg").write_text(
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 350">
<rect width="900" height="350" rx="14" fill="#0d1117"/>
<text x="30" y="38" fill="#f0f6fc" font-size="22" font-family="Arial">Questions solved by month</text>
<line x1="70" y1="280" x2="850" y2="280" stroke="#30363d"/>
{''.join(month_bars)}
</svg>
""",
        encoding="utf-8",
    )

    top_skills = skills.most_common()
    max_skill = max((count for _, count in top_skills), default=1)
    skill_rows = []
    for index, (skill, count) in enumerate(top_skills):
        y = 55 + index * 32
        width = 430 * count / max_skill
        skill_rows.append(
            f'<text x="20" y="{y + 16}" fill="#f0f6fc" font-size="14" '
            f'font-family="Arial">{escape(skill)}</text>'
            f'<rect x="190" y="{y}" width="{width:.1f}" height="22" rx="5" fill="#3fb950"/>'
            f'<text x="{200 + width:.1f}" y="{y + 16}" fill="#f0f6fc" '
            f'font-size="14">{count}</text>'
        )
    skill_height = max(120, 75 + len(top_skills) * 32)
    (ASSETS / "skills.svg").write_text(
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 {skill_height}">
<rect width="700" height="{skill_height}" rx="14" fill="#0d1117"/>
<text x="20" y="35" fill="#f0f6fc" font-size="22" font-family="Arial">Skills and topics practiced</text>
{''.join(skill_rows)}
</svg>
""",
        encoding="utf-8",
    )


def build_readme(records: list[tuple[Path, date]], today: date) -> str:
    total = len(records)
    today_count = sum(solved_on == today for _, solved_on in records)
    month_count = sum(
        solved_on.year == today.year and solved_on.month == today.month
        for _, solved_on in records
    )

    platforms = Counter(path.parts[0].replace("-", " ").title() for path, _ in records)
    skills = Counter(
        title(path.parts[1]) if len(path.parts) > 2 else title(path.stem)
        for path, _ in records
    )
    monthly = {
        month.strftime("%Y-%m"): sum(
            solved_on.year == month.year and solved_on.month == month.month
            for _, solved_on in records
        )
        for month in (
            date(today.year, today.month, 1),
            date(today.year - (today.month == 1), today.month - 1 or 12, 1),
            date(today.year - (today.month <= 2), (today.month - 2) % 12 or 12, 1),
            date(today.year - (today.month <= 3), (today.month - 3) % 12 or 12, 1),
            date(today.year - (today.month <= 4), (today.month - 4) % 12 or 12, 1),
            date(today.year - (today.month <= 5), (today.month - 5) % 12 or 12, 1),
        )
    }

    platform_rows = sorted(platforms.items(), key=lambda item: (-item[1], item[0]))
    skill_rows = sorted(skills.items(), key=lambda item: (-item[1], item[0]))
    recent = sorted(records, key=lambda item: (item[1], str(item[0])), reverse=True)[:10]
    recent_rows = "\n".join(
        f"| `{path.stem}` | {title(path.parts[0])} | {title(path.parts[1])} | {solved_on} |"
        for path, solved_on in recent
    )
    write_svg_charts(monthly, skills)
    busiest_day = Counter(solved_on for _, solved_on in records).most_common(1)
    top_skill, top_skill_count = skill_rows[0] if skill_rows else ("None", 0)
    top_platform, top_platform_count = platform_rows[0] if platform_rows else ("None", 0)
    if busiest_day:
        analysis = (
            f"- **Coverage:** {total} questions across {len(platforms)} platforms/tracks, "
            f"with {top_platform} contributing the most ({top_platform_count}).\n"
            f"- **Strongest topic:** {top_skill} is currently the most practiced category "
            f"with {top_skill_count} solved questions.\n"
            f"- **Current momentum:** {today_count} solved today and {month_count} solved "
            f"this month ({today:%B %Y}).\n"
            f"- **Best solving day:** {busiest_day[0][0]} was the most productive day "
            f"with {busiest_day[0][1]} question(s)."
        )
    else:
        analysis = "- **Analysis:** No solved questions have been recorded yet."

    return f"""# Competitive Programming Progress

> A living dashboard of my data structures, algorithms, and problem-solving practice.

![Python](https://img.shields.io/badge/Python-solutions-3776AB?logo=python&logoColor=white)
![Problems solved](https://img.shields.io/badge/Problems%20solved-{total}-brightgreen)
![Updated](https://img.shields.io/badge/Updated-{today}-blue)

## At a glance

| Metric | Count |
| --- | ---: |
| **Total solved** | **{total}** |
| **Solved today ({today})** | **{today_count}** |
| **Solved this month ({today:%B %Y})** | **{month_count}** |
| **Platforms / tracks** | **{len(platforms)}** |
| **Skills / categories** | **{len(skills)}** |

## Skills practiced

{markdown_table(skill_rows, ("Skill / category", "Solved"))}

![Skills and topics practiced](./assets/skills.svg)

## Platform progress

{markdown_table(platform_rows, ("Platform", "Solved"))}

## Monthly trend

![Questions solved by month](./assets/progress-by-month.svg)

## Analysis report

{analysis}

## Latest solved questions

| Question | Platform | Skill / category | Solved on |
| --- | --- | --- | --- |
{recent_rows}

## Repository layout

- [`leetcode/`](./leetcode) — LeetCode solutions organized by algorithm/topic.
- [`geeksforgeeks/`](./geeksforgeeks) — GeeksforGeeks solutions organized by difficulty.
- [`scripts/generate_readme.py`](./scripts/generate_readme.py) — regenerates this dashboard from Git history.
- [`assets/`](./assets) — generated SVG charts embedded above.

<sub>Generated automatically from tracked solution files and their first-added Git commit. Last updated: {today}.</sub>
"""


def main() -> None:
    today = date.today()
    README.write_text(build_readme(solution_records(), today), encoding="utf-8")
    print(f"Generated {README} for {today}.")


if __name__ == "__main__":
    main()
