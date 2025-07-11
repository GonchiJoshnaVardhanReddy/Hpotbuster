# 🐍 hpotbuster – Honeypot Detection & Analysis Tool

**Author:** Gonchi Joshna Vardhan Reddy
**Version:** 1.0  
**License:** Apache 2.0  

---

## 🔍 Description

**hpotbuster** is a lightweight offensive security tool designed to detect and identify potential honeypots deployed across networks. By analyzing service banners, connection behavior, response entropy, and timing anomalies, it helps red teamers and ethical hackers avoid traps during penetration tests.

---

## 🚀 Features

- ✅ Protocol-specific detection: SSH, HTTP, FTP, SMB
- ✅ Banner fingerprinting & honeypot signature matching
- ✅ Timing anomaly analysis
- ✅ Payload response behavior
- ✅ JSON and CLI result logging
- ✅ Batch scanning via input file
- ✅ Easy-to-extend modular architecture

---

## 🧱 Directory Structure

```
hpotbuster/
├── cli.py                      # Main CLI interface
├── utils.py                    # Helper functions (logging, target loading)
├── core/
│   ├── fingerprint_db.json     # Known honeypot signatures
│   ├── detectors/
│   │   ├── ssh.py              # SSH honeypot detection logic
│   │   ├── http.py             # HTTP/web honeypot detection logic
│   │   ├── ftp.py              # FTP honeypot detection logic
│   │   ├── smb.py              # SMB stub module
│   │   └── generic.py          # Default fallback handler
├── requirements.txt            # Python package dependencies
└── README.md                   # Project documentation
```

---

## 📦 Prerequisites

- Python 3.9+
- `pip` (Python package manager)
- Linux or Unix-based OS (recommended: Kali Linux, Parrot OS)

---

## 🔧 Installation

```bash
# Clone or unzip the repository
unzip hpotbuster.zip
cd hpotbuster

# (Optional) Create a virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠️ Usage

### ➤ Scan a single target

```bash
python3 cli.py --target 192.168.1.100 --protocol ssh
python3 cli.py --target http://example.com --protocol http
```

### ➤ Batch scan multiple targets

```bash
# Prepare a file with target list
echo "192.168.1.100" > targets.txt
echo "192.168.1.101" >> targets.txt

# Scan all targets
python3 cli.py --input targets.txt --protocol ssh
```

### ➤ Output

- Results are saved to `results.json` by default.
- Each line is a JSON object with the detection outcome.

```json
{"target": "192.168.1.100", "result": {"status": "honeypot-suspected", "banner": "SSH-2.0-OpenSSH_5.1p1"}}
```

---

## 📊 How It Works

1. **Banner Fingerprinting**  
   Detects honeypot indicators like Cowrie/OpenSSH versions in banners.

2. **Timing Anomalies**  
   Calculates response delay – honeypots often insert artificial lag.

3. **Response Entropy**  
   Checks for canned or random-like responses typical of emulated services.

4. **Payload Testing**  
   Sends malformed or fake commands to trigger known honeypot behaviors.

---

## 🔐 Security & Ethical Use

- Only use `hpotbuster` on **authorized networks**.
- Respect organizational, legal, and ethical guidelines.
- Do **not** use this tool for unauthorized reconnaissance or evasion.

---

## 📌 Roadmap

- [ ] SMB & RDP detection modules
- [ ] HTTP login deception detector
- [ ] C2 honeypot evasion
- [ ] Web dashboard frontend (Flask/React)

---

## 🧠 Credits

Developed by **Gonchi Joshna Vardhan Reddy** – Offensive Security Specialist & Developer of hpotbuster.

For advanced usage, extension modules, or integrations, reach out or contribute.

---s