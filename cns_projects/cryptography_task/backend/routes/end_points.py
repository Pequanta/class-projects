from fastapi import APIRouter, Request, HTTPException
from utils.encryption_methods import OneTimePadCrypto, AESCrypto, ThreeDESCrypto


router = APIRouter()
otp_encryption = OneTimePadCrypto()

three_des_encryption = ThreeDESCrypto()
aes_encryption = AESCrypto()
@router.get("/connect-check")
async def check_connection():
    return {"message": "Connection works fine"}

@router.post("/generate-key")
async def generate_key(request: Request, algorithm, key):
    pass

@router.post("/encrypt-message")
async def encrypt_message(request: Request, message: str, key: str, algorithm: str):
    encrypted_message = None
    try:
        if algorithm == "otp":
            encrypted_message = otp_encryption.encrypt(message, key)
        elif algorithm == "three_des":
            encrypted_message = three_des_encryption.encrypt(message, key)
        elif algorithm == "aes":
            print("another")
            print("naother")
            encrypted_message = aes_encryption.encrypt(message, key)
        else:
            raise HTTPException(status=404, detail="Unknown encryption method")
        print(encrypted_message)
        return encrypted_message
    except:
        raise HTTPException(status_code=404)
@router.post("/decrypt-message")
async def decrypt_message(request: Request, message: str, key: str, algorithm: str):
    decrypted_message = None
    print(message)
    try:
        if algorithm == "otp":
            decrypted_message = otp_encryption.decrypt(message, key)
        elif algorithm == "three_des":
            decrypted_message = three_des_encryption.decrypt(message, key)
        elif algorithm == "aes":
            print("here")
            decrypted_message = aes_encryption.decrypt(message, key)
        else:
            raise HTTPException(status=404, detail="Unknown encryption method")
        return decrypted_message
    except:
        raise HTTPException(status_code=404)
    
