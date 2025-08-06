# heap 1
Tags: `medium`, `binary exploitation`, `heap`

## Problem Statement:
Can you control your overflow?

Download the binary [here](./chall).

Download the source [here](./chall.c).

Additional details will be available after launching your challenge instance.

## My Solution:
1. On analyzing the source code, it was evidant that the safe_var needs to be equal to "pico" in order for the flag to print.
2. On some testing, and running the binary locally, and running option "2" for writing to buffer, it was found that we needed to write the word "pico" 9 times using that option in order to change the safe_var.
3. On running option "3", for printing the safe_var, we can see that it is successfully replaced!
4. On running option "4" finally to print the flag, the flag was found!

### Flag:
```
picoCTF{starting_to_get_the_hang_c588b8a1}
```