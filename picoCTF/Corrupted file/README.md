# Corrupted File
`easy`, `forenciscs`

## Problem Statement
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

Download the file [here](file).

## My Solution
1. Download the corrupted file.
2. On performing file check, it shows `file: data`, indicating it is unrecognized.
3. Open the file in a hex editor (like `hexedit` or `xxd`) to inspect its contents. The header says `JFIF`, which indicates it is a JPEG file.
4. JPEG files typically start with the bytes `FF D8 FF E0` followed by `00 10 4A 46 49 46 00 01`. The corrupted file starts with a `5C 78 FF E0` instead, indicating the first few bytes are missing or altered.
5. Replace the incorrect starting bytes with the correct JPEG header bytes.
6. Save the modified file.
7. Now copying the same file to a new file and renaming it with a `.jpg` extension.
8. Opening the new file reveals the hidden flag.

### Flag
```
picoCTF{r3st0r1ng_th3_by73s_0e8fb0ec}
```
