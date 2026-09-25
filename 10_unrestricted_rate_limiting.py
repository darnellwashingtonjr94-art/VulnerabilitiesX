"""
Module: Bot & API Abuse
Threat: Automated Brute-Force & Unrestricted Rate Limiting
"""

import time

LOGIN_ATTEMPTS = {}

def vulnerable_login(username: str, password_attempt: str) -> bool:
    # VULNERABLE: No tracking of failed attempts; allows infinite rapid guesses
    return username == "admin" and password_attempt == "Secret123"

def secure_login(username: str, password_attempt: str) -> bool:
    # SECURE: Track attempts per IP/user and enforce exponential time lockouts
    current_time = time.time()
    attempts, last_attempt = LOGIN_ATTEMPTS.get(username, (0, 0))
    
    if attempts >= 3 and (current_time - last_attempt) < 15:
        raise Exception("Account locked due to excessive failed attempts. Try again in 15 seconds.")
    
    success = (username == "admin" and password_attempt == "Secret123")
    if not success:
        LOGIN_ATTEMPTS[username] = (attempts + 1, current_time)
    else:
        LOGIN_ATTEMPTS[username] = (0, 0)
    return success

if __name__ == "__main__":
    user = "admin"
    for i in range(4):
        try:
            res = secure_login(user, f"wrong_pass_{i}")
            print(f"Attempt {i+1}: Failed")
        except Exception as e:
            print(f"Attempt {i+1}:", e)
