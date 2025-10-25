# PW Crack 3
`medium`, `general skills`, `password_cracking`, `hashing`

## Problem Statement:
Can you crack the password to get the flag?

Download the password checker [here](level3.py) and you'll need the encrypted [flag](level3.flag.txt.enc) and the [hash](level3.hash.bin) in the same directory too.

There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## My Solution:
1. Download the files `level3.py`, `level3.flag.txt.enc`, and `level3.hash.bin`.
2. Analyze the `level3.py` script to understand how it checks the password.
3. The end of the python file has an array of all potential passwords:
```python
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```
4. Running the python file and trying each password, we find that the correct password is `2295`.
5. On entering this password, the flag is outputed.

### Flag:
```
picoCTF{m45h_fl1ng1ng_6f98a49f}
```
