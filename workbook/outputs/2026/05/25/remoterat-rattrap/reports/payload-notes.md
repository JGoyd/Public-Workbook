# RATtrap Payload Notes

## Case: REMOTERAT-2026-05
**Author:** Joseph Goydish II

---

## File Properties

- **Filename:** Business-Invitation.js
- **Type:** JScript (WSH)
- **Served Content-Type:** application/json (spoofed)
- **Delivery:** Dropbox (dl=1 forced download)
- **Cipher:** Custom base64 rotation (85+ decoded strings)

## Execution Phases

1. Decode all strings at runtime using custom base64 rotation cipher
2. Exfiltrate `ComputerName` and `UserName` via Telegram API before any disk write
3. Beacon message: `"Inatllation started"` (misspelled — actor fingerprint)
4. Download `bremis.ClientSetup.msi` from `dgs.brimis.org`
5. Execute: `msiexec /i ... /qn /norestart` (silent, no restart)
6. ScreenConnect registers as group `c=Misky` in attacker console
7. Remove any existing LogMeIn Resolve install
8. Download and install LogMeIn Resolve MSI silently
9. Final Telegram beacon: `"Inatllation complete"` (same typo)

## Actor Fingerprint

The misspelling `Inatllation` appears twice in the decoded payload. Same string, same typo, in both the start and completion Telegram beacon messages. Consistent, not corrected between uses, suggesting a template-embedded string. High-value retrohunt pivot.

## C2 Details

- Bot: `@Damisky001bot` (ID: 8970330885)
- Chat: `6687082236`
- API confirmed HTTP 200 at time of observation
