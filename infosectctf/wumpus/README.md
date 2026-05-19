# wumpus
`infosecctf`, `osint`.

## Problem Statement:
Target Company: discord Resource: `/hypesquad`

Brief: During the transition period before the program's overhaul, the application portal was replaced with a 'program paused' notice.

Task: Recover the administrative contact email listed in the plaintext of that notice.

Flag is of format: `CultRang{XXX@XXX}`

## My Solution:
1. It is very clearly `hypesquad`.
2. On doing wayback machine search on `https://discord.com/hypesquad`, we get the email.

### Flag:
```
CultRang{hypesquad@discordapp.com}
```
