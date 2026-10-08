# vigenere cipher

def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

            key_index += 1
        else:
            result += ch

    return result


def decrypt(cipher, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in cipher:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

            key_index += 1
        else:
            result += ch

    return result


text = input("Enter Plain Text: ")
key = input("Enter Key: ")

cipher = encrypt(text, key)
print("Encrypted Text:", cipher)

plain = decrypt(cipher, key)
print("Decrypted Text:", plain)