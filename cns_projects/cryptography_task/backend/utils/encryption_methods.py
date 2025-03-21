import string
import random
import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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
        pass
    def encrypt(self, message: str, key: str):
        pass
    def decrypt(self, message: str, key: str):
        pass