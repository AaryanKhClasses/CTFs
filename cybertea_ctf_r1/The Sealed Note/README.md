# The Sealed Note
`cybertea`, `cryptography`

## Problem Statement
A retired archivist handed you a sealed note containing some RSA values and challenged you to recover the secret message inside. Can you do it?

## My Solution
1. Download the `note.txt` [file](note.txt)
2. We see the RSA values: n, e, and c.
3. We can find the p and q values by using `factordb.com`
4. Running the `solution.py` [file](solution.py), we get our flag

### Flag
```
CTEA_CTF{th3_r1v3st_sh4m1r_4dl3m4n_4lg0r1thm_1s_345y}
```
