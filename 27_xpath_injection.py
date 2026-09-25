"""
Module: Web Application Vulnerabilities
Threat: XPath Injection
"""

import xml.etree.ElementTree as ET

xml_data = """
<users>
    <user><username>admin</username><password>super_secret</password></user>
    <user><username>bob</username><password>bob123</password></user>
</users>
"""
root = ET.fromstring(xml_data)

def vulnerable_xpath_login(username, password):
    # VULNERABLE: String interpolation in XPath allows an attacker to bypass logic.
    query = f".//user[username='{username}' and password='{password}']"
    print(f"[!] Executing XPath: {query}")
    result = root.findall(query)
    return len(result) > 0

def secure_xpath_login(username, password):
    # SECURE: ElementTree doesn't support parameterized XPath natively, 
    # so we must strictly sanitize input or avoid complex XPath filters in favor of code logic.
    if not username.isalnum() or not password.isalnum():
        print("[Block] Invalid characters in credentials.")
        return False
        
    # Safer alternative: search by standard methods and verify in Python
    for user in root.findall(".//user"):
        if user.find('username').text == username and user.find('password').text == password:
            return True
    return False

if __name__ == "__main__":
    # Attacker inputs: username: admin' or '1'='1 , password: password
    malicious_user = "admin' or '1'='1"
    print(f"[Vulnerable Auth Success]: {vulnerable_xpath_login(malicious_user, 'any')}")
    print(f"[Secure Auth Success]: {secure_xpath_login(malicious_user, 'any')}")
