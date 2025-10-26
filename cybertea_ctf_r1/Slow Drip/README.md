# Slow Drip
`cybertea`, `network_forensics`

## Problem Statement
Firewalls are blocking all major protocols, yet a server is still leaking sensitive data. It's not a flood; it's a slow, patient drip. Find the message being smuggled out.

## My Solution
1. Download the `slow_drip.pcapng` [file](slow_drip.pcapng)
2. Open the file in Wireshark.
3. Analyze each packet and concatenate the last 2 characters of each payload.
4. The net result is your final flag.

### Flag
```
CTEA_CTF{g00d_n3tw0rk_f0r3ns1cs_m34ns_ch3cklng_th3_p4yl04d_0f_3v3ry_s1ngl3_p4ck3t}
```
