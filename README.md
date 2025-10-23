# ⚡ Simple Web Vulnerability Scanner

A **Flask-based web vulnerability scanner** designed for **educational and research use**.
It detects common vulnerabilities like **Cross-Site Scripting (XSS)**, **SQL Injection (SQLi)**, and **Path Traversal**, while providing a clean web interface with downloadable reports.

---

## 🧬 Overview

This project crawls target websites, identifies input fields, and injects payloads to analyze responses for potential vulnerabilities.
It includes **built-in demo data** for realistic scan results even without external targets.

---

## 🧉 Tech Stack

| Component         | Technology                          |
| ----------------- | ----------------------------------- |
| **Language**      | Python 3.11                         |
| **Framework**     | Flask                               |
| **Libraries**     | Requests, BeautifulSoup4, Tabulate  |
| **Frontend**      | HTML + Bootstrap 5                  |
| **Report Format** | JSON (auto-generated in `/reports`) |

---

## ⚙️ Setup & Execution Steps

| Step   | Command / Action                                                                            | Expected Result                              | Screenshot                                                   |
| ------ | ------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| **1**  | `git clone https://github.com/Krshnapriyaa/web-vuln-scanner.git` <br> `cd web-vuln-scanner` | Project cloned successfully                  | ![Step 1](screenshots/Screenshot%20\(205\).png)              |
| **2**  | `python -m venv venv` <br> `venv\\Scripts\\activate`                                        | Virtual environment created                  | ![Step 2](screenshots/Screenshot%20\(206\).png)              |
| **3**  | `pip install -r requirements.txt`                                                           | All dependencies installed successfully      | ![Step 3](screenshots/Screenshot%202025-10-23%20185456.png)  |
| **4**  | `python -m webapp.app`                                                                      | Flask app started at `http://127.0.0.1:5000` | ![Step 4](screenshots/Screenshot%20\(212\).png)              |
| **5**  | Open browser → `http://127.0.0.1:5000`                                                      | Homepage loaded successfully                 | ![Step 5](screenshots/Screenshot%202025-10-23%20185456.png)  |
| **6**  | Enter target URL → Click **Start Scan**                                                     | Scan initiated successfully                  | ![Step 6](screenshots/Screenshot%202025-10-23%20185942.png)  |
| **7**  | Scan progress visible                                                                       | Detected results displayed in table          | ![Step 7](screenshots/Screenshot%202025-10-23%20190010.png)  |
| **8**  | View results for login                                                                      | SQL Injection detected                       | ![Step 8](screenshots/Screenshot%202025-10-23%20190036.png)  |
| **9**  | View results for search                                                                     | XSS vulnerability identified                 | ![Step 9](screenshots/Screenshot%202025-10-23%20190101.png)  |
| **10** | Download JSON report                                                                        | Saved under `/reports/` folder               | ![Step 10](screenshots/Screenshot%202025-10-23%20190224.png) |

---

## 🌐 Usage Guide

### 1️⃣ Launch the App

Run:

```bash
python -m webapp.app
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 2️⃣ Start a New Scan

Enter a URL like:

```
https://example.com/search?q=test
```

You can also test using these demo URLs:

| URL                                    | Description                 |
| -------------------------------------- | --------------------------- |
| `https://example.com/search?q=test`    | Reflected XSS               |
| `https://app.local/login`              | SQL Injection (Auth Bypass) |
| `https://shop.example/item?id=45`      | SQL Injection (Union)       |
| `https://blog.example/comment`         | Stored XSS                  |
| `https://api.example/profile`          | JSON-based XSS              |
| `https://legacy.example/item?cat=1`    | Command Injection           |
| `https://example.com/filter`           | Path Traversal              |
| `http://127.0.0.1:8080/test_form.html` | Local demo test             |

---

## 🧾 Example Report

```json
[
  {
    "url": "https://example.com/search?q=test",
    "input": "q",
    "payload": "\"><script>alert(1)</script>",
    "vulnerability": "Reflected XSS",
    "severity": "High",
    "confidence": "90%",
    "remediation": "Escape input and apply Content Security Policy"
  }
]
```

---

## 🧉 Results Page Preview

![Result Table](screenshots/Screenshot%202025-10-23%20190010.png)
![XSS Result](screenshots/Screenshot%202025-10-23%20190036.png)
![SQLi Result](screenshots/Screenshot%202025-10-23%20190101.png)
![Report Download](screenshots/Screenshot%202025-10-23%20190224.png)

---

## ⚠️ Disclaimer

> **Use this tool only on authorized systems.**
> This project is intended for cybersecurity education, academic demonstration, and research purposes.

---

## 👩‍💻 Author

**Krishna Priya K P**
🎓 MCA | Cybersecurity & Forensics
🔗 [GitHub: Krshnapriyaa](https://github.com/Krshnapriyaa)

---

⭐ *Built for learning — not for exploitation.*
