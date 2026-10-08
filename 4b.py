# AES algorithm

# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

print("Generated Key (Hex):", key.hex())

cipher = AES.new(key, AES.MODE_ECB)

plaintext = input("Enter message: ")

encrypted = cipher.encrypt(
    pad(plaintext.encode(), AES.block_size)
)

print("Encrypted (Hex):", encrypted.hex())

decipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(
    decipher.decrypt(encrypted),
    AES.block_size
)

print("Decrypted Text:", decrypted.decode())