# DISKO 1
Tags: `easy`, `forensics`

## Description:
Can you find the flag in this disk image?

## My Solution:
1. Download the provided file (.gzip)
2. Unzip the file using `gunzip`
3. Do `strings disko-1.dd | grep "picoCTF"` to grep the flag.

### Flag
```
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
```
