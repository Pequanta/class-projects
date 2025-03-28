import string
import os
import base64


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
"""
    The following class is credited to @albohlabs(github). Since it is not customary to use otp in encryption-decryption(as it depends in the generation of truly random number)
    , the implementation doesn't entail standard library.
"""
    
class OneTimePadCrypto:
    def __init__(self):
        self.lst_ascii = string.ascii_lowercase
        self.one_time_pad = list(self.lst_ascii)
    def encrypt(self, msg: str, key: str):
        ciphertext = ''
        for idx, char in enumerate(msg):
            charIdx = self.lst_ascii.index(char)
            keyIdx = self.one_time_pad.index(key[idx])

            cipher = (keyIdx + charIdx) % len(self.one_time_pad)
            ciphertext +=  self.lst_ascii[cipher]

        return ciphertext

    def decrypt(self, ciphertext: str, key:str):
        if ciphertext == '' or key == '':
            return ''

        charIdx =  self.lst_ascii.index(ciphertext[0])
        keyIdx = self.one_time_pad.index(key[0])

        cipher = (charIdx - keyIdx) % len(self.one_time_pad)
        char =  self.lst_ascii[cipher]

        return char + self.decrypt(ciphertext[1:], key[1:])
    
class ThreeDESCrypto:
    def __init__(self):
        # Empty constructor since we don't need to initialize with message and key
        pass
    
    def encrypt(self, message: str, key: str) -> str:
        # Convert inputs to bytes
        message_bytes = bytes(message, "utf-8")
        key_bytes = bytes(key, "utf-8")
        
        # Ensure key is 24 bytes (192 bits) for 3DES
        key_bytes = key_bytes.ljust(24)[:24]  # Pad or truncate to 24 bytes
        
        # Generate random IV (8 bytes for 3DES)
        iv = os.urandom(8)  # 3DES block size is 64 bits (8 bytes)
        
        # Create padder and pad the message
        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        padded_data = padder.update(message_bytes) + padder.finalize()
        
        # Create cipher with key and IV
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv))
        encryptor = cipher.encryptor()
        
        # Encrypt the message
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine IV and ciphertext, then encode as base64
        encrypted_bytes = iv + ciphertext
        return base64.b64encode(encrypted_bytes).decode("utf-8")
    
    def decrypt(self, encrypted_data: str, key: str) -> str:
        # Convert key to bytes
        key_bytes = bytes(key, "utf-8")
        key_bytes = key_bytes.ljust(24)[:24]  # Pad or truncate to 24 bytes
        
        # Decode base64 string back to bytes
        encrypted_bytes = base64.b64decode(encrypted_data)
        
        # Extract IV and ciphertext (IV is 8 bytes for 3DES)
        iv = encrypted_bytes[:8]
        ciphertext = encrypted_bytes[8:]
        
        # Create cipher with key and IV
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv))
        decryptor = cipher.decryptor()
        
        # Decrypt the message
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        message_bytes = unpadder.update(padded_data) + unpadder.finalize()
        
        return message_bytes.decode("utf-8")
class AESCrypto:
    def __init__(self):
        pass
    
    def encrypt(self, message: str, key: str) -> str:  # Changed return type to str
        # Convert inputs to bytes
        message_bytes = bytes(message, "utf-8")
        key_bytes = bytes(key, "utf-8")
        
        # Ensure key is 32 bytes (256 bits) - AES-256 requirement
        key_bytes = key_bytes.ljust(32)[:32]
        
        # Generate random IV
        iv = os.urandom(16)
        
        # Create padder and pad the message
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(message_bytes) + padder.finalize()
        
        # Create cipher with key and IV
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
        encryptor = cipher.encryptor()
        
        # Encrypt the message
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine IV and ciphertext, then encode as base64
        encrypted_bytes = iv + ciphertext
        return base64.b64encode(encrypted_bytes).decode("utf-8")  # Return as UTF-8 string
    
    def decrypt(self, encrypted_data: str, key: str) -> str:  # Changed input type to str
        # Convert key to bytes
        key_bytes = bytes(key, "utf-8")
        key_bytes = key_bytes.ljust(32)[:32]
        
        # Decode base64 string back to bytes
        encrypted_bytes = base64.b64decode(encrypted_data)
        
        # Extract IV and ciphertext
        iv = encrypted_bytes[:16]
        ciphertext = encrypted_bytes[16:]
        
        # Create cipher with key and IV
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
        decryptor = cipher.decryptor()
        
        # Decrypt the message
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        message_bytes = unpadder.update(padded_data) + unpadder.finalize()
        
        return message_bytes.decode("utf-8")
