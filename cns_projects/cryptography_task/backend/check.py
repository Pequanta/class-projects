import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Pseudo-random key and initialisation vector
key = os.urandom(32)           # (32*8=256-bit. AES also accepts 128/192-bit)
init_vector = os.urandom(16)   # (16*8=128-bit. AES only accepts this size)

# Setup module-specific classes
cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector))
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

# Encrypt and decrypt data
cyphertext = encryptor.update(b"a secret message") + encryptor.finalize()
print(cyphertext)
plaintext = decryptor.update(cyphertext) + decryptor.finalize()