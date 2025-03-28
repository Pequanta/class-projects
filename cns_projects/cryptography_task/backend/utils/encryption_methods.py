import string
import os
import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

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
        pass
    
    def encrypt(self, message: str, key: str) -> str:
        message_bytes = bytes(message, "utf-8")
        key_bytes = bytes(key, "utf-8")
        key_bytes = key_bytes.ljust(24)[:24]  
        iv = os.urandom(8)  
        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        padded_data = padder.update(message_bytes) + padder.finalize()
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        encrypted_bytes = iv + ciphertext
        return base64.b64encode(encrypted_bytes).decode("utf-8")
    
    def decrypt(self, encrypted_data: str, key: str) -> str:
        key_bytes = bytes(key, "utf-8")
        key_bytes = key_bytes.ljust(24)[:24]  
        encrypted_bytes = base64.b64decode(encrypted_data)
        iv = encrypted_bytes[:8]
        ciphertext = encrypted_bytes[8:]
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        message_bytes = unpadder.update(padded_data) + unpadder.finalize()
        return message_bytes.decode("utf-8")

class AESCrypto:
    def __init__(self):
        pass
    
    def encrypt(self, message: str, key: str) -> str:
        message_bytes = bytes(message, "utf-8")
        key_bytes = bytes(key, "utf-8")
        key_bytes = key_bytes.ljust(32)[:32]
        iv = os.urandom(16)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(message_bytes) + padder.finalize()
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        encrypted_bytes = iv + ciphertext
        return base64.b64encode(encrypted_bytes).decode("utf-8")  
    
    def decrypt(self, encrypted_data: str, key: str) -> str:
        key_bytes = bytes(key, "utf-8")
        key_bytes = key_bytes.ljust(32)[:32]
        encrypted_bytes = base64.b64decode(encrypted_data)
        iv = encrypted_bytes[:16]
        ciphertext = encrypted_bytes[16:]
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        message_bytes = unpadder.update(padded_data) + unpadder.finalize()
        return message_bytes.decode("utf-8")
