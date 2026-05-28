# TRACK A — FCA (UK) · Bank of China (UK) Limited & Standard Chartered

> **Standing disclaimer:** Filing and agency acknowledgement does not constitute adjudication of the underlying claims.

## Case identifiers

- **FCA reference:** `00Db00K8yP.500Sk019RuGn` (FCA Individuals Inbox `consumer.queries@fca.org.uk`)
- **Submission posture:** Conduct / AML supervisory query, supplemented 2026-05-11
- **Subjects (entities):** Bank of China (UK) Limited; Standard Chartered Bank
- **Source corpus referenced:** U.S. Department of Justice public-release Epstein document corpus (Bates references `EFTA01039905`, `EFTA01039908`, `EFTA00664435`, `EFTA02238618`, `EFTA02269722`, `EFTA01778968`, `EFTA01741284`)

## My role

**Reporter / supervisory-query author.** I sent an evidence-based supplement to a prior FCA submission, naming the subjects, citing the DOJ public-release Bates IDs, and offering to provide the underlying PDFs on request. I make no claim that the FCA has opened an investigation or reached any conclusion.

## Timeline

| Date (UTC) | Event | External anchor |
|---|---|---|
| (prior) | Initial FCA submission opened under reference `00Db00K8yP.500Sk019RuGn` | FCA case reference (third-party-controlled) |
| 2026-05-08 16:42:58 UTC | **FCA Consumer Queries / Supervision Hub issues a named-officer substantive reply** (subject: *Bank of China (UK) Limited and Standard Chartered*). Body confirms: (i) FCA recognises both subjects on the Financial Services Register; (ii) FCA confirms receipt of the specific factual concerns (cited verbatim in the reply: 5-day work-shadow placement for a 17-year-old, named intermediary, named offeror); (iii) named officer attests: *"I've today let my colleagues in the appropriate team that supervise the conduct of Bank of China (UK) Limited know about your concerns."* **DKIM-pass `fca.org.uk` selector `intactfcaorguk2` (2048-bit).** | `evidence/FCA-BoC-StanChart-Andrew-substantive-inbound-2026-05-08.eml` SHA-256 `eb9978cb2a2717910ec4fc809ee7518ce456c2962df48684e0c8fafb8213f936` |
| 2026-05-11 15:09:57 UTC | I send the supplement listed in this folder | `evidence/FCA-BoC-StanChart-supplement-2026-05-11.eml` SHA-256 `207fa35b8c57f8d4262442a0b497f9a2509170ce67c070c314d06e706c9b7e77` |
| 2026-05-11 15:11:48 UTC | **FCA system issues automated `Thank you your query has been received.` acknowledgement** from `noreply@fca.org.uk` (Salesforce-relayed). **DKIM-pass on `fca.org.uk` (2048-bit, selector `intactfcaorguk2`).** | `evidence/FCA-acknowledgement-noreply-2026-05-11.eml` SHA-256 `b9f0e77b682359d3e5717b0140deb66790bf2b343c27ec493c38385923f866fc` |
| 2026-05-13 09:08:40 UTC | **FCA Supervision Hub officer issues a second named-officer substantive reply** (subject: *Bank of China (UK) Limited*). Body confirms: (i) receipt of the 2026-05-11 supplement; (ii) explicit **supervisory referral attestation** — *"I've today referred the additional information you've provided regarding Bank of China (UK) Limited to the supervisory appropriate team for further investigation."* **DKIM-pass `fca.org.uk` selector `intactfcaorguk2` (2048-bit).** Same matter reference `00Db00K8yP.500Sk019RuGn`, same Salesforce intake system, same officer who replied on 2026-05-08. | `evidence/FCA-BoC-Andrew-supervisory-referral-inbound-2026-05-13.eml` SHA-256 `41a3003fe5495e14ca4922e0bf486b0a8f47425ba15a01d20f9369622b23bdf5` |

## Substance of the supplement (summary — full text in `evidence/`)

The supplement adds three structured points to the original report:

1. **PEP identification (EFTA01039905, EFTA01039908).** The 17-year-old placement candidate is identified by name; both parents held senior diplomatic positions at the time of the placement. Standard Chartered's CEO had previously flagged placements of this kind as a bribery risk and the bank declined to proceed (EFTA00664435). Bank of China (UK) subsequently accepted the candidate. Under the FCA Handbook definition, this fits Politically Exposed Person status and triggers Enhanced Due Diligence.
2. **Concurrent financial inducement of the PEP's family (EFTA02238618, EFTA02269722).** Decrypted ledger records show medical-invoice payments to the candidate's father (March 2018) and Apple-product purchases for the family's other children (January 2019), made by the offeror's office during the same window the placement was being arranged.
3. **Undeclared London front (EFTA01778968).** A March 2011 internal email proposes an "E&S Investment office in London for European & China deals" structured so the office is "fronted/headed by me and nobody knows you are behind it." If this office was operational during the placement window, it may be relevant to the firm's third-party/introducer risk management.

The supplement attaches the maintainer's PGP public key (fingerprint `6DCB 4235 1237 A98B B474 0070 B36F FC36 1AE5 DAF6` — secondary key; see canonical-profile note on canonical/secondary fingerprint reconciliation) and offers the underlying PDF extracts on request.

## Evidence

