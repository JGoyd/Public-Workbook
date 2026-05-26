rule RATtrap_JScript_Dropper_2026 {
    meta:
        description = "RATtrap (RemoteRAT) JScript dropper -- typo fingerprint + C2 strings"
        author      = "Joseph Goydish II"
        date        = "2026-05-25"
        reference   = "REMOTERAT-2026-05"
        mitre       = "T1059.007, T1219, T1071.001"
    strings:
        $typo  = "Inatllation" ascii wide nocase
        $bot   = "Damisky001bot" ascii wide
        $group = "c=Misky" ascii wide
        $msi   = "bremis.ClientSetup.msi" ascii wide
        $host  = "dgs.brimis.org" ascii wide
    condition:
        $typo
        or ($bot and $group)
        or ($msi and $group)
        or (2 of ($host, $msi, $bot))
}
