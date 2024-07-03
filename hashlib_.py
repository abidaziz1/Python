import hashlib

data = b'Hello, world!'

# MD5
md5_hash = hashlib.md5()
md5_hash.update(data)
print(f"MD5: {md5_hash.hexdigest()}")

# SHA-1
sha1_hash = hashlib.sha1()
sha1_hash.update(data)
print(f"SHA-1: {sha1_hash.hexdigest()}")

# SHA-256
sha256_hash = hashlib.sha256()
sha256_hash.update(data)
print(f"SHA-256: {sha256_hash.hexdigest()}")

# SHA-512
sha512_hash = hashlib.sha512()
sha512_hash.update(data)
print(f"SHA-512: {sha512_hash.hexdigest()}")

# SHA-3 (256)
sha3_256_hash = hashlib.sha3_256()
sha3_256_hash.update(data)
print(f"SHA-3 256: {sha3_256_hash.hexdigest()}")

# SHAKE 128 (with length 16)
shake_128_hash = hashlib.shake_128()
shake_128_hash.update(data)
print(f"SHAKE 128: {shake_128_hash.hexdigest(16)}")

# SHAKE 256 (with length 32)
shake_256_hash = hashlib.shake_256()
shake_256_hash.update(data)
print(f"SHAKE 256: {shake_256_hash.hexdigest(32)}")

import hmac
key = b'secret_key'
message = b'Hello, world!'
hmac_hash = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"HMAC-SHA-256: {hmac_hash}")
# The hmac module can be used in conjunction with hashlib to create message digests that are keyed, providing an additional layer of security.

shake = hashlib.shake_128()
shake.update(b'Hello, world!')
print(shake.hexdigest(32))  # Producing a 32-byte digest
# SHAKE (Secure Hash Algorithm KECCAK) is a type of hash function that can produce an output of arbitrary length.

# def hash_file(filename):
#     sha256 = hashlib.sha256()
#     with open(filename, 'rb') as f:
#         while chunk := f.read(8192):
#             sha256.update(chunk)
#     return sha256.hexdigest()
# print(hash_file('example.txt'))
# Generate a hash of a file's contents to ensure it has not been tampered with.