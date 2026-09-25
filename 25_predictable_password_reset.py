"""
Module: Authentication & Session Management
Threat: Predictable Password Reset Tokens (Broken Authentication)
"""

import time
import random
import secrets

def vulnerable_generate_reset_token(user_email: str) -> str:
    # VULNERABLE: Using a weak PRNG (random) seeded with current time.
    # An attacker can predict the token if they know the approximate time of request.
    random.seed(int(time.time()))
    token = str(random.randint(100000, 999999))
    print(f"[!] Vulnerable Token for {user_email}: {token}")
    return token

def secure_generate_reset_token(user_email: str) -> str:
    # SECURE: Using a cryptographically secure random number generator (CSPRNG).
    token = secrets.token_urlsafe(32)
    print(f"[+] Secure Token for {user_email}: {token}")
    return token

if __name__ == "__main__":
    vulnerable_generate_reset_token("victim@example.com")
    secure_generate_reset_token("victim@example.com")
