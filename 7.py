# HMAC-SHA1 signature

import hmac
import hashlib

key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

signature = hmac.new(key, message, hashlib.sha1).hexdigest()

print("HMAC-SHA1 Signature:", signature)