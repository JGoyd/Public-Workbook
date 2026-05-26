#!/usr/bin/env python3
"""Rebuild workbook index files from workbook/outputs entries."""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from dataclasses import dataclass
from datetime import date as date_type
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_REL = Path("workbook") / "outputs"


@dataclass(frozen=True)
class Entry:
    date: str
    day: str
    slug: str
    title: str
    headline: str
    rel_path: str
    artifacts: str


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return {}, text

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw in lines[1:end]:
        line = raw.rstrip()
        if not line:
            continue
        if current_list_key and line.lstrip().startswith("- "):
            value = line.lstrip()[2:].strip()
            existing = data.setdefault(current_list_key, [])
            if isinstance(existing, list):
                existing.append(value)
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "[]":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [item.strip() for item in inner.split(",") if item.strip()] if inner else []
        elif value == "":
            data[key] = []
            current_list_key = key
        else:
            data[key] = value

    return data, "\n".join(lines[end + 1 :])


def strip_date_from_title(title: str) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}\s*(?:[-:|]|\u00b7|\u2013|\u2014)\s*", "", title).strip()


def fallback_title(slug: str, body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return strip_date_from_title(line[2:].strip()) or slug.replace("-", " ").title()
    return slug.replace("-", " ").title()


def fallback_headline(body: str) -> str:
    lines = body.splitlines()
    for line in lines:
        if line.lower().startswith("headline:"):
            return line.split(":", 1)[1].strip()

    seen_h1 = False
    para: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            if para:
                break
            continue
        if line.startswith("# "):
            seen_h1 = True
            continue
        if not seen_h1:
            continue
        if line.startswith("#") or line == "---" or line.startswith("|"):
            if para:
                break
            continue
        if re.match(r"^(Day|Topic|Status):", line):
            continue
        para.append(line)
        if len(" ".join(para)) > 140:
            break
    headline = " ".join(para).strip()
    return headline[:180].rstrip()


def artifact_summary(entry_dir: Path) -> str:
    labels: list[str] = []
    checks = [
        ("reports", "reports"),
        ("raw", "raw lists"),
        ("json", "JSON"),
        ("screenshots", "screenshots"),
        ("exports", "HTML exports"),
    ]
    for dirname, label in checks:
        path = entry_dir / dirname
        if path.exists() and any(p.is_file() for p in path.rglob("*")):
            labels.append(label)
    tables = entry_dir / "tables"
    if tables.exists():
        table_files = [p for p in tables.rglob("*") if p.is_file()]
        if table_files:
            labels.insert(1 if labels and labels[0] == "reports" else 0, "IOC tables" if any("ioc" in p.name.lower() for p in table_files) else "tables")
    other = entry_dir / "other"
    other_files = [p for p in other.rglob("*") if p.is_file()] if other.exists() else []
    if any(p.suffix.lower() in {".asc", ".sig", ".sha256", ".sha512"} for p in other_files):
        labels.append("verification files")
    if any(p.suffix.lower() in {".yar", ".yara"} for p in other_files):
        labels.append("YARA")
    elif other_files and not any(p.suffix.lower() in {".asc", ".sig", ".sha256", ".sha512"} for p in other_files):
        labels.append("other")
    return ", ".join(labels) if labels else "entry README"


def find_entries(root: Path) -> list[Entry]:
    outputs = root / OUTPUTS_REL
    rows: list[Entry] = []
    for readme in sorted(outputs.glob("*/*/*/*/README.md")):
        parts = readme.relative_to(outputs).parts
        if len(parts) < 5:
            continue
        year, month, day, slug = parts[:4]
        entry_date = f"{year}-{month}-{day}"
        try:
            weekday = datetime.strptime(entry_date, "%Y-%m-%d").strftime("%a")
        except ValueError:
            continue

        text = readme.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)
        title = str(frontmatter.get("title") or fallback_title(slug, body)).strip()
        headline = str(frontmatter.get("headline") or fallback_headline(body)).strip()
        rel_path = readme.relative_to(root).as_posix()
        rows.append(
            Entry(
                date=str(frontmatter.get("date") or entry_date),
                day=weekday,
                slug=str(frontmatter.get("slug") or slug),
                title=title,
                headline=headline,
                rel_path=rel_path,
                artifacts=artifact_summary(readme.parent),
            )
        )

    rows.sort(key=lambda r: r.title.lower())
    rows.sort(key=lambda r: r.date, reverse=True)
    return rows


def daily_table(entries: list[Entry]) -> str:
    out = ["| Date | Day | Topic | Headline | Open |", "| --- | --- | --- | --- | --- |"]
    for entry in entries:
        out.append(f"| {entry.date} | {entry.day} | {entry.title} | {entry.headline} | [open]({entry.rel_path}) |")
    return "\n".join(out)


