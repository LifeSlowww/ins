# rail fence cipher

def encrypt(pt):
    ct = ""

    for i in range(0, len(pt), 2):
        ct += pt[i]

    for i in range(1, len(pt), 2):
        ct += pt[i]

    return ct


def decrypt(ct):
    pt = ""
    mid = (len(ct) + 1) // 2
    row1 = ct[:mid]
    row2 = ct[mid:]

    i = 0
    j = 0

    for k in range(len(ct)):
        if k % 2 == 0:
            pt += row1[i]
            i += 1
        else:
            pt += row2[j]
            j += 1

    return pt


pt = input("Enter Plain Text: ")
ct = encrypt(pt)
msg = decrypt(ct)

print("Encrypted Text :", ct)
print("Decrypted Text :", msg)