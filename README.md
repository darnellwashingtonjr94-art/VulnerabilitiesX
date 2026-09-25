# VulnerabilitiesX

**VulnerabilitiesX** is an educational reference repository and security lab designed to demonstrate, analyze, and remediate modern cyber threats across AI agents, web applications, APIs, and automated bots.

> **Disclaimer:** This repository is strictly for educational, research, and defensive training purposes. All examples should be executed in isolated environments (e.g., local containers or dedicated sandboxes).

---

## 🎯 Project Goals

- **Educate:** Understand how security vulnerabilities manifest in modern application architectures, including autonomous AI systems.
- **Demonstrate:** Compare side-by-side implementations of **vulnerable** code alongside **remediated** (secure) patterns.
- **Benchmark:** Provide standardized test cases for automated security scanning tools, SAST/DAST suites, and red/blue team training.

---

## 🧪 Module Overview

| Category | Lab Identifier | Core Threat Focus |
| :--- | :--- | :--- |
| **AI & Autonomous Agents** | `01-ai-and-agents` | Direct/Indirect Prompt Injection, Excessive Agency, Memory Poisoning |
| **Web & API Security** | `02-web-and-apis` | SQL Injection (SQLi), Cross-Site Scripting (XSS), IDOR, SSRF, BOLA |
| **Bots & Authentication** | `03-bot-and-auth` | Credential Stuffing, Weak JWT Validation, Rate Limit Bypass |

---

## 🛠️ Quick Start

### Prerequisites
- [Docker](https://www.docker.com/) & Docker Compose
- [Python 3.11+](https://www.python.org/)
- [Node.js 20+](https://nodejs.org/)

### Setting Up Local Labs

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/VulnerabilitiesX.git](https://github.com/YOUR-USERNAME/VulnerabilitiesX.git)
   cd VulnerabilitiesX
