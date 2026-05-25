---
name: raw-output-workbook
description: Use when the user asks to update, add to, throw a report into, or maintain the Public Workbook / Cyber Range Research Output Workbook with neutral dated raw outputs by topic.
---

# Raw Output Workbook

## Purpose

Maintain a local ongoing research-output workbook. The workbook stores raw work products by date, topic, and output type using plain Markdown and CSV.

Do not create claims, disclosure language, legal conclusions, confidence scores, methodology explanations, or evidence arguments.

## Target Structure

Use the repo-local `workbook/` directory:

- `workbook/outputs/YYYY/MM/DD/TOPIC-SLUG/`
- `workbook/daily/YYYY-MM-DD.md`
- `workbook/topics/_topic_index.md`
- `workbook/topics/_topic_index.csv`
- `workbook/indexes/master_output_index.csv`
- `workbook/indexes/master_output_index.md`
- `workbook/indexes/topic_output_index.csv`
- `workbook/indexes/topic_output_index.md`
- `workbook/public_view/latest_outputs.md`
- `workbook/private_holdback/`

Each topic-day folder should contain:

- `README.md`
- `output_manifest.csv`
- `output_manifest.md`
- `raw/`
- `reports/`
- `tables/`
- `json/`
- `screenshots/`
- `exports/`
- `other/`

## Workflow

1. Inspect the current project folder and identify new work product. Exclude `.git/`, `workbook/private_holdback/`, dependency caches, build outputs, and editor metadata.
2. Classify each file only as one of: `report`, `table`, `transcript`, `json`, `markdown`, `screenshot`, `source export`, `scan output`, `notes`, `other`.
3. Before copying or indexing, screen for credentials, tokens, API keys, private prompts, hidden source paths, or operationally sensitive material.
4. If a file is public-range safe, copy it under `workbook/outputs/YYYY/MM/DD/TOPIC-SLUG/` in the matching type folder. Do not delete originals.
5. If a file is sensitive, move or copy it to `workbook/private_holdback/` and replace the public entry with `Held back: sensitive/internal material.`
6. If a destination filename already exists, append a timestamp before the extension.
7. Update the topic README, local output manifests, daily log, topic indexes, master indexes, and `workbook/public_view/latest_outputs.md`.
8. Keep descriptions short and neutral. Do not summarize beyond a label.

## Required Return Format

Return only:

- outputs added
- indexes updated
- files held back
- workbook path

