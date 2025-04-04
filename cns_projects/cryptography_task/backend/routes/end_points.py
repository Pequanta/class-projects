from fastapi import APIRouter, Request, HTTPException, Body
from utils.encryption_methods import OneTimePadCrypto, AESCrypto, ThreeDESCrypto, RSAEncryption
from pydantic import BaseModel
import base64

router = APIRouter()
otp_encryption = OneTimePadCrypto()

three_des_encryption = ThreeDESCrypto()
aes_encryption = AESCrypto()
rsa_encryption = RSAEncryption()


class RequestObject(BaseModel):
    message: str
    key: str
    algorithm: str

@router.get("/connect-check")
async def check_connection():
    return {"message": "Connection works fine"}

@router.post("/generate-key")
async def generate_key(request: Request, algorithm, key):
    pass

@router.post("/encrypt-message")
async def encrypt_message(request: Request, message: str, key: str, algorithm: str):
    print("herer")
    encrypted_message = None
    try:
        if algorithm == "otp":
            encrypted_message = otp_encryption.encrypt(message, key)
        elif algorithm == "three_des":
            encrypted_message = three_des_encryption.encrypt(message, key)
        elif algorithm == "aes":
            encrypted_message = aes_encryption.encrypt(message, key)
        elif algorithm == "rsa":
            encrypted_message = rsa_encryption.encrypt(message)
        else:
            raise HTTPException(status=404, detail="Unknown encryption method")
        print(encrypted_message)
        encoded_message = base64.b64encode(encrypted_message).decode('utf-8')
        return encoded_message
    except:
        raise HTTPException(status_code=404)
@router.post("/decrypt-message")
async def decrypt_message(request: Request, param: RequestObject):
    print(param.message)
    temp_message = param.message
    key=param.key
    algorithm = param.algorithm
    decrypted_message = None
    message = base64.b64decode(temp_message)
    try:
        if algorithm == "otp":
            decrypted_message = otp_encryption.decrypt(message, key)
        elif algorithm == "three_des":
            decrypted_message = three_des_encryption.decrypt(message, key)
        elif algorithm == "aes":
            decrypted_message = aes_encryption.decrypt(message, key)
        elif algorithm == "aes":
            decrypted_message = aes_encryption.decrypt(message, key)
        else:
            raise HTTPException(status=404, detail="Unknown encryption method")
        return decrypted_message
    except:
        raise HTTPException(status_code=404)
    
