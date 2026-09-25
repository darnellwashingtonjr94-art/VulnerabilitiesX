"""
Module: Web & System Security
Threat: OS Command Injection
"""

import subprocess

def vulnerable_ping_host(ip_address: str):
    # VULNERABLE: Spawns shell interpreter with concatenated user input
    command = f"ping -c 1 {ip_address}"
    print(f"[!] Running shell command: {command}")
    # subprocess.run(command, shell=True)

def secure_ping_host(ip_address: str):
    # SECURE: Shell disabled (`shell=False`), arguments passed as explicit array elements
    command_args = ["ping", "-c", "1", ip_address]
    print(f"[+] Running array-isolated command: {command_args}")
    # subprocess.run(command_args, shell=False)

if __name__ == "__main__":
    payload = "127.0.0.1; cat /etc/passwd"
    vulnerable_ping_host(payload)
    secure_ping_host(payload)
