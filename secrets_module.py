import secrets

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
random_char = secrets.choice(characters)
print(random_char)

random_index = secrets.randbelow(10)  # Random integer from 0 to 9
print(random_index)

random_bits = secrets.randbits(16)  # Random 16-bit integer
print(random_bits)

random_bytes = secrets.token_bytes(16)  # 16 random bytes
print(random_bytes)

random_hex = secrets.token_hex(16)  # 16 random bytes in hex format
print(random_hex)

random_urlsafe = secrets.token_urlsafe(16)  # 16 random bytes in URL-safe base64 format
print(random_urlsafe)