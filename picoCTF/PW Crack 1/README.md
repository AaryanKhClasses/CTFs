# PW Crack 1
`easy`, `general skills`, `password_cracking`

## Problem Statement:
Can you crack the password to get the flag?

Download the password checker [here](level1.py) and you'll need the encrypted [flag](level1.flag.txt.enc) in the same directory too.

## My Solution:
1. Download the files `level1.py` and `level1.flag.txt.enc`.
2. Analyze the `level1.py` script to understand how it checks the password.
3. The python file has an if statement to compare the entered password with a hardcoded password. (`if(user_pw == "8713")`)
4. Run the script and enter the password `8713` when prompted.
5. The script will decrypt the flag using the correct password and display it.

### Flag:
```
picoCTF{545h_r1ng1ng_1b2fd683}
```
