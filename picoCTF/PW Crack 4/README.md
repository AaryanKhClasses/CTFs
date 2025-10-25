# PW Crack 4
`medium`, `general skills`, `password_cracking`, `hashing`

## Problem Statement:
Can you crack the password to get the flag?

Download the password checker [here](level4.py) and you'll need the encrypted [flag](level4.flag.txt.enc) and the [hash](level4.hash.bin) in the same directory too.

There are 100 potential passwords with 1 being correct. You can find these by examining the password checker script.

## My Solution:
1. Download the files `level4.py`, `level4.flag.txt.enc`, and `level4.hash.bin`.
2. Analyze the `level4.py` script to understand how it checks the password.
3. It has a `hash_pw()` function that takes user input and checks it with the contents of the `level4.hash.bin` file.
4. The function uses the MD5 hashing algorithm to hash the input password.
5. We can create another [python file](solution.py) to iterate through all potential passwords and run the level4.py script to find the correct one.
6. The correct password is found to be `9f63`.

### Flag:
```
picoCTF{fl45h_5pr1ng1ng_d770d48c}
```
