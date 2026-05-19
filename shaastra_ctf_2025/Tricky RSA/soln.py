from sympy import isprime
def rsa_decrypt(ciphertext, d, n):
    """
    Decrypts an RSA ciphertext when n is prime.
    
    Args:
    - ciphertext (int): The encrypted message c = m^e mod n
    - d (int): Private exponent (inverse of e mod (n-1))
    - n (int): Prime modulus
    
    Returns:
    - int: The decrypted plaintext message
    """
    if not isprime(n):
        raise ValueError("This code assumes n is prime.")
    
    return pow(ciphertext, d, n)  # Efficient modular exponentiation

# Helper function to check primality (using sympy for reliability)


# Example usage
n = 148900953097814724338206947679223698832179691968218755697733749707084556942286184505525791780949441847197006147827388400754499224336852575956050210608024912280019773833889546324355353746095214275985515374968532505153145975517881297436944244066461866248895871696012367810254055557824874852294865749524482337551
e = 65537

phi = n - 1
d = pow(e, -1, phi)  # Compute d = e^{-1} mod (n-1)

c = 121076769480411958051494149957748822266761916651856989960685333065892127698252510028422821061257924030569674976010498214466305541374694969727354511840101491547551389611739463068443319789709772210655808254718666561048717294630349889483282304266147748159180993028006648429210247623515263613818295209224052080362
ciphertext = pow(c, e, n)
decrypted = rsa_decrypt(ciphertext, d, n)

print(f"Original message: {c}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted}")