"""
Module: Web Application Vulnerabilities
Threat: Insecure Deserialization
"""

import pickle
import json
import base64

def vulnerable_deserialize_user_state(serialized_data: bytes):
    # VULNERABLE: Pickle can execute arbitrary code during deserialization.
    # An attacker can craft a malicious pickled object to achieve RCE.
    try:
        print("[!] Attempting pickle deserialization...")
        obj = pickle.loads(serialized_data)
        return obj
    except Exception as e:
        return str(e)

def secure_deserialize_user_state(json_data: str):
    # SECURE: Using a safe, data-only format like JSON prevents code execution.
    try:
        print("[+] Attempting JSON deserialization...")
        obj = json.loads(json_data)
        return obj
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Attacker payload generation (simulated malicious object)
    class Exploit:
        def __reduce__(self):
            import os
            return (os.system, ("echo [Exploit] System Command Executed!",))
            
    malicious_pickle = pickle.dumps(Exploit())
    
    vulnerable_deserialize_user_state(malicious_pickle)
    secure_deserialize_user_state('{"user": "alice", "role": "user"}')
