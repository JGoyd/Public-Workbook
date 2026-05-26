# Public Workbook

A daily record of current work, organized by date and topic.
Each entry keeps the findings, source context, tables, and related artifacts in one place.

_Last updated: 2026-05-26_

---

## Where to Start

- [Today / Latest entries](#today--latest)
- [Daily log](#daily-log)
- [By topic](#by-topic)
- [Master index](workbook/indexes/master_output_index.md)

---

## Today / Latest

### 2026-05-26 - Tue - One entry

**Zorro Ranch** - Official New Mexico presence inquiry packet with the HTML version, detached signature, SHA-256 checksum, and public key for verification.
[Read full entry](workbook/outputs/2026/05/26/zorro-ranch/README.md)

---

## Daily Log

<!-- daily-log:start -->
| Date | Day | Topic | Headline | Open |
| --- | --- | --- | --- | --- |
| 2026-05-26 | Tue | Zorro Ranch | Official NM presence inquiry packet, HTML version, detached signature, checksum, and public key | [open](workbook/outputs/2026/05/26/zorro-ranch/README.md) |
| 2026-05-25 | Mon | RemoteRAT / RATtrap | Public campaign write-up, source EML, header export, IOC tables, YARA rule, and Pages export | [open](workbook/outputs/2026/05/25/remoterat-rattrap/README.md) |
| 2026-05-25 | Mon | Thiel Reveal | 2014 scheduling, Valar intro, later logistics, earlier attendee context | [open](workbook/outputs/2026/05/25/thiel-reveal/README.md) |
| 2026-05-25 | Mon | Zorro Ranch | Guest access, staff logistics, property operations, aviation, registration context | [open](workbook/outputs/2026/05/25/zorro-ranch/README.md) |
<!-- daily-log:end -->

_New rows land at the top each day._

---

## By Topic

<!-- topic-index:start -->
| Topic | Entries | Most recent | Jump in |
| --- | ---: | --- | --- |
| RemoteRAT / RATtrap | 1 | 2026-05-25 | [topic page](workbook/topics/remoterat-rattrap.md) |
| Thiel Reveal | 1 | 2026-05-25 | [topic page](workbook/topics/thiel-reveal.md) |
| Zorro Ranch | 2 | 2026-05-26 | [topic page](workbook/topics/zorro-ranch.md) |
<!-- topic-index:end -->

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
