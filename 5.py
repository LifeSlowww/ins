# RSA algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = 61
q = 53

n = p * q

phi = (p - 1) * (q - 1)

e = 17

if gcd(e, phi) != 1:
    print("Invalid value of e")
    exit()

d = mod_inverse(e, phi)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi(n) =", phi)

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

message = int(input("\nEnter message (number less than n): "))

ciphertext = pow(message, e, n)

print("Encrypted message:", ciphertext)

decrypted_message = pow(ciphertext, d, n)

print("Decrypted message:", decrypted_message)