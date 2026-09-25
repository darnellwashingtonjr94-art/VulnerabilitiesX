"""
Module: API & Infrastructure Security
Threat: Cross-Origin Resource Sharing (CORS) Misconfiguration
"""

def vulnerable_cors_handler(request_origin: str) -> dict:
    # VULNERABLE: Blindly reflects any origin provided in the request headers.
    # Allows malicious sites to read authenticated API responses via user's browser.
    headers = {
        "Access-Control-Allow-Origin": request_origin,
        "Access-Control-Allow-Credentials": "true"
    }
    print(f"[!] CORS Headers set to reflect origin: {request_origin}")
    return headers

def secure_cors_handler(request_origin: str) -> dict:
    # SECURE: Strict allowlist of trusted origins.
    ALLOWED_ORIGINS = {"https://myapp.com", "https://api.myapp.com"}
    
    if request_origin in ALLOWED_ORIGINS:
        origin_header = request_origin
    else:
        origin_header = "null" # Deny CORS
        
    headers = {
        "Access-Control-Allow-Origin": origin_header,
        "Access-Control-Allow-Credentials": "true"
    }
    print(f"[+] CORS Headers strict validation. Sent: {origin_header}")
    return headers

if __name__ == "__main__":
    evil_origin = "https://attacker.com"
    vulnerable_cors_handler(evil_origin)
    secure_cors_handler(evil_origin)
