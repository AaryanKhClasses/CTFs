import struct

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1_glue_padding(msg_len):
    pad = b'\x80'
    pad += b'\x00' * ((56 - (msg_len + 1) % 64) % 64)
    pad += struct.pack('>Q', msg_len * 8)
    return pad

class SHA1:
    def __init__(self, h):
        self.h0, self.h1, self.h2, self.h3, self.h4 = h

    def process(self, chunk):
        w = list(struct.unpack(">16I", chunk))
        for i in range(16, 80):
            w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))

        a, b, c, d, e = self.h0, self.h1, self.h2, self.h3, self.h4

        for i in range(80):
            if i < 20:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

        self.h0 = (self.h0 + a) & 0xffffffff
        self.h1 = (self.h1 + b) & 0xffffffff
        self.h2 = (self.h2 + c) & 0xffffffff
        self.h3 = (self.h3 + d) & 0xffffffff
        self.h4 = (self.h4 + e) & 0xffffffff

    def update(self, data):
        for i in range(0, len(data), 64):
            self.process(data[i:i+64])

    def hexdigest(self):
        return ''.join(f"{x:08x}" for x in (self.h0, self.h1, self.h2, self.h3, self.h4))


# ====== CHALLENGE VALUES ======
old_hash = "b37842c37cdfe100527a8cc92b5f5568f47c72bf"
original = b"test message|admin=False|debug=0|uid=40"
append = b"|admin=True|debug=1"

for key_len in range(8, 33):
    state = tuple(int(old_hash[i:i+8], 16) for i in range(0, 40, 8))
    glue = sha1_glue_padding(key_len + len(original))

    sha = SHA1(state)
    sha.update(append)

    forged = original + glue + append

    print(f"\n[+] key_len = {key_len}")
    print("message hex:", forged.hex())
    print("token:", sha.hexdigest())
