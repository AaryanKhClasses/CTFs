# Math Class!
`cybertea_ctf`, `reverse-engineering`

## Problem Statement
Welcome back to class. I hope you've been practicing your arithmetic, because this looks all too familiar.

I'm sure you'll find it... anahtar

Note: The file is new_math_challenge.

## My Solution
1. Download the [new_math_challenge](new_math_challenge) file.
2. Open the file in IDA and analyze the disassembly.
3. It requires 5 "keys" to unlock the flag.
4. On reverse engineering the functions, we find the keys are:
    - Key 1: 111111
    - Key 2: 222222
    - Key 3: 1010101010101010
    - Key 4: 3125243
    - Key 5: 16045690984503103501
5. On successfully entering all the inputs, we get the message.
```
Congrats! To decode the flag, please run the following:
python -c "a=243237381834590518071609223864384240257673166403958029694992324224715727185283769521219; print(a.to_bytes(36, 'little'))"
```

### Flag
```
CTEA_CTF{w31c0m3_b4cK_t0_m4th_cl455}
```
