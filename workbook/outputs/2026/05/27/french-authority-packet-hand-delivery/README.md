---
date: 2026-05-27
slug: french-authority-packet-hand-delivery
title: French Authority Packet Hand Delivery
entry_type: delivery log
covers: 2026-05-27 in-person hand-delivery at Consulate General of France, 3399 Peachtree Rd NE #567, Atlanta, GA 30326
date_range: 2026-05-27
delivery_location: Consulate General of France, 3399 Peachtree Rd NE #567, Atlanta, GA 30326, United States
headline: In-person consulate hand-delivery log for the printed French authority packet and signature receipt
tags: [france, consulate, hand-delivery, packet, public-records]
status: logged
sources: []
---

# 2026-05-27 - French Authority Packet Hand Delivery

Minimal public workbook log for the user-reported in-person hand-delivery of the printed French authority packet.

## Hand-Delivery Location

| Field | Value |
| --- | --- |
| Delivery type | In-person printed packet hand-delivery |
| Location | Consulate General of France |
| Address | 3399 Peachtree Rd NE #567, Atlanta, GA 30326, United States |
| Date | 2026-05-27 |

## Snapshot

| Field | Value |
| --- | --- |
| Topic | French Authority Packet Hand Delivery |
| Work date | 2026-05-27 |
| Delivery mode | In-person printed packet hand-delivery |
| User-reported location | Consulate General of France, 3399 Peachtree Rd NE #567, Atlanta, GA 30326, United States |
| Official packet | [FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf](raw/source_pdfs/FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf) |
| Signature receipt | [FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf](raw/source_pdfs/FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf) |
| Verification files | Existing detached signature, SHA-256 checksum, receipt checksum, public key |
| Signing fingerprint | `4A04 1F50 6D89 4F5E E391 7438 6487 8B56 A2EB 2D11` |

## Files Logged

| Type | File | Description |
| --- | --- | --- |
| PDF packet | [FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf](raw/source_pdfs/FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf) | Printed authority packet |
| PDF receipt | [FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf](raw/source_pdfs/FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf) | Printable signature receipt for the packet |
| Signature | [FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf.asc](other/FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf.asc) | Existing detached signature for the official packet |
| Checksum | [FRENCH_AUTHORITY_PACKET_OFFICIAL.sha256.txt](other/FRENCH_AUTHORITY_PACKET_OFFICIAL.sha256.txt) | Existing SHA-256 sidecar for the official packet |
| Checksum | [FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf.sha256](other/FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf.sha256) | SHA-256 sidecar for the receipt PDF |
| Public key | [Joseph_Gs_Public_Key.asc](other/Joseph_Gs_Public_Key.asc) | Public key for verification |

## Verification

SHA-256:

```text
ddaf5222cf557cc49e21ae4cbcbe7621cf5416abadd05b4424c483781cb72dc8  FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf
39198beeb48adbd54b315c878d64ca15fce0f76fe49eb84ed59997a019b63681  FRENCH_AUTHORITY_PACKET_SIGNATURE_RECEIPT.pdf
```

Verification command:

```powershell
gpg --verify other\FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf.asc raw\source_pdfs\FRENCH_AUTHORITY_PACKET_OFFICIAL.pdf
```

## Held Back

The source folder's build scripts, intermediate HTML files, assets, QA render folders, and second-reader notes were not copied into this minimal public log entry.

---

[Back to workbook home](../../../../../../README.md)
