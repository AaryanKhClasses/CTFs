# Riddle Registry
`easy`, `forensics`

## Problem Statement:
Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.

Find the PDF file here [Hidden Confidential Document](confidential.pdf) and uncover the flag within the metadata.

## My Solution:
1. Download the provided `confidential.pdf` file.
2. On running exiftool on the PDF file, we can see various metadata fields.
```bash
exiftool confidential.pdf
```
3. The author field contains a base64 encoded string:
```
cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV80MjQ0MGM3ZH0=
```
4. On decoding the base64 string, we get the flag:

### Flag:
```
picoCTF{puzzl3d_m3tadata_f0und!_42440c7d}
```
