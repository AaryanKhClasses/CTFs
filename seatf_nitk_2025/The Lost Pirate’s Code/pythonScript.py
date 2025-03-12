from PIL import Image
import numpy as np

def reverse_n_pixels(image_path, n):
    image = Image.open(image_path).convert('L') 
    img_array = np.array(image)
    img_array_flat = img_array.flatten()
    for i in range(0, len(img_array_flat), n):
        img_array_flat[i:i + n] = img_array_flat[i:i + n][::-1]
    reversed_img_array = img_array_flat.reshape(img_array.shape)
    reversed_image = Image.fromarray(reversed_img_array.astype(np.uint8))
    return reversed_image

image_path = ?  
mississippis = ?  
reversed_image = reverse_n_pixels(image_path, n)

reversed_image.show()
reversed_image.save('new_image.png')

# The image you see is a distorted QR code, where various shades of black are used, creating a scribbled effect.
# Not all black areas are identical.
# THINK...
