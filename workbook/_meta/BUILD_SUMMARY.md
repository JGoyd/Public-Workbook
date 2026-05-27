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

Total entries: 14

## Latest Update

Latest local update: added `IRS Form 211 Bates Evidence Packet` as a May 6 portal filing log with the PDF packet held back from public output.

Latest committed checkpoint before this local update: `docs(workbook): log french authority hand delivery` on `main`.

May 27 entries are:

- `Buenos Aires Bond`
- `FCA London Banking Conduct`
- `French Authority Packet Hand Delivery`

May 6 backfill:

- `IRS Form 211 Bates Evidence Packet` was added under the original 2026-05-06 filing date, not May 27.

Latest active paths:

- Current daily note: `workbook/daily/2026-05-27.md`
- IRS filing daily note: `workbook/daily/2026-05-06.md`
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
- IRS Form 211 packet PDFs should stay under `workbook/private_holdback/` and remain ignored by git.
