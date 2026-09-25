"""
Module: AI & Agent Vulnerabilities
Threat: Supply Chain & Agent Plugin Poisoning
"""

import importlib
import hashlib

def vulnerable_load_plugin(plugin_name: str):
    # VULNERABLE: Dynamically loading a third-party tool based on unsanitized input
    # or lacking integrity checks allows an attacker to load malicious local modules.
    try:
        plugin = importlib.import_module(plugin_name)
        print(f"[!] Loaded plugin: {plugin.__name__}")
    except Exception as e:
        print(f"[Error] {e}")

def secure_load_plugin(plugin_name: str, expected_hash: str):
    # SECURE: Verifies the integrity of the plugin file before executing/loading it
    # and enforces a strict allowlist.
    ALLOWED_PLUGINS = {"math_tool", "weather_api"}
    if plugin_name not in ALLOWED_PLUGINS:
        print(f"[Block] Plugin {plugin_name} not in allowlist.")
        return
        
    # Simulate a hash verification
    # with open(f"{plugin_name}.py", "rb") as f: ...
    simulated_file_hash = "abc123hash" 
    
    if simulated_file_hash != expected_hash:
        print(f"[Block] Plugin integrity check failed for {plugin_name}.")
        return
        
    print(f"[+] Securely loaded verified plugin: {plugin_name}")

if __name__ == "__main__":
    vulnerable_load_plugin("os") # Attacker forces agent to load the OS module
    secure_load_plugin("os", "fakehash")
    secure_load_plugin("math_tool", "abc123hash")
