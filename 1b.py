# vernam cipher

plain = input("Enter Plain Text: ").upper()
key = input("Enter Key: ").upper()

if len(plain) != len(key):
    print("Error: Plain Text and Key must be of the same length.")
else:
    cipher = ""
    for i in range(len(plain)):
        p = ord(plain[i]) - 65
        k = ord(key[i]) - 65
        c = (p + k) % 26
        cipher += chr(c + 65)

    print("Encrypted Text:", cipher)

    text = ""
    for i in range(len(cipher)):
        c = ord(cipher[i]) - 65
        k = ord(key[i]) - 65
        p = (c - k) % 26
        text += chr(p + 65)

    print("Decrypted Text:", text)