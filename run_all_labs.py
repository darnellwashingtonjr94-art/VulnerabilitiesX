#!/usr/bin/env python3
"""
VulnerabilitiesX - Master Test Runner
Iterates through all 30 vulnerability scripts to verify they run without syntax 
or execution errors. Captures stdout/stderr and provides an execution summary.
"""

import sys
import time
import subprocess
from pathlib import Path

def run_scripts(base_dir="."):
    # Recursively find all scripts matching the two-digit prefix pattern (01_*.py to 30_*.py)
    script_paths = sorted(Path(base_dir).rglob("[0-9][0-9]_*.py"))
    
    if not script_paths:
        print("No lab scripts found. Ensure scripts are named like '01_prompt_injection.py'.")
        return

    print("=" * 65)
    print("🛡️  VulnerabilitiesX - Master Lab Runner")
    print("=" * 65)
    
    results = []
    total_time = 0

    for path in script_paths:
        # Print a loading indicator that gets overwritten
        print(f"▶ Running {path.name:<35} ... ", end="", flush=True)
        start_time = time.time()
        
        try:
            # Run the script with a 5-second timeout to prevent infinite loops (e.g., bad auth logic)
            process = subprocess.run(
                [sys.executable, str(path)],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            elapsed = time.time() - start_time
            total_time += elapsed
            
            # Check if the script executed successfully (exit code 0)
            if process.returncode == 0:
                print(f"\r✅ [{elapsed:04.2f}s] {path.name:<35} (PASS)  ")
                results.append((path.name, "PASS", elapsed, process.stdout))
            else:
                print(f"\r❌ [{elapsed:04.2f}s] {path.name:<35} (FAIL)  ")
                results.append((path.name, "FAIL", elapsed, process.stderr))
                
        except subprocess.TimeoutExpired:
            elapsed = time.time() - start_time
            total_time += elapsed
            print(f"\r⚠️ [{elapsed:04.2f}s] {path.name:<35} (TIMEOUT)")
            results.append((path.name, "TIMEOUT", elapsed, "Execution exceeded 5 seconds."))
            
        except Exception as e:
            print(f"\r❌ {path.name:<35} (EXCEPTION: {e})")
            results.append((path.name, "ERROR", 0, str(e)))

    # Generate the Execution Summary
    print("\n" + "=" * 65)
    print("📊 Execution Summary")
    print("=" * 65)
    
    passed = sum(1 for r in results if r[1] == "PASS")
    failed = sum(1 for r in results if r[1] == "FAIL")
    timeouts = sum(1 for r in results if r[1] == "TIMEOUT")
    
    # Print the table
    for name, status, t, output in results:
        # Basic ANSI colors for terminal output
        color = "\033[92m" if status == "PASS" else "\033[91m" if status == "FAIL" else "\033[93m"
        reset = "\033[0m"
        print(f"{color}{status:7}{reset} | {name:<35} | {t:04.2f}s")
        
        # Optionally uncomment the lines below to print the error logs for failed scripts
        # if status == "FAIL":
        #     print(f"    {color}Error Log:{reset} {output.strip()}")

    print("-" * 65)
    print(f"Total Scripts: {len(results)} | Passed: {passed} | Failed: {failed} | Timeouts: {timeouts}")
    print(f"Total Execution Time: {total_time:.2f} seconds")
    print("=" * 65)

if __name__ == "__main__":
    # Allows passing a specific directory as an argument: `python run_all_labs.py ./labs`
    target_directory = sys.argv[1] if len(sys.argv) > 1 else "."
    run_scripts(target_directory)
