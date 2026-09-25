"""
Module: API & Infrastructure Security
Threat: Server-Side Request Forgery (SSRF) via Webhooks
"""

import urllib.parse
import ipaddress

def vulnerable_register_webhook(target_url: str):
    # VULNERABLE: Accepts any URL for webhook registration, allowing attackers to probe
    # internal microservices or cloud metadata endpoints.
    print(f"[!] Registered webhook for: {target_url}")
    # requests.post(target_url, data=event_data)

def secure_register_webhook(target_url: str):
    # SECURE: DNS resolution and strict IP validation against private/internal blocks.
    try:
        parsed_url = urllib.parse.urlparse(target_url)
        # In a real scenario, you must resolve the hostname to an IP and check it, 
        # protecting against DNS rebinding. Here we simulate the IP check:
        simulated_resolved_ip = ipaddress.ip_address("10.0.0.5") # Example internal IP
        
        if simulated_resolved_ip.is_private or simulated_resolved_ip.is_loopback:
            raise ValueError("Webhook URLs cannot resolve to internal/private IPs.")
            
        print(f"[+] Securely registered webhook for: {target_url}")
    except Exception as e:
        print(f"[Block] {e}")

if __name__ == "__main__":
    internal_target = "http://internal-billing-service.local/admin"
    vulnerable_register_webhook(internal_target)
    secure_register_webhook(internal_target)
