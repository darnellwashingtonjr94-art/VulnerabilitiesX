"""
Module: API & Bot Security
Threat: Unrestricted Resource Consumption (Pagination DoS)
"""

# Simulating a large database table
LARGE_DATASET = [{"id": i, "name": f"Item_{i}"} for i in range(100000)]

def vulnerable_get_items(limit: int):
    # VULNERABLE: Allows a client to request an unbounded number of records,
    # causing memory exhaustion and database overload.
    print(f"[!] Fetching {limit} records into memory...")
    return LARGE_DATASET[:limit]

def secure_get_items(limit: int):
    # SECURE: Enforces a strict server-side maximum limit (pagination constraint).
    MAX_LIMIT = 100
    safe_limit = min(limit, MAX_LIMIT)
    print(f"[+] Safe fetch constrained to {safe_limit} records.")
    return LARGE_DATASET[:safe_limit]

if __name__ == "__main__":
    malicious_limit = 9999999
    print(f"[Vulnerable]: Returned {len(vulnerable_get_items(malicious_limit))} items")
    print(f"[Secure]: Returned {len(secure_get_items(malicious_limit))} items")
