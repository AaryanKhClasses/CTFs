# Secret of The Polyglot
Tags: `easy`, `forensics`, `polyglot`, `file_format`

## Problem Statement:
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/8/flag2of2-final.pdf).

## My Approach:
1. On downloading the pdf file, it contains the words "pn9_&_pdf" which hints we could change the file extension to a ".png"
2. On changing the file extension to ".png", we get the text "picoCTF{f1u3n7_"
3. The rest of the flag is inside the pdf itself ("1n_pn9_&_pdf_249d05c0}")

### Flag:
```
picoCTF{f1u3n7_1n_pn9_&_pdf_249d05c0}
```
