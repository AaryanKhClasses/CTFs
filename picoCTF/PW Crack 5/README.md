# PW Crack 5
`medium`, `general skills`, `password_cracking`, `hashing`

## Problem Statement:
Can you crack the password to get the flag?

Download the password checker [here](level5.py) and you'll need the encrypted [flag](level5.flag.txt.enc) and the [hash](level5.hash.bin) in the same directory too.

Here's a [dictionary](dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

## My Solution:
1. Download the files `level5.py`, `level5.flag.txt.enc`, `level5.hash.bin` and `dictionary.txt`.
2. Analyze the `level5.py` script to understand how it checks the password.
3. Similar to `PW Crack 4`, the script reads the hash from `level5.hash.bin` and compares it to the MD5 hash of the entered password.
4. Use a [Python script](solution.py) to iterate through each password in `dictionary.txt`, compute its MD5 hash, and compare it to the hash read from `level5.hash.bin`.
5. The script finds the correct password `7e5f`.

### Flag:
```
picoCTF{h45h_sl1ng1ng_40f26f81}
```
