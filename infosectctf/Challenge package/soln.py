#!/usr/bin/env python3
# CultRang VM License Auto-Solver (ROBUST VERSION)

TARGET = 0x7E4A8C9F

def ror(x, r):
    return ((x >> r) | (x << (32 - r))) & 0xffffffff

def djb2(data):
    h = 0
    for b in data:
        h = ((h << 5) + h + b) & 0xffffffff
    return h

# Hidden keys from binary
hidden = [
    0x13376942,
    0xDEADBEEF,
    0xCAFEBABE,
    0x8BADF00D
]

# ── Step 1: Invert the VM ──────────────────────────────
chunks = []
for h in hidden:
    out = h ^ 0x42424242
    x = (out - 0x1342) & 0xffffffff
    x = ror(x, 7)
    x ^= 0xEFBEADDE
    chunks.append(x)

# ── Step 2: Build base key ─────────────────────────────
key = bytearray(32)

for i, c in enumerate(chunks):
    off = i * 8
    key[off:off+4] = b'AAAA'                # free bytes
    key[off+4:off+8] = c.to_bytes(4, 'big') # VM-fixed

# ── Step 3: Brute-force last 3 bytes (fast & safe) ────
print("[*] Fixing DJB2 checksum...")

base = key[:-3]

found = False
for b1 in range(256):
    for b2 in range(256):
        for b3 in range(256):
            key = base + bytes([b1, b2, b3])
            if djb2(key) == TARGET:
                found = True
                break
        if found: break
    if found: break

if not found:
    raise RuntimeError("No valid key found (unexpected)")

license_key = key.decode('latin1')

print("[+] Valid license key found!")
print(license_key)
print()
print(f"Flag: CultRang{{{license_key}}}")
