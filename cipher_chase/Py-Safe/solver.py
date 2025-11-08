from itertools import product
import random
import string
import time

def crc16(s: str) -> int:
    val = 65535
    for ch in s:
        val ^= ord(ch)
        for _ in range(8):
            if val & 1:
                val = (val >> 1) ^ 40961
            else:
                val >>= 1
    return val & 65535

table = [0, 7, 14, 9, 28, 27, 18, 21, 56, 63, 54, 49, 36, 35, 42, 45, 112, 119, 126, 121, 108, 107, 98, 101, 72, 79, 70, 65, 84, 83, 90, 93, 224, 231, 238, 233, 252, 251, 242, 245, 216, 223, 214, 209, 196, 195, 202, 205, 144, 151, 158, 153, 140, 139, 130, 133, 168, 175, 166, 161, 180, 179, 186, 189, 199, 192, 201, 206, 219, 220, 213, 210, 255, 248, 241, 246, 227, 228, 237, 234, 183, 176, 185, 190, 171, 172, 165, 162, 143, 136, 129, 134, 147, 148, 157, 154, 39, 32, 41, 46, 59, 60, 53, 50, 31, 24, 17, 22, 3, 4, 13, 10, 87, 80, 89, 94, 75, 76, 69, 66, 111, 104, 97, 102, 115, 116, 125, 122, 137, 142, 135, 128, 149, 146, 155, 156, 177, 182, 191, 184, 173, 170, 163, 164, 249, 254, 247, 240, 229, 226, 235, 236, 193, 198, 207, 200, 221, 218, 211, 212, 105, 110, 103, 96, 117, 114, 123, 124, 81, 86, 95, 88, 77, 74, 67, 68, 25, 30, 23, 16, 5, 2, 11, 12, 33, 38, 47, 40, 61, 58, 51, 52, 78, 73, 64, 71, 82, 85, 92, 91, 118, 113, 120, 127, 106, 109, 100, 99, 62, 57, 48, 55, 34, 37, 44, 43, 6, 1, 8, 15, 26, 29, 20, 19, 174, 169, 160, 167, 178, 181, 188, 187, 150, 145, 152, 159, 138, 141, 132, 131, 222, 217, 208, 215, 194, 197, 204, 203, 230, 225, 232, 239, 250, 253, 244, 243]

def crc8(s: str) -> int:
    val = 0
    for ch in s:
        val = table[(val ^ ord(ch)) & 255]
    return val & 255

# Known password from challenge
target = "JustAn0th3rPassw0rd"
t16 = crc16(target)
t8 = crc8(target)
print("Target CRC16:", t16)
print("Target CRC8: ", t8)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
start = time.time()
print("Starting deterministic brute force (lengths 1..5) ...")
found = None
for L in range(1, 6):
    print(" Trying length =", L)
    for tup in product(chars, repeat=L):
        s = "".join(tup)
        if s == target:
            continue
        if crc16(s) == t16 and crc8(s) == t8:
            found = s
            break
    if found:
        break

if found:
    print("Collision found (deterministic):", found)
    print("Time:", time.time() - start)
    raise SystemExit(0)

print("No collision in lengths 1..5. Starting randomized search (length 6..10).")
random.seed(0)
chars_rand = string.ascii_letters + string.digits + "!@#$%^&*()_+"
tries = 0
start2 = time.time()
while tries < 2000000:
    tries += 1
    L = random.randint(6, 10)
    s = ''.join(random.choice(chars_rand) for _ in range(L))
    if s == target:
        continue
    if crc16(s) == t16 and crc8(s) == t8:
        found = s
        break
    if tries % 100000 == 0:
        print(" Random tries:", tries, "elapsed:", int(time.time() - start2), "s")

if found:
    print("Collision found (random):", found)
    print("Total tries:", tries)
    print("Time:", time.time() - start2)
else:
    print("No collision found within the attempted search limits.")
