# The Chimera Project
`cybertea`, `network_forensics`

## Problem Statement
A bio-ethicist was on the verge of a breakthrough... We have a capture of their last data sync, containing what appears to be research imagery of his secret animals. Decode what he meant to say from it.

## My Solution
1. Download the `chimera.pcapng` [file](chimera.pcapng)
2. On running `strings`, we find a variety of different lines, but the ones we are interested in are:
```
CTEA_CTF{th3_p4ck      // Flag Starts!!!
_h4d_s0m3_ups    // go on go on.....`
_4nd_d0wns}  // Flag Complete!!!
```
3. Merging all these three, we get the final flag.

### Flag
```
CTEA_CTF{th3_p4ck_h4d_s0m3_ups_4nd_d0wns}
```
