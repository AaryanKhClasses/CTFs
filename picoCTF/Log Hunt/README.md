# Log Hunt
Tags: `easy`, `general skills`

## Problem Statement:
Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?

Download the [logs](server.log) and figure out the full flag from the fragments.

## My Solution:
1. Download the provided `server.log` file.
2. Open the log file in a text editor to search for fragments of the flag.
3. Search for the term `picoCTF{`, we find `picoCTF{us3_` as the first part
4. Search for `_` to find the next parts: `y0urlinux_`, and `sk1lls_`
5. Finally, search for `}` to find the last part: `cedfa5fb}`
6. Combine all the parts together to form the complete flag.

### Flag:
```
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
```
