# The Invisible Labyrinth
`cybertea`, `miscellaneous`

## Problem Statement
We recovered a corrupted archive. It appears empty, but it's a digital labyrinth of thousands of invisible files and directories. Standard tools will fail.

Your mission: Find your way through the chaos to find the one hidden message.

## My Solution
1. Extract the `The_Invisible_Labyrinth.zip` [archive](The_Invisible_Labyrinth.zip).
2. We know the starting part is `CTEA_CTF{`, so converting it into base64, we get `Q1RFQV9DVEZ7`.
3. On searching this globally string on VSCode, we find a singular instance of the string in a hidden file.
```
Q1RFQV9DVEZ7ZDMzcF9kMXZlXzFudDBfdGgzX3YwMWRfPGNoYXJhY3Rlcl9jb3VudD59
```
4. On decoding this base64 string, we reveal the hidden message.
```
CTEA_CTF{d33p_d1ve_1nt0_th3_v01d_<character_count>}
```
5. As the character count of the base64 string is 51, we put that in the place.

### Flag
```
CTEA_CTF{d33p_d1ve_1nt0_th3_v01d_51}
```
