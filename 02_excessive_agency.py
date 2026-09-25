"""
Module: AI & Agent Vulnerabilities
Threat: Excessive Agency & Unbounded Tool Execution
"""

import os

def vulnerable_tool_execution(action: str, target: str):
    # VULNERABLE: Agent can execute arbitrary system commands with no boundary check
    print(f"[!] Executing autonomous command: {action} {target}")
    os.system(f"{action} {target}")

def secure_tool_execution(action: str, target: str):
    # SECURE: Strict whitelist of allowed commands and sanitized targets
    ALLOWED_ACTIONS = {"ping": "ping -c 1", "status": "echo"}
    if action not in ALLOWED_ACTIONS:
        raise ValueError("Unauthorized tool action requested.")
    
    # Strip dangerous shell characters
    safe_target = "".join(c for c in target if c.isalnum() or c in ".-")
    print(f"[+] Executing safe tool: {ALLOWED_ACTIONS[action]} {safe_target}")

if __name__ == "__main__":
    vulnerable_tool_execution("echo", "Hello; rm -rf /") # Triggers dangerous sub-command
    secure_tool_execution("ping", "127.0.0.1")
