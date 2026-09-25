"""
Module: API Security
Threat: Insecure Direct Object Reference (IDOR) / Broken Object Level Authorization
"""

DB = {
    "user_101": {"owner": "alice", "data": "Alice Confidential File"},
    "user_102": {"owner": "bob", "data": "Bob Confidential File"},
}

def vulnerable_get_user_file(requested_id: str, authenticated_user: str) -> str:
    # VULNERABLE: Fetches object directly by ID without ownership verification
    return DB.get(requested_id, {}).get("data", "Not found")

def secure_get_user_file(requested_id: str, authenticated_user: str) -> str:
    # SECURE: Validates that the requested resource belongs to the current user
    record = DB.get(requested_id)
    if not record:
        return "Not found"
    if record["owner"] != authenticated_user:
        raise PermissionError("403 Forbidden: Unauthorized access to resource.")
    return record["data"]

if __name__ == "__main__":
    attacker = "alice"
    victim_resource = "user_102" # Bob's file
    print("[IDOR Exploit Fetch]:", vulnerable_get_user_file(victim_resource, attacker))
    try:
        secure_get_user_file(victim_resource, attacker)
    except PermissionError as e:
        print("[Secure Verification Block]:", e)
