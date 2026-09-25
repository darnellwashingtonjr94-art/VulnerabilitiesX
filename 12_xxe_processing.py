"""
Module: Web Application Vulnerabilities
Threat: XML External Entity (XXE) Processing
"""

import xml.etree.ElementTree as ET
# In a real environment, use defusedxml to patch this safely.

def vulnerable_parse_xml(xml_payload: str):
    # VULNERABLE: Parsing untrusted XML data allows external entity expansion, 
    # potentially reading local system files (e.g., /etc/passwd).
    try:
        # Standard ElementTree in older Python versions or lxml with resolve_entities=True
        root = ET.fromstring(xml_payload)
        return root.text
    except Exception as e:
        return str(e)

def secure_parse_xml(xml_payload: str):
    # SECURE: Using a hardened XML parser that disables entity expansion and DTDs.
    try:
        import defusedxml.ElementTree as DET
        root = DET.fromstring(xml_payload)
        return root.text
    except Exception as e:
        return "Secure parser blocked entity expansion or invalid XML."

if __name__ == "__main__":
    xxe_payload = """<?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
    <data>&xxe;</data>"""
    print("[Vulnerable (Simulated)]: Attempts to read /etc/passwd via entity reference.")
    print("[Secure Parser Output]:", secure_parse_xml(xxe_payload))
