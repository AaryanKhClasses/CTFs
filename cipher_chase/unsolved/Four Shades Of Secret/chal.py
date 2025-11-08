from Crypto.Util.number import *

with open("flag.txt", "rb") as f:
    FLAG = f.read()

p, q, r, s = [getPrime(1024) for i in range(4)]
N = p*q*r*s
pt = bytes_to_long(FLAG)
ct = pow(pt, 65537, N)
print(f"p = {p}, q = {q}, r = {r}, s = {s}")
print(f"N = {N}")
print(f"shard1 = {7*p + 7*q + 7*r + 7*s + 11}")
print(f"shard2 = {3*(p**2 + q**2 - 2*p - 2*q) + 3*(r**2 + s**2 - 2*r - 2*s)}")
print(f"shard3 = {5*p**3 + 5*q**3 + 5*r**3 + 5*s**3 + 13*p*q*r*s}")
print(f"ciphertext = {ct}")
