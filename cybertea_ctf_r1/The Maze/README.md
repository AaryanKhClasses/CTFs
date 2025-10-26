# The Maze
`cybertea`, `cryptography`

## Problem Statement
You've been given a file containing encoded data. This is just the entrance to the path. Decoding it only pulls you deeper into the maze, where the core message is still scrambled by an old cipher. To bring order to the chaos, you must find the correct key and you'll need to go crazy for it!

## My Solution
1. Download the `sane.txt` [file](sane.txt)
2. The file contains the text: `RUtFWl9BVld7eTB0X2F0NHRrM2NfcmozX21pZmwzdDN9`
3. On decoding it using Base64, we get: `EKEZ_AVW{y0t_at4tk3c_rj3_mifl3t3}`
4. We know that the flag starts with `CTEA_CTF`
5. Calculating the shifts, we get to know that the key is `CRAZY` for a Vigenère cipher.
6. On applying the Vigenère cipher decryption with the key `CRAZY`, we get the final flag.

### Flag
```
CTEA_CTF{y0u_cr4ck3d_th3_vign3r3}
```
