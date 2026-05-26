# 2026-05-25 - RemoteRAT / RATtrap

Public threat-research workbook entry for `REMOTERAT-2026-05`.

This entry groups the public RemoteRAT repository artifacts into one dated workbook page: the campaign write-up, SMTP header notes, payload notes, cluster linkage note, IOC tables, domain list, YARA rule, and GitHub Pages export.

## Snapshot

| Field | Value |
| --- | --- |
| Topic | RemoteRAT / RATtrap |
| Case ID | `REMOTERAT-2026-05` |
| Date | 2026-05-25 |
| Public repository | [JGoyd/RemoteRAT](https://github.com/JGoyd/RemoteRAT) |
| Published page | [RemoteRAT Pages](https://jgoyd.github.io/RemoteRAT/) |
| Initial commit | [`329b40f`](https://github.com/JGoyd/RemoteRAT/commit/329b40f3ce6ec719ff5a9235b5ce7105d5cbb377) |
| Repo commit status | GitHub-verified signed commit |
| Main artifact types | Markdown reports, IOC CSVs, domain list, YARA rule, HTML page export |

## What This Entry Contains

| Area | Files | What to open first |
| --- | ---: | --- |
| Reports | 4 | [RemoteRAT repo README](reports/remoterat-readme.md) |
| IOC tables | 2 | [High-confidence IOCs](tables/iocs-high-confidence.csv) |
| Raw lists | 1 | [Domain blocklist](raw/domains.txt) |
| Detection rule | 1 | [RATtrap YARA rule](other/rattrap_jscript_dropper.yar) |
| HTML exports | 2 | [GitHub Pages export](exports/github-pages-index.html) |

## Findings by Lane

### 1. Delivery and Headers

The SMTP header note records authenticated Gmail delivery routed through a Hyonix VPS origin. The report keeps the useful mail-routing fields together: origin IP, session ID, Message-ID, authentication results, DKIM fragment, and displayed sender context.

Open:

- [SMTP header analysis](reports/smtp-headers.md)

Useful anchors:

- SMTP origin IP: `207[.]189[.]26[.]195`
- Sender: `cigardah287[@]gmail[.]com`
- Subject: `Business Meeting Invitation`
- Authentication: SPF, DKIM, and DMARC pass in the published note

### 2. RATtrap Payload Behavior

The payload note describes `Business-Invitation.js` as a JScript dropper served with a spoofed `application/json` content type. It records runtime string decoding, Telegram beaconing, ScreenConnect installation, LogMeIn Resolve installation, and the repeated typo string used as a pivot.

Open:

- [Payload notes](reports/payload-notes.md)

Useful anchors:

- Dropper filename: `Business-Invitation.js`
- MSI filename: `bremis.ClientSetup.msi`
- ScreenConnect group parameter: `c=Misky`
- Typo fingerprint: `Inatllation`

### 3. Telegram C2 and Operator Context

The public repo records a Telegram bot and chat as part of the observed C2 path at publication time. The workbook keeps those values in the IOC table and YARA-linked context rather than spreading them across the entry.

Open:

- [High-confidence IOCs](tables/iocs-high-confidence.csv)
- [RATtrap YARA rule](other/rattrap_jscript_dropper.yar)

Useful anchors:

- Telegram bot: `@Damisky001bot`
- Telegram bot ID: `8970330885`
- Telegram chat: `6687082236`

### 4. Dual-RMM Persistence

The repo write-up and payload note describe a two-channel remote-management setup: ScreenConnect plus LogMeIn Resolve. The workbook preserves the published notes and the detection rule without repackaging them as a new report.

Open:

- [RemoteRAT repo README](reports/remoterat-readme.md)
- [Payload notes](reports/payload-notes.md)

Useful anchors:

- ScreenConnect dropper host: `dgs.brimis[.]org`
- ScreenConnect MSI: `bremis.ClientSetup.msi`
- Secondary RMM: LogMeIn Resolve

### 5. SILENTCONNECT Cluster Linkage

The cluster note groups RemoteRAT with earlier SILENTCONNECT-compatible nodes by URL grammar and ScreenConnect setup pattern. The RemoteRAT node adds Telegram beaconing and dual-RMM persistence in the published note.

Open:

- [Cluster linkage](reports/cluster-linkage.md)

Cluster nodes listed:

- `tigecarllc[.]de`
- `newoneazu[.]com`
- `bumptobabeco[.]top`
- `dgs.brimis[.]org`

### 6. Published Detection Material

The entry includes two IOC CSVs, a domain list, and a YARA rule. The CSVs separate high-confidence case indicators from medium-confidence cluster context.

Open:

- [High-confidence IOCs](tables/iocs-high-confidence.csv)
- [Medium-confidence IOCs](tables/iocs-medium-confidence.csv)
- [Domain blocklist](raw/domains.txt)
- [RATtrap YARA rule](other/rattrap_jscript_dropper.yar)

## Artifact Map

| Type | File | Description |
| --- | --- | --- |
| Report | [remoterat-readme.md](reports/remoterat-readme.md) | Public repository README copied into the workbook |
| Report | [smtp-headers.md](reports/smtp-headers.md) | SMTP header notes |
| Report | [payload-notes.md](reports/payload-notes.md) | RATtrap payload notes |
| Report | [cluster-linkage.md](reports/cluster-linkage.md) | SILENTCONNECT cluster linkage note |
| Table | [iocs-high-confidence.csv](tables/iocs-high-confidence.csv) | High-confidence IOC table |
| Table | [iocs-medium-confidence.csv](tables/iocs-medium-confidence.csv) | Medium-confidence IOC table |
| Raw | [domains.txt](raw/domains.txt) | Defanged domain list |
| Rule | [rattrap_jscript_dropper.yar](other/rattrap_jscript_dropper.yar) | YARA rule |
| HTML export | [github-pages-index.html](exports/github-pages-index.html) | Copied GitHub Pages page |
| HTML export | [incident-map.html](exports/incident-map.html) | Copied incident map page |

## Related Links

- [RemoteRAT repository](https://github.com/JGoyd/RemoteRAT)
- [RemoteRAT GitHub Pages](https://jgoyd.github.io/RemoteRAT/)
- [Initial signed commit](https://github.com/JGoyd/RemoteRAT/commit/329b40f3ce6ec719ff5a9235b5ce7105d5cbb377)

---

[Back to workbook home](../../../../../../README.md)