def topic_rollup(entries: list[Entry]) -> list[dict[str, object]]:
    topics: dict[str, dict[str, object]] = {}
    for entry in entries:
        topic = topics.setdefault(
            entry.slug,
            {
                "slug": entry.slug,
                "title": entry.title,
                "count": 0,
                "latest": entry.date,
            },
        )
        topic["count"] = int(topic["count"]) + 1
        if entry.date > str(topic["latest"]):
            topic["latest"] = entry.date
            topic["title"] = entry.title
    return sorted(topics.values(), key=lambda t: str(t["title"]).lower())


def topic_table(entries: list[Entry]) -> str:
    out = ["| Topic | Entries | Most recent | Jump in |", "| --- | ---: | --- | --- |"]
    for topic in topic_rollup(entries):
        slug = str(topic["slug"])
        out.append(
            f"| {topic['title']} | {topic['count']} | {topic['latest']} | "
            f"[topic page](workbook/topics/{slug}.md) |"
        )
    return "\n".join(out)


def replace_block(text: str, marker: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {re.escape(marker)}:start -->)(.*?)(<!-- {re.escape(marker)}:end -->)", re.DOTALL)
    new_text, count = pattern.subn(rf"\1\n{body}\n\3", text)
    if count != 1:
        raise ValueError(f"README.md needs exactly one {marker} marker block")
    return new_text


def update_readme(text: str, entries: list[Entry], today: str) -> str:
    text = re.sub(r"_Last updated:.*?_", f"_Last updated: {today}_", text)
    text = replace_block(text, "daily-log", daily_table(entries))
    text = replace_block(text, "topic-index", topic_table(entries))
    return text


def master_output_index_md(entries: list[Entry]) -> str:
    out = ["# Master Output Index", "", "| Date | Topic | Entry | Main artifacts |", "| --- | --- | --- | --- |"]
    for entry in entries:
        rel = (Path("..") / Path(entry.rel_path).relative_to("workbook")).as_posix()
        out.append(f"| {entry.date} | {entry.title} | [open]({rel}) | {entry.artifacts} |")
    return "\n".join(out) + "\n"


def topic_output_index_md(entries: list[Entry]) -> str:
    out = ["# Topic Output Index", "", "| Topic | Entries | Most recent | Topic page |", "| --- | ---: | --- | --- |"]
    for topic in topic_rollup(entries):
        out.append(
            f"| {topic['title']} | {topic['count']} | {topic['latest']} | "
            f"[open](../topics/{topic['slug']}.md) |"
        )
    return "\n".join(out) + "\n"


def topic_index_md(entries: list[Entry]) -> str:
    out = ["# All Topics", "", "| Topic | Entries | Most recent | Open |", "| --- | ---: | --- | --- |"]
    for topic in topic_rollup(entries):
        out.append(f"| {topic['title']} | {topic['count']} | {topic['latest']} | [open]({topic['slug']}.md) |")
    return "\n".join(out) + "\n"


def csv_text(headers: list[str], rows: list[list[object]]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return buf.getvalue()


def generated_files(root: Path, entries: list[Entry], today: str) -> dict[Path, str]:
    readme_path = root / "README.md"
    readme = update_readme(readme_path.read_text(encoding="utf-8"), entries, today)
    topics = topic_rollup(entries)

    return {
        readme_path: readme,
        root / "workbook" / "indexes" / "master_output_index.md": master_output_index_md(entries),
        root / "workbook" / "indexes" / "master_output_index.csv": csv_text(
            ["date", "topic_slug", "topic", "entry_path", "main_artifacts"],
            [[entry.date, entry.slug, entry.title, entry.rel_path, entry.artifacts] for entry in entries],
        ),
        root / "workbook" / "indexes" / "topic_output_index.md": topic_output_index_md(entries),
        root / "workbook" / "indexes" / "topic_output_index.csv": csv_text(
            ["topic_slug", "topic", "entries", "most_recent", "topic_page"],
            [
                [
                    topic["slug"],
                    topic["title"],
                    topic["count"],
                    topic["latest"],
                    f"workbook/topics/{topic['slug']}.md",
                ]
                for topic in topics
            ],
        ),
        root / "workbook" / "topics" / "_topic_index.md": topic_index_md(entries),
        root / "workbook" / "topics" / "_topic_index.csv": csv_text(
            ["topic_slug", "topic_name", "entries", "most_recent", "topic_page"],
            [
                [
                    topic["slug"],
                    topic["title"],
                    topic["count"],
                    topic["latest"],
                    f"workbook/topics/{topic['slug']}.md",
                ]
                for topic in topics
            ],
        ),
    }


def rebuild(root: Path = ROOT, today: str | None = None, check: bool = False) -> bool:
    today = today or date_type.today().isoformat()
    entries = find_entries(root)
    files = generated_files(root, entries, today)
    changed = False
    for path, content in files.items():
        old = path.read_text(encoding="utf-8") if path.exists() else ""
        if old != content:
            changed = True
            if check:
                print(f"would update {path.relative_to(root).as_posix()}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Rebuild workbook indexes")
    parser.add_argument("--check", action="store_true", help="fail if generated indexes are stale")
    parser.add_argument("--date", help="override Last updated date, YYYY-MM-DD")
    args = parser.parse_args(argv)

    changed = rebuild(ROOT, today=args.date, check=args.check)
    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
