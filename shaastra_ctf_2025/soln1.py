import base64

# --- Functions from the original code (unchanged) ---
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

# --- Decryption Function ---
def decrypt(cipher_b64, initial_state, mask):
    # 1. Base64 Decode
    ciphertext_bytes = base64.b64decode(cipher_b64)
    
    # Calculate required bits based on decoded ciphertext length
    num_bits = 8 * len(ciphertext_bytes)
    
    # 2. Generate Key Stream
    keystream_bits = lfsr_stream(initial_state, mask, num_bits)
    keystream_bytes = bits_to_bytes(keystream_bits)
    
    # 3. XOR Decryption (P = C XOR K)
    plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext_bytes, keystream_bytes)])
    
    # Return as a decoded string
    return plaintext_bytes.decode()

# ... [Keep your original lfsr, lfsr_stream, bits_to_bytes functions] ...
import base64

# ... [Keep your original decrypt function] ...
def decrypt(cipher_b64, initial_state, mask):
    ciphertext_bytes = base64.b64decode(cipher_b64)
    num_bits = 8 * len(ciphertext_bytes)
    keystream_bits = lfsr_stream(initial_state, mask, num_bits)
    keystream_bytes = bits_to_bytes(keystream_bits)
    plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext_bytes, keystream_bytes)])
    return plaintext_bytes

# --- Execution ---
cipher_b64 = "z5Lh8UDCx8+YmVW1K0bTBIqewM5XCmE3dyrWOoRNYo8zc+rZs2402/OvLHzltOJevnSoTvtUSeFkIKaLuSzlwMJpQ6xYVh0oO2GTLWXJ29AWPXjkphNgUZVSaHlvdlVkgbJZttZbZbg="

# Keep the common mask
mask = 0x80000057

# Brute-force the initial state
print("Starting brute-force...")
for initial_state_guess in range(1, 10000000): # Start from 1, checking up to 10 million states
    try:
        decrypted_bytes = decrypt(cipher_b64, initial_state_guess, mask)
        
        # Try to decode the result. If it fails, the 'except' block catches it.
        # This is a good way to check for printable ASCII/UTF-8 text.
        plaintext = decrypted_bytes.decode('utf-8')
        
        # Check if the decrypted text looks like a flag
        if "Shaastra" in plaintext or "SHAASTRA" in plaintext or decrypted_bytes[0] in range(32, 127):
            print("--- SUCCESS ---")
            print(f"Initial State Found: {initial_state_guess}")
            print(f"Deciphered Text: {plaintext}")
            break
            
    except UnicodeDecodeError:
        # Expected error if the key is wrong. Continue to the next state.
        continue

print("Brute-force finished.")

# --- Execution ---
cipher_b64 = "z5Lh8UDCx8+YmVW1K0bTBIqewM5XCmE3dyrWOoRNYo8zc+rZs2402/OvLHzltOJevnSoTvtUSeFkIKaLuSzlwMJpQ6xYVh0oO2GTLWXJ29AWPXjkphNgUZVSaHlvdlVkgbJZttZbZbg="

# Assumed Key Parameters (Initial State and Mask)
initial_state = 1
mask = 0x80000057 # Common 32-bit LFSR tap mask

# decrypted_text = decrypt(cipher_b64, initial_state, mask)

# print(f"Deciphered Text: {decrypted_text}")