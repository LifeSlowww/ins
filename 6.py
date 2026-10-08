# diffe-hellman key exchange

p = int(input("Enter a prime number(p): "))
g = int(input("Enter primitive root(g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

print("\nAlice's Public Key:", A)
print("Bob's Public Key:", B)

alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print("\nSecret Key calculated by Alice:", alice_secret)
print("Secret Key calculated by Bob:", bob_secret)

if alice_secret == bob_secret:
    print("\nKey Exchange Successful!")
    print("Shared Secret Key:", alice_secret)
else:
    print("\nKey Exchange Failed!")