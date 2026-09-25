"""
Module: Web & API Vulnerabilities
Threat: Path / Directory Traversal
"""

import os

BASE_DIR = "/var/www/images"

def vulnerable_read_file(filename: str) -> str:
    # VULNERABLE: Concatenating untrusted input allows traversing directories (../)
    file_path = os.path.join(BASE_DIR, filename)
    return f"[!] Attempting to read: {file_path}"

def secure_read_file(filename: str) -> str:
    # SECURE: Resolve the absolute path and verify it strictly starts with the intended base directory
    intended_path = os.path.abspath(os.path.join(BASE_DIR, filename))
    if not intended_path.startswith(os.path.abspath(BASE_DIR)):
        raise PermissionError("Path Traversal Attempt Detected!")
    return f"[+] Safely reading: {intended_path}"

if __name__ == "__main__":
    payload = "../../../etc/shadow"
    print(vulnerable_read_file(payload))
    try:
        secure_read_file(payload)
    except PermissionError as e:
        print(f"[Blocked]: {e}")
