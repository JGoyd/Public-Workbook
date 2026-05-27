# Valar Source-Document Hardening Log

Date: 2026-05-26

Scope: source-PDF staging and visual verification for the Valar / Southern Trust lane. This is an additive hardening pass and does not update the submission packet.

## Source Staging

Public DOJ source PDFs were staged in:

`india_supplement_2026-05-26/hardening/source_pdfs/`

Manifest:

`india_supplement_2026-05-26/hardening/source_pdf_manifest_2026-05-26.csv`

Result: 16 PDFs validate as `%PDF` files and match expected page counts. The DOJ path required the age-verification cookie `justiceGovAgeVerified=true`; without it, DOJ returned an HTML age-verification page rather than a PDF.

Rendered verification pages are in:

`india_supplement_2026-05-26/hardening/source_renders/`

Visual verification matrix:

`india_supplement_2026-05-26/hardening/source_pdf_visual_verification_2026-05-26.csv`

## April 4, 2017 Reconciliation Item

The April 4, 2017 `$2,500,000` Valar III capital-call item is now hardened from source PDFs:

| Source | Visual finding |
|---|---|
| `EFTA01435885` p1 | Deutsche Bank Private Wealth Management asset-movement authorization for Southern Trust Company Inc.; wire amount `$2,500,000`; bank Silicon Valley Bank; ABA `121140399`; beneficiary Valar Global Fund III LP; account `3301520427`; additional instructions `Southern Trust Company Inc. Capital Call`. |
| `EFTA01435887` p3 | Signature/date block shows Darren Indyke and `04-04-2017`. OCR is imperfect around the signature line, but the source image visibly supports the date and printed name. |
| `EFTA01387768` p1 | Deutsche Bank internal email, 2017-04-04, `RE: STC wire (I)`, says the request and docs were uploaded into NetX and Southern Trust is wiring `$2.5mm` per attached instructions. It also instructs verification using Darren's number listed on the account, not via Richard Kahn. |
| `EFTA01299550` p1 | Incoming/outgoing wires/checks/ACH report dated 04/04/2017 lists Silicon Valley Bank, Southern Trust Company Inc. Capital Call, Valar Global Fund III LP, account `3301520427`, amount `2500000.00`. |
| `EFTA00811490` p2 / `EFTA00811491` | April 30, 2017 asset summary lists `Valar III Capital Call 4 (2,500,000)` and `Valar III Capital Call 5 (3,000,000)`. |

Treatment: call 4 can now be treated as visually confirmed source evidence rather than only OCR/corpus inference.

## 2019 Final Draws

| Source | Visual finding |
|---|---|
| `EFTA01288200` p1 | January 2019 Deutsche Bank statement shows 01-08 outgoing money transfer to Silicon Valley Bank account `3301520427` / Valar Global Fund III LP / `(2,500,000.00)`. |
| `EFTA01288388` p2 / `EFTA01288389` | April 2019 Deutsche Bank statement shows 04-17 outgoing money transfer to Silicon Valley Bank account `3301520427` / Valar Global Fund III LP / `(1,500,000.00)`. |

These two rows visually support the final `$4,000,000` after the June 2018 paid-in capital position of `$21,000,000`.

## OCR Caveats

- `EFTA01387768` visually reads `$2.5mm`, but text extraction can render it as `52.5mm` because the dollar sign is joined to the amount.
- Several bank statements OCR `Valar Global Fund III LP` as `Valar Globaal Fund III LP` or similar. The visual source pages still show the same Valar/SVB/account/payment pattern.
- `EFTA01435885` amount formatting may extract as `$ 2,500.000`; visual review supports `$2,500,000`.

## Current Hardened Status

Confirmed:

- Source PDFs staged and hash-manifested.
- Critical pages rendered to PNG.
- April 4 call-4 reconciliation visually confirmed across wire authorization, internal DB email, ACH/wires report, and asset summary.
- January and April 2019 final Valar outflows visually confirmed from bank statements.

Still open:

- Standalone native capital-call notice for call 3.
- Standalone native capital-call notice or approval email for 2019 final draw A and B.
- Standalone source page for DB-SDNY-0006985 / call 9 bank statement row, beyond the transaction-chart support already captured.
