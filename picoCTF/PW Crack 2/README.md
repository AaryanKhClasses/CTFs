# PW Crack 2
`easy`, `general skills`, `password_cracking`

## Problem Statement:
Can you crack the password to get the flag?

Download the password checker [here](level2.py) and you'll need the encrypted [flag](level2.flag.txt.enc) in the same directory too.

## My Solution:
1. Download the files `level2.py` and `level2.flag.txt.enc`.
2. Analyze the `level2.py` script to understand how it checks the password. 
3. The python file has an if statement to compare the entered password with a hardcoded hashed password. (`if(user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65))`)
4. Converting the chr() values to their ASCII characters gives us the password `39ce`.
5. Run the script and enter the password `39ce` when prompted.
6. The script will decrypt the flag using the correct password and display it.

### Flag:
```
picoCTF{tr45h_51ng1ng_502ec42e}
```
