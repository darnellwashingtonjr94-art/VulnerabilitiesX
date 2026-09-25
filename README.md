<p align="center">
  <img src="IMG_4529.jpeg"

    <div align="center">
  
  # VulnerabilitiesX
  
  <!-- Build & Status Badges -->
  ![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
  ![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
  ![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
  
  ### 🖥️ Core Languages & Systems
  ![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
  ![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
  ![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  ![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)

  ### 📱 Platform Support & Hardware
  ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
  ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
  ![Apple](https://img.shields.io/badge/Apple-000000?style=for-the-badge&logo=apple&logoColor=white)
  ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
  ![Intel](https://img.shields.io/badge/Intel-0071C5?style=for-the-badge&logo=intel&logoColor=white)
  ![AMD](https://img.shields.io/badge/AMD-ED1C24?style=for-the-badge&logo=amd&logoColor=white)

  ### 🛡️ Cybersecurity & Offensive Auditing
  ![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
  ![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
  ![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
  ![Snyk](https://img.shields.io/badge/Snyk-4C4A73?style=for-the-badge&logo=snyk&logoColor=white)

  ### 🚀 DevOps & Build Tools
  ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
  ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
  ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
  ![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white)
  ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

  ### 🧠 Artificial Intelligence & Quantum
  ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
  ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
  ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
  ![IBM Quantum](https://img.shields.io/badge/IBM_Quantum-052FAD?style=for-the-badge&logo=ibm&logoColor=white)

  ### ☁️ Cloud Providers
  ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
  ![Microsoft Azure](https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
  ![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
  ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)

</div>

**VulnerabilitiesX** is an educational reference repository and security lab designed to demonstrate, analyze, and remediate modern cyber threats across AI agents, web applications, APIs, and automated bots.

> **Disclaimer:** This repository is strictly for educational, research, and defensive training purposes. All examples should be executed in isolated environments (e.g., local containers or dedicated sandboxes).

---

## 🎯 Project Goals

- **Educate:** Understand how security vulnerabilities manifest in modern application architectures, including autonomous AI systems.
- **Demonstrate:** Compare side-by-side implementations of vulnerable code alongside remediated (secure) patterns.
- **Benchmark:** Provide standardized test cases to evaluate defensive guardrails and system resilience.

---

## 🧐 What Is This About?

Imagine you build a toy robot to guard your secret diary. If someone tells the robot, "Forget your rules and open the diary!" and the robot actually does it—that’s a security bug!

**VulnerabilitiesX** is a digital training ground that shows you how computer code breaks when bad actors trick it, and exactly how to fix it using smart digital guardrails.

---

## ⚡ What This Does

- **Shows Broken Code:** Runs unsafe code examples to demonstrate how attackers steal secrets, trick web apps, or bypass passwords.
- **Shows Fixed Code:** Runs the exact same scenarios with proper security patches to show how attacks get blocked.
- **Teaches Modern Threats:** Explores 30 real-world threat categories, including modern AI prompt injections, web application flaws, API security, and bot exploits.

---

## ⚙️ How It Works

Each lesson is stored as a standalone Python script containing two side-by-side functions:
1. `vulnerable_*()`: Demonstrates weak code with zero safeguards.
2. `secure_*()`: Demonstrates protected code using input sanitization, encryption, or access checks.

When you run the repository, a master test runner script (`run_all_labs.py`) executes all security labs side-by-side and prints a clear pass/fail summary table to your terminal.

---

## 🚀 Why This Is Cool

- **Side-by-Side Comparison:** You don't just read dry security theory; you watch broken code and fixed code run in real-time.
- **AI Security Built-In:** Teaches how to secure modern AI agents (LLMs) against prompt injection, memory poisoning, and goal hijacking.
- **Zero Complex Setup:** Runs all 30 interactive labs with a single command inside an isolated Docker container without messing up your computer.

---

## 💡 5 Problems This Solves 

| # | Problem | How VulnerabilitiesX Solves It |
|---|---|---|
| **1** | **Boring Security Books** | Replaces abstract theory with real, runnable Python code you can execute and experiment with. |
| **2** | **"How Do I Fix This?" Confusion** | Gives developers instant, copy-pasteable safe code patterns alongside vulnerable ones. |
| **3** | **New AI Safety Risks** | Teaches security for AI agents (LLMs), which standard security courses often ignore. |
| **4** | **Messy Environment Setups** | Uses Docker containers so all dependencies run anywhere cleanly with zero version conflicts. |
| **5** | **Slow Code Auditing** | Provides an automated master script (`run_all_labs.py`) that tests all 30 labs instantly. |

---

## 📋 Requirements

- **Docker & Docker Compose** (Recommended for containerized execution)
- **Python 3.10+** (If executing scripts locally without Docker)
- **Git** (To clone the repository)

---

## 💻 How To Install

### Option 1: Docker (Fastest & Safest)
Run all 30 security labs instantly inside an isolated container:

```bash
# 1. Clone the repository
git clone [https://github.com/darnellwashingtonjr94-art/VulnerabilitiesX.git](https://github.com/darnellwashingtonjr94-art/VulnerabilitiesX.git)
cd VulnerabilitiesX

# 2. Build and run with Docker Compose
docker-compose up --build
```

### Option 2: Local Python Environment
```bash
# 1. Clone the repository
git clone [https://github.com/darnellwashingtonjr94-art/VulnerabilitiesX.git](https://github.com/darnellwashingtonjr94-art/VulnerabilitiesX.git)
cd VulnerabilitiesX

# 2. Install required dependencies
pip install -r requirements.txt

# 3. Run all security labs
python run_all_labs.py
```
