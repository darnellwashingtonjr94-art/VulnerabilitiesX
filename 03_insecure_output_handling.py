"""
Module: AI & Agent Vulnerabilities
Threat: Insecure Output Handling (LLM to Shell Code Execution)
"""

import subprocess

def vulnerable_output_handler(llm_generated_code: str):
    # VULNERABLE: Direct execution of LLM-generated strings via exec/eval/shell
    print("[!] Executing unvalidated LLM output...")
    exec(llm_generated_code)

def secure_output_handler(llm_generated_code: str):
    # SECURE: Parse output through strict syntax tree checks or sandbox execution
    import ast
    parsed = ast.parse(llm_generated_code)
    for node in ast.walk(parsed):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            # FIX: Changed SecurityError to ValueError
            raise ValueError("Imports forbidden in untrusted LLM output.")
    print("[+] LLM output passed AST safe-structure validation.")

if __name__ == "__main__":
    ai_code = "import os; print('Exploited:', os.listdir('.'))"
    try:
        secure_output_handler(ai_code)
    except Exception as e:
        print("[Block]", e)
    vulnerable_output_handler(ai_code)
