# ⚡ Simple Web Vulnerability Scanner

A **Flask-based web vulnerability scanner** designed for **educational and research use**.  
It detects common vulnerabilities like **Cross-Site Scripting (XSS)**, **SQL Injection (SQLi)**, and **Path Traversal** while providing a modern, interactive UI with downloadable reports.

---

## 🧠 Overview

This project crawls web pages, detects forms, and injects payloads to analyze responses for potential vulnerabilities.  
It also includes **built-in demo results** so you can test and visualize realistic scans without connecting to live targets.

---

## 🧩 Tech Stack

- **Language:** Python 3.11  
- **Framework:** Flask  
- **Libraries:** BeautifulSoup4, Requests, Tabulate  
- **Frontend:** HTML, Bootstrap 5  
- **Output Format:** JSON Reports  

---

## 📁 Project Structure

```
web-vuln-scanner/
│
├── webapp/
│   ├── app.py                 # Flask web server
│   └── templates/
│       ├── index.html         # Homepage
│       └── results.html       # Scan results page
│
├── scanner/
│   ├── crawler.py
│   ├── injector.py
│   ├── form_parser.py
│   ├── payloads.py
│   ├── logger.py
│   ├── sample_data.py         # Demo scan results
│   └── detectors.py
│
├── reports/                   # Auto-generated scan reports
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### Step 1️⃣ — Clone the Repository
```bash
git clone https://github.com/Krshnapriyaa/web-vuln-scanner.git
cd web-vuln-scanner
```

### Step 2️⃣ — Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # For Windows
```

### Step 3️⃣ — Install Dependencies
```bash
pip install -r requirements.txt
```

---

### Step 4️⃣ — Verify Installed Packages
```bash
python -m pip list
```

---

### Step 5️⃣ — Run the Application
```bash
python -m webapp.app
```

Now open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## 🌐 Usage

### 1️⃣ Open the Application

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.  
You’ll see the **Simple Web Vulnerability Scanner** home screen.

---

### 2️⃣ Start a New Scan

Enter a target URL, for example:

```
https://example.com/search?q=test
```

You can also use any of these **demo URLs** to instantly see sample vulnerability results:

| Target URL | Description |
|-------------|-------------|
| `https://example.com/search?q=test` | Reflected XSS |
| `https://app.local/login` | SQL Injection (Auth Bypass) |
| `https://shop.example/item?id=45` | SQL Injection (Union) |
| `https://blog.example/comment` | Stored XSS |
| `https://api.example/profile` | Reflected XSS in JSON |
| `https://legacy.example/item?cat=1` | Command Injection |
| `https://example.com/filter` | Path Traversal |
| `https://example.com/profile?user=krish` | Encoded XSS |
| `https://example.com/products?sort=name` | SQL Injection (Boolean) |
| `http://127.0.0.1:8080/test_form.html` | Local test target |

---

## 🧾 Results and Reports

After scanning, you’ll be redirected to the **results page**.  
Each entry includes:
- Input field  
- Payload used  
- Vulnerability detected (XSS/SQLi)  
- Snippet of response  
- Severity, Confidence, and Remediation advice  

You can also download the report as a JSON file.

---

## 📁 Sample JSON Report

```json
[
  {
    "input": "username",
    "payload": "admin' OR '1'='1",
    "xss": false,
    "sqli": true,
    "severity": "Critical",
    "confidence": "85%",
    "remediation": "Use prepared statements, parameterized queries"
  }
]
```

Reports are automatically saved inside the `/reports/` folder.

---

## ⚠️ Disclaimer

> **Educational Use Only**  
> Do not scan websites without authorization.  
> This project is intended solely for academic and security learning purposes.

---

## 👩‍💻 Author

**Krishna Priya K P**  
🎓 MCA | Cybersecurity & Forensics  
🔗 GitHub: [Krshnapriyaa](https://github.com/Krshnapriyaa)  
📧 For academic use and research guidance

---

⭐ *Built for learning — not for exploitation.*
