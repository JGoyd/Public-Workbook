# Build Summary

The workbook is a flat, date-organized public log. Each `outputs/YYYY/MM/DD/<topic>/` folder holds one entry with its own README, artifacts, and local manifest when available.

## Current Entry Count

| Date | Entries |
| --- | ---: |
| 2026-05-27 | 3 |
| 2026-05-26 | 2 |
| 2026-05-25 | 3 |
| 2026-05-24 | 1 |
| 2026-05-18 | 1 |
| 2026-05-13 | 1 |
| 2026-05-12 | 1 |
| 2026-05-06 | 2 |
| 2026-05-04 | 1 |
| 2026-04-30 | 1 |

Total entries: 16

## Latest Update

Latest local update: prepared `Lithuania Panevezys Prosecutor Update` as an April 30 first-acknowledgement entry, using source-faithful wording that submitted information was attached to criminal case materials and forwarded for evaluation.

Latest committed checkpoint before this local update: `docs(workbook): log french authority hand delivery` on `main`.

May 27 entries are:

- `Buenos Aires Bond`
- `FCA London Banking Conduct`
- `French Authority Packet Hand Delivery`

May 6 backfill:

- `IRS Form 211 Bates Evidence Packet` was added under the original 2026-05-06 filing date, not May 27. Its root README open link points to the GitHub Pages PDF mirror.

May 4 backfill:

- `Singapore CPIB FormSG Submission` was added under the original 2026-05-04 submission timestamp, not the May 27 package assembly date. Its root README open link points to the GitHub Pages PDF mirror.

April 30 backfill:

- `Lithuania Panevezys Prosecutor Update` was added under the 2026-04-30 first acknowledgement date. Its root README open link points to the April 30 PDF mirror; the May 22 agency update and May 23 reply remain inside the same core bundle as later context.

Latest active paths:

- Current daily note: `workbook/daily/2026-05-27.md`
- Lithuania daily note: `workbook/daily/2026-04-30.md`
- IRS filing daily note: `workbook/daily/2026-05-06.md`
- Singapore CPIB daily note: `workbook/daily/2026-05-04.md`
- Template: `workbook/templates/entry_template.md`
- Index builder: `scripts/update-indexes.py`
- Index test: `tests/test_update_indexes.py`

Resume checks:

```powershell
python scripts/update-indexes.py --check
python -m unittest discover -s tests -v
```

Both checks passed on 2026-05-27 after the IRS entry and index refresh.

## Continuation Notes

- Generated index tables are rebuilt by `scripts/update-indexes.py`; do not edit generated blocks in `README.md` by hand.
- New entries should start from `workbook/templates/entry_template.md` and land under `workbook/outputs/YYYY/MM/DD/<topic-slug>/`.
- Public HTML mirrors currently live under `docs/<topic-slug>/` when an entry has a Pages route.
- The French hand-delivery entry intentionally logs only the packet PDFs, verification files, and public key. Source build scripts, intermediate HTML, QA renders, assets, and second-reader notes were held back from the public workbook entry.
- IRS Form 211 packet PDF is intentionally public in `workbook/outputs/2026/05/06/irs-form-211-bates-evidence-packet/reports/` and mirrored under `docs/irs-form-211-bates-evidence-packet/`.
- Singapore CPIB response-ID PDF is intentionally public in `workbook/outputs/2026/05/04/singapore-cpib-formsg-submission/reports/` and mirrored under `docs/singapore-cpib-formsg-submission/`.
- Lithuania core bundle intentionally excludes the combined report/email-body markdown, package manifest CSV, and duplicate Downloads EML export.
