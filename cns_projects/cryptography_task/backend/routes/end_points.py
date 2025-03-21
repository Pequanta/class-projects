from fastapi import APIRouter, Request, HTTPException
from utils.encryption_methods import OneTimePadCrypto





router = APIRouter()
otp_encryption = OneTimePadCrypto()

@router.get("/connect-check")
def check_connection():
    return {"message": "Connection works fine"}

@router.post("/generate-key")
def generate_key(request: Request, algorithm, key):
    pass

@router.post("/encrypt-message")
def encrypt_message(request: Request, message: str, key: str, algorithm: str):
    encrypted_message = None
    try:
        if algorithm == "otp":
            encrypted_message = otp_encryption.encrypt(message, key)
        elif algorithm == "three_des":
            encrypted_message = ""
        elif algorithm == "three_des":
            encrypted_message = ""
        else:
            encrypted_message = ""
        print(encrypted_message)
        return encrypted_message
    except:
        raise HTTPException(status_code=404)
@router.post("/decrypt-message")
def decrypt_message(request: Request, message: str, key: str, algorithm: str):
    decrypted_message = None
    try:
        if algorithm == "otp":
            decrypted_message = otp_encryption.decrypt(message, key)
        elif algorithm == "three_des":
            decrypted_message = ""
        elif algorithm == "three_des":
            decrypted_message = ""
        else:
            decrypted_message = ""
        return decrypted_message
    except:
        raise HTTPException(status_code=404)
    
