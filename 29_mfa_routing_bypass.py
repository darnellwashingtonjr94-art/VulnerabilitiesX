"""
Module: Authentication & Session Management
Threat: Multi-Factor Authentication (MFA) Bypass
"""

# Simulating a session store
SESSION_STORE = {"session_abc": {"user": "alice", "mfa_verified": False}}

def vulnerable_access_dashboard(session_id: str, request_step: str):
    # VULNERABLE: Relies on a client-provided parameter (`request_step`) to determine auth state.
    # An attacker can skip the MFA POST request and just request the dashboard.
    if request_step == "skip_mfa_and_go_to_dashboard":
        print("[!] Vulnerable: Dashboard accessed without MFA validation.")
        return True
    return False

def secure_access_dashboard(session_id: str):
    # SECURE: Enforces state-checking exclusively on server-side session variables.
    session = SESSION_STORE.get(session_id)
    if not session:
        return False
        
    if not session.get("mfa_verified"):
        print("[Block] Secure: MFA not completed. Redirecting to MFA challenge.")
        return False
        
    print("[+] Secure: Dashboard accessed successfully.")
    return True

if __name__ == "__main__":
    vulnerable_access_dashboard("session_abc", "skip_mfa_and_go_to_dashboard")
    secure_access_dashboard("session_abc")
