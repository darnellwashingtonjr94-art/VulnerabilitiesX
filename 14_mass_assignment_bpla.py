"""
Module: API Security
Threat: Mass Assignment / Broken Property Level Authorization (BPLA)
"""

class User:
    def __init__(self, username):
        self.username = username
        self.email = ""
        self.is_admin = False

def vulnerable_update_profile(user_obj, request_data: dict):
    # VULNERABLE: Blindly applying all provided JSON fields to the object attributes
    for key, value in request_data.items():
        setattr(user_obj, key, value)
    return user_obj

def secure_update_profile(user_obj, request_data: dict):
    # SECURE: Strict allowlist of fields permitted for user modification
    ALLOWED_FIELDS = {"email", "display_name"}
    for key, value in request_data.items():
        if key in ALLOWED_FIELDS:
            setattr(user_obj, key, value)
        else:
            print(f"[Blocked] Unauthorized property modification attempt: {key}")
    return user_obj

if __name__ == "__main__":
    malicious_payload = {"email": "attacker@evil.com", "is_admin": True}
    
    vuln_user = User("alice")
    vulnerable_update_profile(vuln_user, malicious_payload)
    print(f"[Vulnerable Update]: is_admin = {vuln_user.is_admin}")
    
    sec_user = User("bob")
    secure_update_profile(sec_user, malicious_payload)
    print(f"[Secure Update]: is_admin = {sec_user.is_admin}")
