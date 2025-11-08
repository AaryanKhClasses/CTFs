# Py-Safe
`cipher_chase`, `reverse-engineering`

## Problem Statement
Can you help me open the safe? I think I've lost my password.

**Attachment:** [safe.py](safe.py)

## My Solution
1. Running the [solver.py](solver.py) script gives the flag.
```
Target CRC16: 1872
Target CRC8:  181
Starting deterministic brute force (lengths 1..5) ...
 Trying length = 1
 Trying length = 2
 Trying length = 3
 Trying length = 4
 Trying length = 5
Collision found (deterministic): bgbEL
Time: 52.13321304321289
```

### Flag
```
ZenseCTF{bgbEL}
```
