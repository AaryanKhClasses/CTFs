# The Next Stop
`cybertea`, `cryptography`

## Problem Statement
An encrypted file containing a secret message was left on a university server by a number-theory professor. Along with that he also gave a note that was mentioning some kind of weird sequence.

The information you decode from the note is just a waypoint, but one of its fingerprints might help you to decrypt what he left behind

## My Solution
1. Download the `enc_file.txt` [file](enc_file.txt) and the `seq_note.txt` [file](seq_note.txt).
2. The `enc_file.txt` contains: `2237212269756d774d44064c0855075a106c5744036e56514555010d5711040d061e`
3. The `seq_note.txt` contains:
```
"Do you think you are clever enough to read what I left for you in the note ?"

"If yes, then below is what i left for you"

"Irdrelare'j eldsvi zj kyv jvtfeu ze kyzj jvhlvetv. Kyv kyziu nrj wfleu ze 1957. Kyv wfliky — kyv fev Z jflxyk — ivhlzivu yvrmzvi tfdglkv reu nrj ivmvrcvu ze 1991 reu kyrk dzxyk sv kyv fev kyrk tre yvcg pfl"
```
4. On parsing the `seq_note.txt` contents in a Caesar cipher with a shift of 17, we get:
```
Ramanujan's number is the second in this sequence. The third was found in 1957. The fourth -- the one I sought -- required heavier compute and was revealed in 1991 and that might be the one that can help you
```
5. The sequence is: `2`, `1729`, `87539319`, `6963472309248`, ...
6. The fourth number is `6963472309248`.
7. Convert the hex ciphertext to bytes.
8. Take the decimal number `6963472309248`, compute its MD5 hex digest:
```py
md5("6963472309248") = acdc66916024a638c366010e660cce5c.
```
9. Use that MD5 hex (as ASCII) as a repeating XOR key against the ciphertext bytes.
10. XOR -> plaintext to get the flag.

### Flag
```
CTEA_CTF{t4xic4bs_ar3_f4sc1n4t1ng}
```
