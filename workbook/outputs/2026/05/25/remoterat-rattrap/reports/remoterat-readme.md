# RemoteRAT

> **Active Infrastructure at Time of Publication**
> Telegram C2 bot (`@Damisky001bot`) and RMM dropper host (`dgs.brimis[.]org`) confirmed live at 2026-05-25T20:56:07Z. All indicators are defanged for safe handling.

---

## Overview

**RemoteRAT** is an active initial-access broker campaign that delivers the **RATtrap** JScript dropper via authenticated spearphishing email. RATtrap silently installs two independent remote-management tools (ScreenConnect + LogMeIn Resolve) and reports victim telemetry to an operator-controlled Telegram bot in real time.

This repository documents Case 2026-05 — the first public observation of the RemoteRAT campaign — and its connection to the broader SILENTCONNECT ScreenConnect-abuse cluster tracked by Elastic Security Labs and SOCPrime.

| Field | Value |
|---|---|
| **Campaign** | RemoteRAT |
| **Dropper** | RATtrap (JScript) |
| **Case ID** | REMOTERAT-2026-05 |
| **First Observed** | 2026-05-25T20:56:07Z |
| **Author** | Joseph Goydish II |
| **Actor Handle** | `Damisky` / `Misky` |
| **Classification** | Initial Access Broker — Dual-RMM RAT Dropper |
| **Delivery** | Gmail-authenticated spearphishing via Hyonix VPS (AS931) |
| **C2 Channel** | Telegram Bot API |
| **Campaign Cluster** | SILENTCONNECT (Elastic / SOCPrime) |
| **Infra Age at Attack** | 17 days |
| **Prior Feed Coverage** | Zero — not indexed on any public feed at discovery |

---

## How the Attack Works

A business-invitation email arrives in the victim inbox looking entirely legitimate. It passes SPF, DKIM, and DMARC. It is sent from a real Gmail account over an authenticated connection routed through a Hyonix Windows VPS.

When the victim clicks the link, a file called `Business-Invitation.js` is pulled from Dropbox and executed by Windows Script Host. That is the **RATtrap** dropper. Within seconds an attacker-controlled Telegram bot logs the victim's computer name and username. Two remote-management tools are then installed silently as Windows services.

From that point the attacker has full persistent access to the machine. They can see the screen, interact with the keyboard and mouse, transfer files, and return through either channel whenever they choose. Nothing visibly unusual happens during installation. No antivirus fires because the tools are legitimate signed software.

The ScreenConnect component has iOS and Android clients, giving a network-present operator a potential bridge from the initial Windows foothold to mobile devices on the same network.

---

## RATtrap Dropper

RATtrap is an obfuscated JScript dropper distributed as a `.js` file with a spoofed `Content-Type: application/json` header to evade gateway inspection.

Key capabilities:
- Custom base64 rotation cipher for string obfuscation
- Real-time Telegram beacon on install start and completion — victim `ComputerName` and `UserName` sent before any file is written to disk
- Silent download and execution of ScreenConnect MSI (`msiexec /qn /norestart`)
- Silent install of LogMeIn Resolve as a secondary persistent channel
- Cleanup of any existing LogMeIn install before deploying fresh

Actor fingerprint: the string `Inatllation` (misspelled) appears twice in the decoded payload. Same typo, consistent across both Telegram beacon messages. Reliable pivot for retrohunting.

---

## Attack Chain

```
[Hyonix VPS HY-52556 / 207.189.26.195 / AS931]
       |  ESMTPSA authenticated submission
       v
[smtp.gmail.com]
       |  Business Meeting Invitation — SPF PASS / DKIM PASS / DMARC PASS
       v
[Victim Inbox — clean delivery]
       |  Victim clicks link
       v
[invite.php] -- HTTP 302 -->
[Dropbox: Business-Invitation.js | Content-Type: application/json (spoofed)]
       |  Windows Script Host executes RATtrap
       v
[RATtrap JScript Dropper — custom base64 cipher]
       |
       +-- Telegram: @Damisky001bot (8970330885) chat 6687082236
       |     ComputerName | UserName | "Inatllation started"
       |
       +-- dgs.brimis[.]org --> bremis.ClientSetup.msi (11.6 MB)
       |     msiexec /qn /norestart  |  group: c=Misky
       |
       +-- LogMeIn Resolve MSI (secondary)
             Remove existing install, deploy fresh, persist as service
```

---

## Repository Structure

```
RemoteRAT-2026/
├── README.md
├── docs/
│   ├── index.html                GitHub Pages dashboard
│   └── incident-map.html
├── iocs/
│   ├── iocs-high-confidence.csv
│   ├── iocs-medium-confidence.csv
│   └── domains.txt
├── yara/
│   └── rattrap_jscript_dropper.yar
└── analysis/
    ├── smtp-headers.md
    ├── payload-notes.md
    └── cluster-linkage.md
```

---

## IOCs (High Confidence)

All indicators defanged. Remove brackets before operational use.

| Type | Indicator |
|---|---|
| IPv4 | `207[.]189[.]26[.]195` |
| Domain | `dgs.brimis[.]org` |
| Domain | `brimis[.]org` |
| Filename | `Business-Invitation.js` |
| Filename | `bremis.ClientSetup.msi` |
| Sender | `cigardah287[@]gmail[.]com` |
| Message-ID | `6a14b765.dbd6c068.4730f.84a6@mx.google.com` |
| SMTP Session | `46e09a7af769-7e60648257csm7912345a34` |
| String | `Inatllation` (actor typo fingerprint) |
| URL Param | `c=Misky` |
| Telegram Bot | `@Damisky001bot` (ID: 8970330885) |
| Telegram Chat | `6687082236` |

---

## YARA

See [`rattrap_jscript_dropper.yar`](../other/rattrap_jscript_dropper.yar)

---

## MITRE ATT&CK

T1566.002, T1078, T1583.003, T1583.001, T1204.002, T1059.007, T1027, T1553, T1071.001, T1102.002, T1219, T1082, T1567

---

## References

- Elastic Security Labs — SILENTCONNECT campaign
- SOCPrime — SILENTCONNECT active threat (March 2026)
- Acronis TRU — Dual-RMM patterns (September 2025)
- Darktrace — Hyonix AS931 investigation (May 2025)

---

## License

Released for defensive and research purposes only.
Copyright 2026 Joseph Goydish II.
