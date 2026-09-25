"""
Module: AI & Agent Vulnerabilities
Threat: Agent Data Leakage (PII Exposure to Third-Party LLMs)
"""

import re

def vulnerable_agent_query(user_prompt: str, user_profile: dict):
    # VULNERABLE: Passing raw, unsanitized user profile data directly to an external API/LLM
    context = f"User context: {user_profile}. Prompt: {user_prompt}"
    print(f"[!] Sending to external LLM: {context}")
    return "API Request Sent."

def secure_agent_query(user_prompt: str, user_profile: dict):
    # SECURE: Data masking and redaction of PII before sending to external endpoints.
    safe_profile = user_profile.copy()
    
    # Redact SSN and Mask Credit Card
    if "ssn" in safe_profile:
        safe_profile["ssn"] = "[REDACTED]"
    if "cc" in safe_profile:
        safe_profile["cc"] = f"****-****-****-{safe_profile['cc'][-4:]}"
        
    context = f"User context: {safe_profile}. Prompt: {user_prompt}"
    print(f"[+] Sending to external LLM: {context}")
    return "API Request Sent."

if __name__ == "__main__":
    sensitive_data = {"name": "Alice", "ssn": "123-45-6789", "cc": "4111222233334444"}
    prompt = "What is my account status?"
    
    vulnerable_agent_query(prompt, sensitive_data)
    print("-" * 40)
    secure_agent_query(prompt, sensitive_data)
