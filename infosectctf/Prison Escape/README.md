# Prison Escape
`infosecctf`, `forensics`

## Problem Statement:
You find yourself trapped in an island prison. After a daring escape, you reach the seashore—only to be stopped by a sailor who demands a secret code. The key lies hidden in a mysterious painting on the prison’s main building wall. You have a hexbook of some file whose first 13 blocks are ciphered in some way.

The inscription beneath the painting reads: "Samuel Morse hid the flag in an image in an image all in jpg. Some people might know about rot13."

Only a true cybersecurity expert can decipher the hidden flag from these clues.

note: Morse code is a telecommunications method which encodes text characters as standardized sequences of two different signal durations, called dots and dashes. note: To extract embedded image from a steg file use steghide extract command on Linux. passphrase is 123

You may or mayn't need a password, but if needed the password is encoded as Y3Rmb25saW5IMjAyNg==

hexfile: https://infosecctf.cultrang.com/static-files/hexbook.txt

## My Solution:
1. Downloaded the hexfile and see the first few bytes are gibberish.
2. Running a ROT-13 decoder on the file and without affecting any non-hex characters, I got a new hexfile: [fixed.hex](./out/fixed.hex)
3. Converted the fixed hexfile to binary using `xxd -r -p fixed.hex > image.jpg`
4. Opened the [image.jpg](./out/image.jpg) and used steghide with the password `123` to extract the hidden image [paintingsteg.jpg](./out/paintingsteg.jpg).
5. (STUCK)

### Flag:
```

```
