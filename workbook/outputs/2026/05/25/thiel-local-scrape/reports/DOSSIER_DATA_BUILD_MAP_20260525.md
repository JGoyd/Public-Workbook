# Thiel Dossier Data Build Map

## Packet State

- Output folder: `[local path omitted]`
- Selected focused EFTA docs: 3837
- Full text exports: 3837
- Quote-bank rows: 9017
- Re-OCR / cleanup queue: 973
- Public ICE packet texts copied: 24
- Excluded low-signal candidate EFTAs: 3049

## Scope Note

This packet uses the local SQLite OCR/text layer. The database source paths point to `/atb-data/...`; local Windows PDFs were not found in the checked dataset paths. If those PDFs are restored, use `needs_reocr_or_cleanup.csv` as the re-OCR queue.

## Core Dossier Anchors

| EFTA | Lane | Pages | Quality | Score | Why it matters | Text |
|---|---|---:|---|---:|---|---|
| EFTA00609489 | thiel_valar_capital | 98 | USABLE_TEXT | 164 | Valar Global Fund III PPM; top decoder.cmd hit; contains $200M fund, Thiel Persons language, Thiel/Palantir framing. | `[local path omitted]` |
| EFTA00810400 | thiel_valar_capital | 74 | USABLE_TEXT | 164 | Second large Valar packet; useful comparison against Fund III terms/performance language. | `[local path omitted]` |
| EFTA00591045 | thiel_valar_capital | 22 | USABLE_TEXT | 152 | Valar deck; clean bridge from Thiel/Valar to Palantir intelligence/defense/law-enforcement language. | `[local path omitted]` |
| EFTA00807234 | thiel_valar_capital | 29 | USABLE_TEXT | 123 | Image-scan Valar-adjacent packet surfaced high in anchors; review before quoting. | `[local path omitted]` |
| EFTA02097678 | thiel_epstein_access_intel | 5 | USABLE_TEXT | 104 | Schedule lane placing Thiel around Burns/Leon/Larry/Cass/Ehud context. | `[local path omitted]` |
| EFTA00362699 | thiel_epstein_access_intel | 1 | USABLE_TEXT | 82 | Direct Epstein-Thiel scheduling email with Bill Burns, Woody/Kathy, Bob Kerrey. | `[local path omitted]` |
| EFTA02594707 | thiel_valar_capital | 1 | NOISY_OCR_REVIEW | 85 | Direct Thiel-to-Epstein Valar $10-20MM solicitation; needs cleanup but anchor is strong. | `[local path omitted]` |
| EFTA02656963 | security_tech | 4 | OCR_CLEANUP_REVIEW | 114 | Carbyne/Trae Stephens/Founders Fund/Palantir security-tech lane; keep separate from ICE unless bridged. | `[local path omitted]` |
| EFTA01921275 | direct_thiel | 1 | USABLE_TEXT | 44 | Epstein to Barak: Peter Thiel dinner availability. | `[local path omitted]` |
| EFTA02587944 | direct_thiel | 1 | NOISY_OCR_REVIEW | 44 | Epstein to Larry Summers: Peter Thiel with him weekend in NY. | `[local path omitted]` |
| EFTA00465311 | direct_thiel | 3 | USABLE_TEXT | 32 | 2017 Epstein staff dietary logistics for Peter Thiel. | `[local path omitted]` |
| EFTA02024389 | direct_thiel | 2 | USABLE_TEXT | 32 | 2012 MONEY seminar attendee list including Peter Thiel. | `[local path omitted]` |
| EFTA01055201 | direct_thiel | 1 | USABLE_TEXT | 32 | 2017 Palm Beach outreach from Epstein to Thiel. | `[local path omitted]` |

## First Quote Pass

Use `quote_bank.csv`, filtered to these first:
- `EFTA00609489` -> `[local path omitted]`
- `EFTA00810400` -> `[local path omitted]`
- `EFTA00591045` -> `[local path omitted]`
- `EFTA00807234` -> `[local path omitted]`
- `EFTA02097678` -> `[local path omitted]`
- `EFTA00362699` -> `[local path omitted]`
- `EFTA02594707` -> `[local path omitted]`
- `EFTA02656963` -> `[local path omitted]`

## Cleanup First

These are not blockers for knowing the data exists, but they need cleanup before polished quotation:
- `EFTA02594707`: NOISY_OCR_REVIEW / noise 29.85 / Direct Thiel-to-Epstein Valar $10-20MM solicitation; needs cleanup but anchor is strong.
- `EFTA02587944`: NOISY_OCR_REVIEW / noise 48.58 / Epstein to Larry Summers: Peter Thiel with him weekend in NY.
- `EFTA02656963`: OCR_CLEANUP_REVIEW / noise 9.18 / Carbyne/Trae Stephens/Founders Fund/Palantir security-tech lane; keep separate from ICE unless bridged.

## Dossier Structure From Data

1. Access timeline: `EFTA01921275`, `EFTA02587944`, `EFTA00362699`, `EFTA02097678`, `EFTA01055201`, `EFTA00465311`.
2. Money lane: `EFTA02594707`, `EFTA00591045`, `EFTA00609489`, `EFTA00810400`.
3. State/security lane: `EFTA00591045`, `EFTA00609489`, `EFTA02656963`, plus public ICE packet text.
4. Public ICE/Palantir context: `public_ice_packet_text` plus `public_ice_packet_manifest.csv`.
5. Decoder/key appendix: keep decoder output as triage/provenance, not evidence.


## Key / Decoder Context Layer

The key material is preserved and joined into the dossier packet. Use it as discovery provenance and prioritization: source text proves the factual claim; key hits explain why that context was elevated.

- Key context matrix: `[local path omitted]`
- Phase14 raw key-hit rows: `[local path omitted]`
- Desktop decoder key hits: `[local path omitted]`
- Reporting notes: `[local path omitted]`

Strong examples to consider in the dossier:
- `EFTA00609489`: desktop decoder top Valar PPM hit; use as key-prioritized fund packet, not hidden-code proof.
- `EFTA00810400`: desktop decoder also elevated the second Valar packet.
- `EFTA02097678`: phase14/key context intersects the schedule/access lane.
- `EFTA02594707`: direct text remains the proof; key context is secondary until the email cleanup is done.

## Files To Open First

- `[local path omitted]`
- `[local path omitted]`
- `[local path omitted]`
- `[local path omitted]`
- `[local path omitted]`
- `[local path omitted]`
