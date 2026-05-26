# Public Workbook

A running work timeline, organized by the date the work was done, submitted, or finalized.
Each entry keeps the findings, source context, tables, and related artifacts in one place.
GitHub publish dates are housekeeping; they do not control the order here.

_Last updated: 2026-05-26_

---

## Where to Start

- [Work timeline](#work-timeline)
- [Current threads](#current-threads)
- [Master index](workbook/indexes/master_output_index.md)
- [Topic index](workbook/topics/_topic_index.md)

---

## Work Timeline

This table follows the work/submission date. The `Covers` column shows the real-world event date or source window when that differs from the work date.

<!-- work-timeline:start -->
| Work Date | Day | Topic | Type | Covers | What changed | Open |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-26 | Tue | Zorro Ranch | packet | 2026-05-26 NM presence inquiry packet | Official NM presence inquiry packet, HTML version, detached signature, checksum, and public key | [open](workbook/outputs/2026/05/26/zorro-ranch/README.md) |
| 2026-05-25 | Mon | RemoteRAT / RATtrap | public writeup | 2026-05-25 source EML and public repo artifacts | Public campaign write-up, source EML, header export, IOC tables, YARA rule, and Pages export | [open](workbook/outputs/2026/05/25/remoterat-rattrap/README.md) |
| 2026-05-25 | Mon | Thiel Reveal | research note | 2012-03 to 2017-12 source-document context | 2014 scheduling, Valar intro, later logistics, earlier attendee context | [open](workbook/outputs/2026/05/25/thiel-reveal/README.md) |
| 2026-05-25 | Mon | Zorro Ranch | research note | 2009 to 2015 source-document context | Guest access, staff logistics, property operations, aviation, registration context | [open](workbook/outputs/2026/05/25/zorro-ranch/README.md) |
| 2026-05-24 | Sun | U-Haul Evidence Transfer | manual transcription | 2025-02-27 to 2025-03-25 records-handling sequence | WFO-to-IMD transfer sequence, ERT photo logs, item-level transcription, and release-processing context | [open](workbook/outputs/2026/05/24/uhaul-evidence-transfer/README.md) |
| 2026-05-13 | Wed | SEC Ito Referral | supplement | 2026-05-13 supplement and 2026-05-14 receipt | Supplement 01, OMMS update PDF, receipt EML, and hashes for submission 17780-976-067-126 | [open](workbook/outputs/2026/05/13/sec-ito-referral/README.md) |
| 2026-05-06 | Wed | SEC Ito Referral | submission | 2026-05-06 SEC TCR submission | Initial SEC TCR evidence packet for submission 17780-976-067-126 | [open](workbook/outputs/2026/05/06/sec-ito-referral/README.md) |
<!-- work-timeline:end -->

---

## Current Threads

<!-- topic-index:start -->
| Topic | Entries | Latest work | Jump in |
| --- | ---: | --- | --- |
| RemoteRAT / RATtrap | 1 | 2026-05-25 | [topic page](workbook/topics/remoterat-rattrap.md) |
| SEC Ito Referral | 2 | 2026-05-13 | [topic page](workbook/topics/sec-ito-referral.md) |
| Thiel Reveal | 1 | 2026-05-25 | [topic page](workbook/topics/thiel-reveal.md) |
| U-Haul Evidence Transfer | 1 | 2026-05-24 | [topic page](workbook/topics/uhaul-evidence-transfer.md) |
| Zorro Ranch | 2 | 2026-05-26 | [topic page](workbook/topics/zorro-ranch.md) |
<!-- topic-index:end -->

---

## Date Rules

- Work Date: when the work was done, submitted, finalized, or packaged.
- Covers: the event date or source-document window covered by the entry.
- GitHub publish dates do not reorder the workbook.
- Session IDs are lookup pointers only; they are not workbook entries.

---

## Entry Format

Each entry is meant to be easy to browse:

1. Snapshot - the short case card.
2. Findings by lane - grouped context, not one long block of text.
3. Artifact map - what files were added and where they live.
4. Tables and detection material - CSVs, rules, exports, and raw source files.
5. Links out - public repo, rendered page, or related entries when present.

This repository is the workbook. Daily entries and topic pages are the main paths through it.

---

## Repo Map

```text
workbook/
|-- outputs/YYYY/MM/DD/<topic>/   daily entries
|-- topics/                       per-topic rollups
|-- indexes/                      master + topic indexes
|-- daily/                        daily notes
|-- _meta/                        build notes and operational files
`-- templates/                    entry templates
```

---

_Updated as new entries are added._
