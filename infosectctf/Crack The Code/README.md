# Crack the Code
`infosecctf`, `reverse`

## Problem Statement
find the flag which was encrypted using this code

**Attachments:** [q2.cpp](q2.cpp) and [q2_enc.txt](q2_enc.txt)

## My Solution:
1. Fix the given **C** file to **C++** and fix all the errors (commas and semicolons).
2. Compiling and running the code changes the integer matrix [q2_enc.txt](q2_enc.txt) file to a new floating-point matrix [q2_enc.txt](./out/q2_enc.txt) file.
3. Every value in the integer matrix is even
4. Dividing all values by 2 yields printable ASCII values
5. The characters reads in column-wise order gives the flag.
```
67 117 108 116 → C u l t
82 97 110 103 → R a n g
123 119 105 110 → { w i n
110 101 114 125 → n e r }
```

### Flag:
```
CultRang{winner}
```
