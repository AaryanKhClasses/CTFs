# Never Gonna Give You Up
`cybertea`, `steganography`

## Problem Statement
*You know the rules, and so do I. Give a simple scan a try. I'm never gonna give you the flag up that easily, I'm never gonna just let you down, I'm not going to run around and desert you.*

*The path forward isn't in the link you get, but inside the image where the promise is kept. Find the hidden message, don't say goodbye. Piece it together, and don't you dare cry ;)*

## My Solution
1. Download the `stego_chall3nge.png` [image file](stego_chall3nge.png)
2. On running `zsteg` on the image, we find a text:
```
aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2RyaXZlL2ZvbGRlcnMvMWM2T0JZUktPUGZCYXpmQUFLckxrajVWUGhxeXJnOTlLP3VzcD1zaGFyaW5n
```
3. Decoding the Base64 string gives us:
```
https://drive.google.com/drive/folders/1c6OBYRKOPfBazfAAKrLkj5VPhqyrg99K?usp=sharing
```
4. This google drive folder contains 4 images, located [here](qr_codes/)
5. On merging these 4 images, we find the final qr code [here](final.png)
6. The final QR Code gives the flag.

### Flag
```
CTEA_CTF{y0u_just_g0t_r1ckr0ll3d}
```
