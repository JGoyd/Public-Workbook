# SMTP Header Analysis

## Case: REMOTERAT-2026-05
**Author:** Joseph Goydish II

---

## Hop Chain

**Hop 1 — Origin**
- `Received: from HY-52556 (207.189.26.195)` by `smtp.gmail.com` via ESMTPSA
- TLS: ECDHE-ECDSA-AES128-GCM-SHA256 (128-bit)
- Timestamp: `Mon, 25 May 2026 13:56:05 -0700 PDT`
- SMTP session: `46e09a7af769-7e60648257csm7912345a34`

**Hop 2 — Gmail internal**
- Message-ID: `6a14b765.dbd6c068.4730f.84a6@mx.google.com`
- DKIM signed: `d=gmail.com` / `b=PteO1gbs...` (2048-bit RSA-SHA256)

**Hop 3 — Delivery**
- Received at `mail.protonmail.ch` (mailinosl106) via ESMTPS TLS 1.3
- Delivered to: `[RECIPIENT REDACTED]`
- SPF: PASS (smtp.mailfrom=gmail.com)
- DKIM: PASS (2048-bit, d=gmail.com)
- DMARC: PASS (p=none, header.from=gmail.com)
- Spam score: 0

## Key Indicators

| Field | Value |
|---|---|
| Return-Path | `cigardah287@gmail.com` |
| SMTP Origin IP | `207.189.26.195` (HY-52556) |
| SMTP Session | `46e09a7af769-7e60648257csm7912345a34` |
| Message-ID | `6a14b765.dbd6c068.4730f.84a6@mx.google.com` |
| DKIM Fragment | `b=PteO1gbs` |
| Subject | Business Meeting Invitation |
| From Display | Growth Strategies LLC |
