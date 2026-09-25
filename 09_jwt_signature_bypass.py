"""
Module: Authentication & Session Management
Threat: JWT Signature Bypass / Insecure Algorithm Handling
"""

import jwt

SECRET = "super-secret-key-123"

def vulnerable_decode_token(token: str) -> dict:
    # VULNERABLE: Disables signature verification or allows 'none' algorithm
    return jwt.decode(token, options={"verify_signature": False})

def secure_decode_token(token: str) -> dict:
    # SECURE: Enforces explicit algorithm whitelist and key verification
    return jwt.decode(token, SECRET, algorithms=["HS256"])

if __name__ == "__main__":
    valid_token = jwt.encode({"user": "admin"}, SECRET, algorithm="HS256")
    print("[Vulnerable Decode]:", vulnerable_decode_token(valid_token))
    print("[Secure Verified Decode]:", secure_decode_token(valid_token))
