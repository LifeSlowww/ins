# DES algorithm

# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)

cipher = DES.new(key, DES.MODE_ECB)

plaintext = input("Enter message: ")

encrypted = cipher.encrypt(
    pad(plaintext.encode(), DES.block_size)
)

print("Encrypted Text:", encrypted.hex())

decipher = DES.new(key, DES.MODE_ECB)

decrypted = unpad(
    decipher.decrypt(encrypted),
    DES.block_size
)

print("Decrypted Text:", decrypted.decode())