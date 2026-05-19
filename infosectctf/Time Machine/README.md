# Time Machine:
`infosecctf`, `forensics`

## Problem Statement
One day Simon was running to the jungle in the night and accidently he saw a machine but he didn't know how to use it. It was a time machine which accidently caught Simon and travelled him to 100 years back near the Forensic Research Institute (FORRI) at Liverpool John Moores University in the UK. After restless attempt to escape from the era he got to know a key book which contains a special flag which must be used to operate the machine in reverse operation to correct the mistake.

But there is a problem- the key book is encrypted with a three digit password. There is another problem- the key in the key book has the key but in ciphered form. When he was silently searching for some clue inside the institute he got an encrypted audiofile which was one in its kind. Help Simon in analyzing the audiofile. On its cover it was written that the passphrase is 12345678.

Only a cybersecurity expert can use the clues and run the machine to escape from it, because he knows what is ROT13.

- https://infosecctf.cultrang.com/static-files/audiofile.gpg
- https://infosecctf.cultrang.com/static-files/key.txt.gpg

## My Solution:
1. On doing
```
gpg --batch --yes --passphrase "12345678" -o audio.wav -d audiofile.gpg
```
2. We get an audio file, and on reversing and pitching it down, we hear: `!Lov=y0@f0r=v=r`
3. On doing
```
gpg --batch --yes --passphrase "!Lov=y0@f0r=v=r" -o file.txt -d key.txt.gpg
```
4. We get a text file with ROT13 encoded flag: `PhygEnat{Vaqvna_crbcyr}`
5. Decoding it using ROT13 gives the flag: `CultRang{Indian_people}`

### Flag:
```
CultRang{Indian_people}
```
