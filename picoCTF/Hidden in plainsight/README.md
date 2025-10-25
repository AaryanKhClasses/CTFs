# Hidden in Plain Sight
`easy`, `forensics`

## Problem Statement:
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

Download the jpg image [here](img.jpg).

## My Solution:
1. Download the provided `img.jpg` file.
2. Open a terminal and use the `file` command to check the file type:
```bash
file img.jpg
```
3. The output indicates that it is a JPEG image, but it may contain hidden data.
```
img.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9", baseline, precision 8, 640x640, components 3
```
4. The comment section contains a base64 encoded string: `c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9`.
5. The decoded string from base64 is `steghide:cEF6endvcmQ=`.
6. This `cEF6endvcmQ=` is another base64 encoded string. Decoding it gives us `pAzzword`.
7. The prefix `steghide:` suggests that the hidden data is embedded using the Steghide tool, and `pAzzword` is likely the password needed to extract it.
8. Use Steghide to extract the hidden data from the image:
```bash
steghide extract -sf img.jpg -p pAzzword
```
9. After running the command, Steghide extracts a file named `flag.txt`.
10. Open the `flag.txt` file to find the hidden flag.

### Flag:
```
picoCTF{h1dd3n_1n_1m4g3_67479645}
```
