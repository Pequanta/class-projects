from fastapi import APIRouter, Request, HTTPException
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import string
import random
import sys




"""
    The following class is credited to @albohlabs(github). Since it is not customary to use otp in encryption-decryption(as it depends in the generation of truly random number)
    , the implementation doesn't entail standard library.
"""
random.seed(11) #ensuring the repreoducibility of different checkups in one program run.
class OneTimePadCrypto:
    def __init__(self):
        self.lst_ascii = string.ascii_lowerlowercase
        self.one_time_pad = random.shuffle(list(self.lst_ascii))
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
router = APIRouter()
otp_encryption = OneTimePadCrypto()

@router.get("/connect-check")
def check_connection():
    return {"message": "Connection works fine"}

@router.post("/generate-key")
def generate_key(request: Request, algorithm, key):
    pass

@router.post("/encrypt-message")
def encrypt_message(request: Request, plain_message: str, key: str, algorithm: str):
    encrypted_message = None
    try:
        if algorithm == "otp":
            encrypted_message = otp_encryption.encrypt(plain_message, key)
        elif algorithm == "three_des":
            encrypted_message = ""
        elif algorithm == "three_des":
            encrypted_message = ""
        else:
            encrypted_message = ""
    except:
        raise HTTPException(status_code=404)
@router.post("/decrypt-message")
def decrypt_message(request: Request, encrypted_message: str, key: str, algorithm: str):
    decrypted_message = None
    try:
        if algorithm == "otp":
            decrypted_message = otp_encryption.encrypt(encrypted_message, key)
        elif algorithm == "three_des":
            decrypted_message = ""
        elif algorithm == "three_des":
            decrypted_message = ""
        else:
            decrypted_message = ""
    except:
        raise HTTPException(status_code=404)
    
