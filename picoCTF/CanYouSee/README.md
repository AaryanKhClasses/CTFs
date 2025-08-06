# CanYouSee
Tags: `easy`, `forensics`

## Problem Statement:
How about some hide and seek?

Download this file [here](https://artifacts.picoctf.net/c_titan/131/unknown.zip).

## My Approach:
1. On downloading the file and unzipping it, we get an image.
2. Open the file in an EXIF viewer and check the metadata for any hidden information.
3. The Attribution URL is `cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==`
4. On decoding the base64 encoded text, we get the flag.

### Flag:
```
picoCTF{ME74D47A_HIDD3N_d8c381fd}
```