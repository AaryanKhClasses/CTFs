import numpy as np
from PIL import Image
import itertools
import string

# Load the image
im = Image.open('starry_night_stego.png')  # Adjust filename if needed (the uploaded image)
img = np.array(im)
height, width = img.shape[:2]

if img.ndim == 3 and img.shape[2] >= 3:
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    has_alpha = (img.shape[2] == 4)
    a = img[:,:,3] if has_alpha else None
else:
    print("Image lacks RGB channels!")
    exit()

# Define possible scan orders (row-major, column-major, diagonal, etc.)
def get_pixels(order='row'):
    coords = []
    if order == 'row':
        for y in range(height):
            for x in range(width):
                coords.append((y, x))
    elif order == 'col':
        for x in range(width):
            for y in range(height):
                coords.append((y, x))
    elif order == 'rev_row':
        for y in range(height-1, -1, -1):
            for x in range(width-1, -1, -1):
                coords.append((y, x))
    elif order == 'hilbert':  # Skip complex Hilbert for speed; add if needed
        pass
    return coords

scan_orders = ['row', 'col', 'rev_row']

# Channels combinations: which channels to use (R,G,B,A?)
channel_sets = [
    ('R',), ('G',), ('B',), ('A',) if has_alpha else None,
    ('R','G'), ('R','B'), ('G','B'), ('R','G','B'),
    ('R','G','B','A') if has_alpha else None
]
channel_sets = [c for c in channel_sets if c]  # Filter None

# Permutations of channel order for multi-channel
def get_permutations(chs):
    return list(itertools.permutations(chs)) if len(chs) > 1 else [(chs[0],)]

# Masks: all pixels vs only where channels "struggle" (not all equal)
masks = {
    'all': np.ones((height, width), bool),
    'struggle_rgb': (r != g) | (r != b) | (g != b),
    'struggle_any': np.ones((height, width), bool),  # Placeholder
}
if has_alpha:
    masks['struggle_rgba'] = (r != g) | (r != b) | (r != a) | (g != b) | (g != a) | (b != a)

# Bit extraction modes: LSB, MSB, bit1, bit2, etc. (0=LSB, 7=MSB)
bit_positions = range(8)

# Reverse bitstream? Yes/No
reverses = [False, True]

# Possible message lengths to try (bytes)
max_bytes = 200

print("Starting bruteforce... this may take a while (thousands of combinations)")

found = False
for scan in scan_orders:
    coords = get_pixels(scan)
    
    for ch_set in channel_sets:
        perms = get_permutations(ch_set)
        
        for perm in perms:
            chan_map = {'R': r, 'G': g, 'B': b, 'A': a}
            channels = [chan_map[c] for c in perm]
            
            for mask_name, mask in masks.items():
                for bit_pos in bit_positions:
                    for rev in reverses:
                        # Extract bits
                        bits = []
                        for y, x in coords:
                            if not mask[y, x]:
                                continue
                            for chan in channels:
                                val = chan[y, x]
                                bit = (val >> bit_pos) & 1
                                bits.append(bit)
                        
                        if not bits:
                            continue
                        
                        if rev:
                            bits = bits[::-1]
                        
                        # Pack to bytes
                        bit_array = np.array(bits, dtype=np.uint8)
                        padding = (8 - len(bit_array) % 8) % 8
                        bit_array = np.pad(bit_array, (0, padding), constant_values=0)
                        bytes_data = np.packbits(bit_array).tobytes()
                        
                        # Try to decode as ASCII, look for flag patterns
                        try:
                            text = bytes_data.decode('ascii', errors='ignore')
                        except:
                            text = str(bytes_data)
                        
                        # Look for common flag formats
                        flags = []
                        if 'CTEA_CTF{' in text.lower():
                            flags.append(text[text.lower().index('CTEA_CTF{'):].split('}')[0] + '}')
                        if any(c in text for c in string.printable) and len(text) > 20:
                            if any(word in text.lower() for word in ['secret', 'van', 'gogh', 'truth', 'deathbed']):
                                flags.append(text[:100])
                        
                        for f in flags:
                            print("\n" + "="*60)
                            print(f"POSSIBLE FLAG FOUND!")
                            print(f"Scan: {scan}, Channels: {perm}, Mask: {mask_name}, Bit: {bit_pos}, Reverse: {rev}")
                            print(f"Flag: {f}")
                            print("="*60)
                            found = True
                        
                        # Optional: print clean ASCII if long enough
                        clean = ''.join(c for c in text[:max_bytes] if c in string.printable)
                        if len(clean) > 30 and clean.isalpha():
                            print(f"Clean text: {clean[:200]}")
                            print(f"Config -> scan:{scan} ch:{perm} mask:{mask_name} bit:{bit_pos} rev:{rev}")

if not found:
    print("No obvious flag found. Try narrowing or adding more heuristics.")
else:
    print("Bruteforce complete. Check above for candidates!")