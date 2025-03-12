import itertools

ciphertext = "Hjg_KiFTyVaO_KvMcYHoYg_fReIoHi"
key = "BLACKBEARD"

def shift_back(text, shift):
    """Shifts each letter in the text back by the given shift amount."""
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char  # Keep non-alphabet characters unchanged
    return decrypted_text

def vigenere_decrypt(ciphertext, key):
    """Decrypts a Vigenère cipher with the given key."""
    decrypted_text = []
    key_cycle = itertools.cycle(key)  # Repeat key cyclically

    for char in ciphertext:
        if char.isalpha():  # Only decrypt letters
            shift = ord(next(key_cycle).upper()) - ord('A')  # Determine shift from key
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            decrypted_text.append(char)  # Keep non-alphabet characters unchanged

    return ''.join(decrypted_text)

# Step 1: Apply Vigenère decryption
vigenere_decrypted_text = vigenere_decrypt(ciphertext, key)

# Step 2: Shift back by 10
final_decrypted_text = shift_back(vigenere_decrypted_text, 10)
print(final_decrypted_text)
