import base64

def lfsr(state, mask):
    bit = state & 1
    state >>= 1
    if bit:
        state ^= mask
    return state, bit

def lfsr_stream(state, mask, num_bits):
    stream = []
    for np in range(num_bits):
        state, bit = lfsr(state, mask)
        stream.append(bit)
    return stream

def bits_to_bytes(bits):
    return [int(''.join(str(b) for b in bits[i:i+8]), 2) for i in range(0, len(bits), 8)]

def encrypt(plaintext,initial_state,mask):
    plaintext=plaintext.encode()
    num_bits=8*len(plaintext)
    keystream_bits = lfsr_stream(initial_state, mask, num_bits)
    keystream_bytes = bits_to_bytes(keystream_bits)
    ciphertext_bytes = bytes([p ^ k for p, k in zip(plaintext, keystream_bytes)])
    return base64.b64encode(ciphertext_bytes)

###############
# Output      #
###############

cipher_b64 = "z5Lh8UDCx8+YmVW1K0bTBIqewM5XCmE3dyrWOoRNYo8zc+rZs2402/OvLHzltOJevnSoTvtUSeFkIKaLuSzlwMJpQ6xYVh0oO2GTLWXJ29AWPXjkphNgUZVSaHlvdlVkgbJZttZbZbg="