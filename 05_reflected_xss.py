"""
Module: Web Application Vulnerabilities
Threat: Reflected Cross-Site Scripting (XSS)
"""

import html

def vulnerable_render_greeting(user_query: str) -> str:
    # VULNERABLE: Unescaped string interpolated directly into HTML context
    return f"<h1>Search Results for: {user_query}</h1>"

def secure_render_greeting(user_query: str) -> str:
    # SECURE: Entity encoding translates special HTML characters into safe literals
    safe_query = html.escape(user_query)
    return f"<h1>Search Results for: {safe_query}</h1>"

if __name__ == "__main__":
    xss_payload = "<script>alert(document.cookie)</script>"
    print("[Vulnerable Output]:", vulnerable_render_greeting(xss_payload))
    print("[Secure Output]:", secure_render_greeting(xss_payload))
