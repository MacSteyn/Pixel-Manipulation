from PIL import Image
import numpy as np

def encrypt_image(image_path, key_path):
    # Open the image
    img = Image.open(image_path)
    
    # Ensure image is in RGB mode for consistent processing
    img = img.convert('RGB')

    # Convert the image to a NumPy array
    img_array = np.array(img, dtype=np.uint8)

    # Generate a random key of the same shape as img_array
    key = np.random.randint(0, 190, img_array.shape, dtype=np.uint8)

    # Save the key for decryption
    np.save(key_path, key)

    # Encrypt each pixel using XOR with the key
    encrypted_array = np.bitwise_xor(img_array, key)

    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array, 'RGB')

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully. Encrypted image saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key_path):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)

    # Ensure image is in RGB mode for consistent processing
    encrypted_img = encrypted_img.convert('RGB')

    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)

    # Load the key for decryption
    key = np.load(key_path)

    # Decrypt each pixel using XOR with the key
    decrypted_array = np.bitwise_xor(encrypted_array, key)

    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array, 'RGB')

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully. Decrypted image saved as 'decrypted_image.png'.")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    # Prompt user for the image path
    image_path = input("Enter the path to the image file: ").strip().strip('"').strip("'")
    
    # Define a path to save the encryption key
    key_path = "encryption_key.npy"

    # Encrypt the image
    encrypt_image(image_path, key_path)
    
    # Decrypt the image
    decrypt_image("encrypted_image.png", key_path)

if __name__ == "__main__":
    main()
    
