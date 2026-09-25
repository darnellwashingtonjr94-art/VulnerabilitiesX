"""
Module: Web & API Vulnerabilities
Threat: SQL Injection (SQLi)
"""

import sqlite3

def vulnerable_search_user(cursor, username: str):
    # VULNERABLE: String formatting allows query structure manipulation
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return cursor.execute(query).fetchall()

def secure_search_user(cursor, username: str):
    # SECURE: Parameterized queries use placeholders to escape user inputs
    query = "SELECT * FROM users WHERE username = ?"
    return cursor.execute(query, (username,)).fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username TEXT, role TEXT)")
    cur.execute("INSERT INTO users VALUES ('admin', 'superuser'), ('alice', 'user')")

    sqli_payload = "admin' OR '1'='1"
    print("[Vulnerable SQLi Result Count]:", len(vulnerable_search_user(cur, sqli_payload)))
    print("[Secure Query Result Count]:", len(secure_search_user(cur, sqli_payload)))
