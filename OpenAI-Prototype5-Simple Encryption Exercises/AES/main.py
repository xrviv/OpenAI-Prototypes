#OpenAIGPT3 Assisted Code

from Cryptodome.Cipher import AES
import base64
import os
from Cryptodome.Util.Padding import pad, unpad

# Get user input
os.system('clear')
print()
print("============================")
plaintext = input("Enter the text to be encrypted: ").encode()
print("============================")
print()

# AES encryption
key = b'abcdefghijklmnop' # use your own secret key
iv = b'abcdefghijklmnop' # use your own random IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the plaintext
padded_plaintext = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_plaintext)

# Encode the ciphertext in base64
encoded_ciphertext = base64.b64encode(ciphertext)

# Display the encoded ciphertext
os.system('clear')
print()
print("============================")
print("Encrypted text: ", encoded_ciphertext)
print("============================")