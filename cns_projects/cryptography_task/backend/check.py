import string
import random
import sys
class OneTimePadCrypto:
    def __init__(self):
        self.lst_ascii = [chr(i) for i in range(12)]
        self.one_time_pad = list(self.lst_ascii)
    def encrypt(self, msg, key):
        ciphertext = ''
        for idx, char in enumerate(msg):
            charIdx = self.lst_ascii.index(char)
            keyIdx = self.one_time_pad.index(key[idx])

            cipher = (keyIdx + charIdx) % len(self.one_time_pad)
            ciphertext +=  self.lst_ascii[cipher]

        return ciphertext

    def decrypt(self, ciphertext, key):
        if ciphertext == '' or key == '':
            return ''

        charIdx =  self.lst_ascii.index(ciphertext[0])
        keyIdx = self.one_time_pad.index(key[0])

        cipher = (charIdx - keyIdx) % len(self.one_time_pad)
        char =  self.lst_ascii[cipher]

        return char + self.decrypt(ciphertext[1:], key[1:])
