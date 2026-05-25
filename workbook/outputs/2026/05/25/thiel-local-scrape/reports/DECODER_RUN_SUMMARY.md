# Peter Thiel Canonical Decoder Run Summary

Mode: additive local run. Source databases and evidence files were not modified.

## Runs

- Current 10-slot historical harness:
  - Log: `phase14_thiel_current_10slot.log`
  - Scope: `[local path omitted]`
  - Key order: `0416,0928,0514,0521,0521,1001,0302,0906,0613,0628`
  - Result: completed. Top convergences landed mostly on DOJ/Maxwell legal-document rows, so this log is retained as raw decoder context rather than promoted as Thiel-specific evidence.

- Canonical multi-space sweep:
  - Script: `run_canonical_thiel_decoder.py`
  - Log: `canonical_decoder_run.log`
  - Summary: `canonical_decoder_summary.json`
  - All relevant hits: `canonical_decoder_hits.csv` / `canonical_decoder_hits.jsonl`
  - Promoted hits: `meaningful_decoder_hits.csv`
  - Key order: `0416,0928,0514,0521,0521,1001,0302,0906,0613,0628`

## Canonical Sweep Counts

- Spaces swept: 10
- Decoder hits per space: 2,055
- Total Thiel-family relevant hits after token filtering: 54
- Promoted meaningful hits: 11
- Direct EFTA OCR exports from promoted hits: 6
- Additional no-EFTA email-pair/sender hits resolved to source documents: 26 rows / 18 unique EFTAs
- Total OCR text files now in `ocr_text`: 24

## Promoted EFTA Text Exports

Directory: `ocr_text`

Direct EFTA hits:

- `EFTA00465311.txt` - Dec. 1, 2017 dietary-restriction logistics for Peter Thiel.
- `EFTA01055201.txt` - Feb. 3, 2017 Epstein to Thiel: Palm Beach weekend availability.
- `EFTA01921275.txt` - May 30, 2014 Epstein to Ehud Barak: Peter Thiel can come to dinner on June 9.
- `EFTA02024389.txt` - March 2012 proposed money-conference attendee list including Peter Thiel.
- `EFTA02097678.txt` - Sept. 2014 schedule pages listing Peter Thiel, lunch with Peter Thiel, Bill Burns, Jagland/Terje, Boris Nikolic, Jabor, Leon Black, and others.
- `EFTA02507068.txt` - April 9, 2015 Epstein to Thiel; short OCR-garbled note mentioning Nathan Myhrvold and money/payment wording.

Resolved no-EFTA decoder hits:

- `EFTA00362699.txt` and related Sept. 12, 2014 duplicates/variants - Epstein/Thiel weekend scheduling chain: one-on-one, Bill Burns joining, dinner with Woody/Kathy, and Sunday lunch with Bob Kerrey.
- `EFTA02098197.txt` - Talia Parnass / Lesley Groff logistics for Thiel at 9 East 71st Street; includes the same Bill Burns / Woody / Kathy / Bob Kerrey chain and notes Thiel had a last-minute conflict for brunch.
- `EFTA02587944.txt` - Epstein to Larry Summers: "peter thiel with me weekend, ny, are you around?"
- `EFTA02594707.txt` - Peter Thiel to Epstein, cc Andrew McCormack and James Fitzgerald, "introductions"; describes Valar Ventures and says it would make sense for Epstein to put in `$10-20MM`.

See `resolved_noefta_email_docs.csv` for the full resolved source-document list.

## Meaningful Buckets

1. 2014 direct-contact / schedule channel.
   - Strongest text: `EFTA00362699`, `EFTA02098197`, `EFTA02097678`, `EFTA01921275`.
   - Meaning: decoder reinforced the already important 2014 Thiel channel around Epstein-hosted meetings and logistics.

2. Valar financial-introduction channel.
   - Strongest text: `EFTA02594707`.
   - Meaning: direct Thiel-authored Valar introduction to Epstein with an explicit proposed investment range.

3. Continued logistical contact after 2014.
   - Strongest text: `EFTA00465311`, `EFTA01055201`.
   - Meaning: later logistical/contact records, useful for timeline continuity, not standalone legal conclusions.

4. Early network/attendee context.
   - Strongest text: `EFTA02024389`.
   - Meaning: Thiel appears on a proposed money-conference attendee list with other tech/finance names.

## Guardrail

Decoder output is a prioritization layer. The meaningful items above are only promoted because they have extracted EFTA text. No conduct claim should be made from decoder position alone.
