# Public Workbook

A running work timeline, organized by the date the work was done, submitted, or finalized.
Each entry keeps the findings, source context, tables, and related artifacts in one place.
GitHub publish dates are housekeeping; they do not control the order here.

_Last updated: 2026-05-27_

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
| 2026-05-27 | Wed | Buenos Aires Bond | public writeup | 2018-04 to 2018-05 Southern Financial LLC / Deutsche Bank Buenos Aires bond public-record context | Buenos Aires Bond public HTML report with detached signature, checksum, and public key | [open](https://jgoyd.github.io/Public-Workbook/buenos-aires-bond/) |
| 2026-05-27 | Wed | FCA London Banking Conduct | public writeup | 2026-05-08 to 2026-05-13 FCA Bank of China (UK) Limited / Standard Chartered correspondence sequence | FCA London Banking Conduct public HTML report, supporting packet README, unique EML anchors, checksums, and signatures | [open](https://jgoyd.github.io/Public-Workbook/fca-bank-of-china-stanchart/) |
| 2026-05-26 | Tue | Valar / Southern Trust | source hardening | 2016-01 to 2019-09 Valar Global Fund III / Southern Trust source-document context | Valar / Southern Trust financial lane, source-PDF hardening, rendered page checks, and India-threshold framing | [open](https://jgoyd.github.io/Public-Workbook/valar-southern-trust/) |
| 2026-05-26 | Tue | Zorro Ranch | packet | 2026-05-26 NM presence inquiry packet | Official NM presence inquiry packet, HTML version, detached signature, checksum, and public key | [open](workbook/outputs/2026/05/26/zorro-ranch/README.md) |
| 2026-05-25 | Mon | RemoteRAT / RATtrap | public writeup | 2026-05-25 source EML and public repo artifacts | Public campaign write-up, source EML, header export, IOC tables, YARA rule, and Pages export | [open](workbook/outputs/2026/05/25/remoterat-rattrap/README.md) |
| 2026-05-25 | Mon | Thiel Reveal | research note | 2012-03 to 2017-12 source-document context | 2014 scheduling, Valar intro, later logistics, earlier attendee context | [open](workbook/outputs/2026/05/25/thiel-reveal/README.md) |
| 2026-05-25 | Mon | Zorro Ranch | research note | 2009 to 2015 source-document context | Guest access, staff logistics, property operations, aviation, registration context | [open](workbook/outputs/2026/05/25/zorro-ranch/README.md) |
| 2026-05-24 | Sun | U-Haul Evidence Transfer | manual transcription | 2025-02-27 to 2025-03-25 records-handling sequence | WFO-to-IMD transfer sequence, ERT photo logs, item-level transcription, and release-processing context | [open](workbook/outputs/2026/05/24/uhaul-evidence-transfer/README.md) |
| 2026-05-18 | Mon | French Financial Corridor | packet | 2026-05-02 to 2026-05-23 French agency contact, first response, and packet transmission sequence | French agency response, Brunel/MC2 evidence packet, email-thread export, PGP header extract, and rendered Pages disclosure | [open](https://jgoyd.github.io/Public-Workbook/french-financial-corridor/) |
| 2026-05-13 | Wed | SEC Ito Referral | supplement | 2026-05-13 supplement and 2026-05-14 receipt | Supplement 01, OMMS update PDF, receipt EML, and hashes for submission 17780-976-067-126 | [open](workbook/outputs/2026/05/13/sec-ito-referral/README.md) |
| 2026-05-12 | Tue | SEC KSA Bond 2016 Omega | submission | 2026-05-12 SEC TCR packet for 2016 KSA sovereign bond issue context | SEC TCR packet and before-submission export for KSA Bond 2016 Omega | [open](workbook/outputs/2026/05/12/sec-ksa-bond-2016-omega/README.md) |
| 2026-05-06 | Wed | SEC Ito Referral | submission | 2026-05-06 SEC TCR submission | Initial SEC TCR evidence packet for submission 17780-976-067-126 | [open](workbook/outputs/2026/05/06/sec-ito-referral/README.md) |
<!-- work-timeline:end -->

---

## Current Threads

<!-- topic-index:start -->
| Topic | Entries | Latest work | Jump in |
| --- | ---: | --- | --- |
| Buenos Aires Bond | 1 | 2026-05-27 | [topic page](workbook/topics/buenos-aires-bond.md) |
| FCA London Banking Conduct | 1 | 2026-05-27 | [topic page](workbook/topics/fca-bank-of-china-stanchart.md) |
| French Financial Corridor | 1 | 2026-05-18 | [topic page](workbook/topics/french-financial-corridor.md) |
| RemoteRAT / RATtrap | 1 | 2026-05-25 | [topic page](workbook/topics/remoterat-rattrap.md) |
| SEC Ito Referral | 2 | 2026-05-13 | [topic page](workbook/topics/sec-ito-referral.md) |
| SEC KSA Bond 2016 Omega | 1 | 2026-05-12 | [topic page](workbook/topics/sec-ksa-bond-2016-omega.md) |
| Thiel Reveal | 1 | 2026-05-25 | [topic page](workbook/topics/thiel-reveal.md) |
| U-Haul Evidence Transfer | 1 | 2026-05-24 | [topic page](workbook/topics/uhaul-evidence-transfer.md) |
| Valar / Southern Trust | 1 | 2026-05-26 | [topic page](workbook/topics/valar-southern-trust.md) |
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
