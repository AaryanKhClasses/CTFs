import codecs
import re

with open("hexbook.txt") as f:
    data = f.read()

def fix_char(c):
    if c.upper() in "ABCDEF0123456789 \n":
        return c
    if c.isalpha():
        return codecs.decode(c, "rot_13")
    return c

fixed = "".join(fix_char(c) for c in data)

with open("fixed.hex", "w") as f:
    f.write(fixed)
