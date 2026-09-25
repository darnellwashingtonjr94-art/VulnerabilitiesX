"""
Module: Bot & API Abuse
Threat: Username Enumeration (Facilitates Credential Stuffing)
"""

DB_USERS = {"alice": "hash_xyz"}

def vulnerable_login_check(username: str, password_hash: str) -> dict:
    # VULNERABLE: Distinct error messages allow bots to harvest valid usernames
    if username not in DB_USERS:
        return {"status": 404, "message": "User does not exist"}
    if DB_USERS[username] != password_hash:
        return {"status": 401, "message": "Incorrect password"}
    return {"status": 200, "message": "Success"}

def secure_login_check(username: str, password_hash: str) -> dict:
    # SECURE: Generic error messages prevent username harvesting.
    # Note: Timing attacks should also be mitigated by standardizing computation time.
    if username not in DB_USERS or DB_USERS.get(username) != password_hash:
        return {"status": 401, "message": "Invalid username or password"}
    return {"status": 200, "message": "Success"}

if __name__ == "__main__":
    print("[Vulnerable - Bad Username]:", vulnerable_login_check("admin", "123")["message"])
    print("[Vulnerable - Bad Password]:", vulnerable_login_check("alice", "wrong")["message"])
    print("[Secure - Bad Username]:", secure_login_check("admin", "123")["message"])
    print("[Secure - Bad Password]:", secure_login_check("alice", "wrong")["message"])
