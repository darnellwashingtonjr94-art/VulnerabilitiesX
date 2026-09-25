"""
Module: Web Application Vulnerabilities
Threat: Business Logic Race Condition (TOCTOU / Scalping)
"""

import time
import threading

inventory = {"limited_sneakers": 1}

def vulnerable_purchase(user: str):
    # VULNERABLE: Time-Of-Check to Time-Of-Use (TOCTOU) flaw.
    # Concurrent requests can pass the check before the inventory decrements.
    if inventory["limited_sneakers"] > 0:
        time.sleep(0.1) # Simulate database latency
        inventory["limited_sneakers"] -= 1
        print(f"[!] {user} bought the item! Remaining: {inventory['limited_sneakers']}")

# Secure implementation using a thread lock (simulating a DB row lock/atomic operation)
lock = threading.Lock()

def secure_purchase(user: str):
    # SECURE: Atomic transaction prevents concurrent threads from violating the constraint.
    with lock:
        if inventory["limited_sneakers"] > 0:
            time.sleep(0.1) 
            inventory["limited_sneakers"] -= 1
            print(f"[+] {user} bought the item! Remaining: {inventory['limited_sneakers']}")
        else:
            print(f"[Block] {user} purchase failed. Out of stock.")

if __name__ == "__main__":
    print("--- Simulating Vulnerable Race Condition ---")
    inventory["limited_sneakers"] = 1
    threads = [threading.Thread(target=vulnerable_purchase, args=(f"Bot_{i}",)) for i in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()
    
    print("\n--- Simulating Secure Transaction ---")
    inventory["limited_sneakers"] = 1
    threads = [threading.Thread(target=secure_purchase, args=(f"User_{i}",)) for i in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()
