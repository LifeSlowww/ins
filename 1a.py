# shift cipher

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result


def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += ch
    return result


plain = input("Enter Plain Text : ")
key = int(input("Enter Shift Key : "))

cipher = encrypt(plain, key)
print("Encrypted Text :", cipher)

original = decrypt(cipher, key)
print("Decrypted Text :", original)