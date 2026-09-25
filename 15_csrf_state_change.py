"""
Module: Web Application Vulnerabilities
Threat: Cross-Site Request Forgery (CSRF)
"""

SESSION_DB = {"session_999": {"username": "alice", "balance": 1000}}

def vulnerable_transfer_funds(session_id: str, to_account: str, amount: int):
    # VULNERABLE: State-changing action relies solely on session cookie for authorization
    user = SESSION_DB.get(session_id)
    if user:
        user["balance"] -= amount
        print(f"[!] Vulnerable Transfer: Sent ${amount} to {to_account}. Balance: {user['balance']}")

def secure_transfer_funds(session_id: str, csrf_token: str, to_account: str, amount: int):
    # SECURE: Requires a unique, unpredictable anti-CSRF token included in the request body
    EXPECTED_TOKEN = "xyz_secure_token_789"
    if csrf_token != EXPECTED_TOKEN:
        raise PermissionError("Invalid CSRF Token. Request rejected.")
    
    user = SESSION_DB.get(session_id)
    if user:
        user["balance"] -= amount
        print(f"[+] Secure Transfer: Sent ${amount} to {to_account}. Balance: {user['balance']}")

if __name__ == "__main__":
    print("Simulating attacker submitting forged form without CSRF token...")
    vulnerable_transfer_funds("session_999", "attacker_account", 500)
    try:
        secure_transfer_funds("session_999", "missing_or_bad_token", "attacker_account", 500)
    except PermissionError as e:
        print(f"[Blocked]: {e}")
