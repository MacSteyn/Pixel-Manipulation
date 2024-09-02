Develop a simple image encryption GUI tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

Here’s a simple Python program that uses the Tkinter library for the GUI and the Pillow library for image manipulation. This program will perform a basic pixel manipulation operation (bitwise XOR with a constant value) for encryption and decryption.

In this program, the encrypt_decrypt function performs the encryption or decryption operation on the image. It opens the image, converts it to RGB format, and then performs a bitwise XOR operation on the RGB values of each pixel. The open_image function opens a file dialog for the user to select an image, and then it calls the encrypt_decrypt function with the selected image. The main part of the program creates a simple GUI with a button that calls the open_image function when clicked.

Please note that you need to have the Tkinter and Pillow libraries installed in your Python environment to run this program. You can install them using pip:

pip install tkinter pillow

This is a very basic form of image encryption and is not suitable for securing sensitive data. It’s just for illustrative purposes.

In version two of the updated code after showing the result image, the open_image function opens a save file dialog for the user to select where to save the image. If the user selects a save location, it saves the result image to that location. The asksaveasfilename function automatically adds the “.png” extension to the filename if the user doesn’t specify an extension.

Please refer to the sample encrypted and decrypted image files.
