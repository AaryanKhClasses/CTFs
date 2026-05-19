# Paw-some Secrets
`cybertea_ctf`, `sanity-check`

## Problem Statement
My meme dogs have something to tell you… but only through their pictures. Can you figure out what they’re trying to say?

## My Solution
1. Extract the [challenge_files.zip](challenge_files.zip) file.
2. Use `exiftool` on each of the image files and look for the flag parts in the metadata.
3. Combine the flag parts to get the final flag.

### Flag
```
CTEA_CTF{1_r34lly_l0v3_t0_s33_y0u_guy5_ch3ck_th3_m3t4d4t4_0f_th3_p1ctur35_0f_my_cut3_4nd_h1l4r10u5_d0gg05_f1n4lly_th3_fl4g_end5}
```