| Artifact | Path | SHA-256 | Signature | OTS |
|---|---|---|---|---|
| **2026-05-08 FCA substantive reply** (inbound, **DKIM-pass `fca.org.uk`**, named-officer attestation that concerns have been passed to BoC (UK) supervisory team) | `evidence/FCA-BoC-StanChart-Andrew-substantive-inbound-2026-05-08.eml` | `eb9978cb2a2717910ec4fc809ee7518ce456c2962df48684e0c8fafb8213f936` | PENDING (.asc) | PENDING (.ots) |
| 2026-05-11 FCA supplement (sent by me) | `evidence/FCA-BoC-StanChart-supplement-2026-05-11.eml` | `207fa35b8c57f8d4262442a0b497f9a2509170ce67c070c314d06e706c9b7e77` | PENDING (.asc) | PENDING (.ots) |
| 2026-05-11 FCA automated acknowledgement (inbound, **DKIM-pass `fca.org.uk`**) | `evidence/FCA-acknowledgement-noreply-2026-05-11.eml` | `b9f0e77b682359d3e5717b0140deb66790bf2b343c27ec493c38385923f866fc` | PENDING (.asc) | PENDING (.ots) |
| **2026-05-13 FCA supervisory referral attestation** (inbound, **DKIM-pass `fca.org.uk`**, named-officer attestation that 2026-05-11 supplement was *"referred to the supervisory appropriate team for further investigation"*) | `evidence/FCA-BoC-Andrew-supervisory-referral-inbound-2026-05-13.eml` | `41a3003fe5495e14ca4922e0bf486b0a8f47425ba15a01d20f9369622b23bdf5` | PENDING (.asc) | PENDING (.ots) |

## External anchors (third-party-controlled)

- FCA Individuals Inbox routing: `consumer.queries@fca.org.uk`
- **FCA DKIM signature on inbound acknowledgement: `fca.org.uk` selector `intactfcaorguk2` (2048-bit) — 🟢 Tier-1 cryptographic anchor** (Authentication-Results: `dkim=pass (2048-bit key) header.d=fca.org.uk header.i=@fca.org.uk header.b="n0t0eu2W"`).
- FCA case reference (server-generated, embedded in subject line of supplement): `00Db00K8yP.500Sk019RuGn`.
- **Reference reconciliation**: the FCA acknowledgement headers expose the Salesforce internals — `X-Sfdc-Lk: 00Db0000000K8yP` (Org-Link) and `X-Sfdc-Entityid: 500Sk000019RuGn` (Entity-ID). These match the subject-line reference exactly and confirm `00Db…/500Sk…` is FCA's Salesforce-internal pair, not an external case number.
- Underlying source corpus: DOJ public-release Epstein document index (Bates EFTA-series IDs cited).

## Verification steps (third-party, no trust in me)

1. **Verify the FCA DKIM anchor on the inbound acknowledgement.** Run any DKIM-verifier against `evidence/FCA-acknowledgement-noreply-2026-05-11.eml`. Selector `intactfcaorguk2`, domain `fca.org.uk`, 2048-bit. SPF passes for `fca.org.uk`. DMARC passes with `p=reject`. The signed body includes the acknowledgement text and the message-ID `<3SoUKDexQcy3vSp5cr88Gw.ozS62SRud1mwfVpKMImfKCk@sfdc.net>` (Salesforce-relayed but DKIM-signed by FCA's own key).
2. The outbound supplement was sent from ProtonMail (`Esq.JG.legal@proton.me`) to `consumer.queries@fca.org.uk` on 2026-05-11 15:09:57 UTC. Because that `.eml` is the *outbound* copy, it does not carry an inbound DKIM signature; its authenticity now rests on (a) the FCA case reference in the subject line, which only the FCA's case-management system generates, and (b) the inbound FCA acknowledgement above, which carries the `fca.org.uk` DKIM signature and was issued ~2 minutes after the supplement was delivered.
3. The Bates references cited (e.g., `EFTA01741284`, `EFTA01039905`) can be located in the publicly released DOJ Epstein document corpus. Anyone can pull the named documents from the public release and confirm the textual content quoted in the supplement.
4. The PGP fingerprint attached in the supplement (`6DCB…DAF6`) is the maintainer's secondary key. The canonical key is `4A04 1F50 6D89 4F5E E391 7438 6487 8B56 A2EB 2D11`. See `canonical/index.md` for the cross-attestation status between the two keys.

## What this evidence does and does NOT establish

**It establishes:**
- That I filed an FCA conduct/AML supervisory query against Bank of China (UK) Limited and Standard Chartered, citing specific DOJ Bates-numbered documents.
- That the FCA Consumer Queries / Supervision Hub issued **two named-officer substantive replies** (2026-05-08 and 2026-05-13) on the matter, both DKIM-signed by `fca.org.uk`, both citing the matter reference `00Db00K8yP.500Sk019RuGn`, with explicit attestation that the information was passed to / referred to the supervisory team responsible for Bank of China (UK) Limited.
- The factual content of the cited DOJ Bates documents is independently verifiable by anyone from the public release.

**It does NOT establish:**
- That the FCA has opened any formal investigation, taken any enforcement action, reached any finding, or concluded anything substantive about the firms or individuals named. The FCA's standing policy (quoted verbatim in the 2026-05-08 reply) is that *"we'll generally not provide feedback on what action has been taken... there is no general right for members of the public to know the outcome of reports that they make."* The supervisory-referral attestation is an **intake-routing statement**, not an adjudicative finding.
- That any individual or entity named in the supplement has been found to have engaged in misconduct.
- That the PEP classification, AML deficiency, or "undeclared London front" characterizations have been adjudicated by any tribunal. They are my characterizations sourced to specific Bates-numbered documents.

## Domain-separation note

This case is **Track A only**. It does not reference, depend on, or share artifacts with any Track B (cybersecurity) case in this evidence system. The two tracks must never be combined in a single artifact or claim.
