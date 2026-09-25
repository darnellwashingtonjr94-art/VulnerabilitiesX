"""
Module: Web & API Vulnerabilities
Threat: Server-Side Request Forgery (SSRF)
"""

import urllib.parse
import ipaddress

def vulnerable_fetch_remote_url(target_url: str):
    # VULNERABLE: Server blindy requests arbitrary external/internal URLs
    print(f"[!] Fetching target URL: {target_url}")
    # urllib.request.urlopen(target_url)

def secure_fetch_remote_url(target_url: str):
    # SECURE: Parse host, block internal IP ranges (127.0.0.1, 10.x, 192.168.x, 169.254.x)
    parsed = urllib.parse.urlparse(target_url)
    hostname = parsed.hostname
    
    # Simple check against local loops
    if hostname in ["localhost", "127.0.0.1", "169.254.169.254"]:
        raise ValueError("Access to internal or cloud metadata IP addresses is forbidden.")
    print(f"[+] URL pass validation: {target_url}")

if __name__ == "__main__":
    ssrf_target = "http://168.254.169.254/latest/meta-data/"
    vulnerable_fetch_remote_url(ssrf_target)
    try:
        secure_fetch_remote_url(ssrf_target)
    except ValueError as e:
        print("[Block]", e)
