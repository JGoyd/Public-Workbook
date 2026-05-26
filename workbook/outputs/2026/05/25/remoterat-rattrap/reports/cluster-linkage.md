# SILENTCONNECT Cluster Linkage

## Case: REMOTERAT-2026-05
**Author:** Joseph Goydish II

---

## Shared Fingerprint

The URL grammar `/Bin/*ClientSetup.msi?e=Access&y=Guest` is shared across all four cluster nodes.

## Node Timeline

| Domain | First Seen | SC Group | ASN | Notes |
|---|---|---|---|---|
| tigecarllc[.]de | 2026-01-02 | c=cc | Cloudflare | Genesis node |
| newoneazu[.]com | 2026-01-26 | c=sim | Alsycon NL | CMD injection attempt in SC params |
| bumptobabeco[.]top | 2026-03-29 | y=Guest | Majestic Hosting VA | No group param |
| dgs.brimis[.]org | 2026-05-08 | c=Misky | Cloudflare | Telegram C2 + dual-RMM added |

## Evolution Notes

`dgs.brimis.org` is the first node to implement:
1. Real-time Telegram C2 beacon with victim telemetry
2. Dual-RMM persistence (ScreenConnect + LogMeIn Resolve)

These additions represent a meaningful capability upgrade over prior nodes. Documented by Elastic Security Labs (SILENTCONNECT) and SOCPrime (March 2026 advisory).
