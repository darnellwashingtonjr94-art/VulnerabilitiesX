"""
Module: Authentication & Cloud Security
Threat: Insecure Password Storage
"""

import hashlib
import os

def vulnerable_store_password(password: str) -> str:
    # VULNERABLE: Using obsolete, fast hashing algorithms like MD5 without salts
    # Vulnerable to rainbow tables and brute-force cracking.
    return hashlib.md5(password.encode()).hexdigest()

def secure_store_password(password: str) -> bytes:
    # SECURE: Using a modern key derivation function (PBKDF2, bcrypt, or Argon2) with a random salt
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000 # High iteration count
    )
    return salt + hashed_password

if __name__ == "__main__":
    pwd = "password123"
    print("[Vulnerable MD5 Hash]:", vulnerable_store_password(pwd))
    print("[Secure PBKDF2 Storage]:", secure_store_password(pwd).hex()[:40] + "...")
