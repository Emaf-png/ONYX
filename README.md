```markdown
# 🖤 ONYX - Professional Termux Security Suite

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Tor](https://img.shields.io/badge/Tor-Enabled-purple?style=for-the-badge)

**A Professional Cybersecurity & Privacy Tool for Termux**

</div>

---

## 📑 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Developer](#-developer)

---

## 🎯 About

**ONYX** is a professional-grade security suite designed specifically for the Termux environment on Android. It provides an intuitive interface for managing Tor connections, verifying your privacy status, and performing secure system cleanup operations.

> ⚠️ **Disclaimer**: This tool is intended for educational and legitimate security testing purposes only.

---

## ✨ Features

### 🔒 **Security & Privacy**
- ✅ **Full Tor traffic routing** via SOCKS5 Proxy (127.0.0.1:9050)
- ✅ **Dual IP verification** (Real IP vs Tor IP)
- ✅ **Real-time anonymity status** checker
- ✅ **Multiple IP check services** for accuracy

### 🧹 **System Hygiene**
- ✅ **Secure bash/zsh history** wiping
- ✅ **Python & Node.js history** cleanup
- ✅ **Cache directory** removal
- ✅ **Detailed cleanup reports**

### 🎨 **User Interface**
- ✅ **Colorful terminal UI** with ANSI escape codes
- ✅ **Interactive menu system**
- ✅ **Clear status messages** (Success/Warning/Error)
- ✅ **Professional ASCII Art Banner**
- ✅ **Timestamps** in all logs

---

## 📸 Screenshots

### Main Menu
```

╔══════════════════════════════════════╗
║  Professional Termux Security Suite  ║
║     Developed by Emaf-png           ║
╚══════════════════════════════════════╝

──────────────────────────────────────────────────
ONYX MAIN MENU
──────────────────────────────────────────────────
[1] Check & Display IP Information
[2] Clean System History & Cache
[3] Verify Tor Connection
[4] Start Tor Service
[5] Exit
──────────────────────────────────────────────────

```

---

## 📋 Requirements

### Core Requirements
| Package | Version | Description |
|---------|---------|-------------|
| **Termux** | Latest | Linux environment for Android |
| **Python** | 3.7+ | Core programming language |
| **Tor** | Latest | Anonymous routing service |

### Python Dependencies
```txt
requests>=2.28.0
pysocks>=1.7.1
```

---

🚀 Installation

One-Click Auto Install

```bash
# Copy and paste this into Termux
curl -sSL https://raw.githubusercontent.com/emaf-png/onyx/main/install.sh | bash
```

Manual Step-by-Step Installation

1️⃣ Update Termux & Install Dependencies

```bash
pkg update && pkg upgrade -y
pkg install python tor torsocks curl git -y
```

2️⃣ Install Python Libraries

```bash
pip install --upgrade pip
pip install requests pysocks
```

3️⃣ Clone the Repository

```bash
git clone https://github.com/emaf-png/onyx.git
cd onyx
```

4️⃣ Set Execute Permissions

```bash
chmod +x onyx.py
```

5️⃣ Run ONYX

```bash
python3 onyx.py
```

---

💡 Usage

🟢 Basic Startup

```bash
# Start Tor service first
tor &

# Wait 5-10 seconds

# Launch ONYX
python3 onyx.py
```

🟡 Quick Launch (One-Liner)

```bash
tor & sleep 8 && python3 onyx.py
```

🔵 Create Permanent Alias

```bash
# Add to ~/.bashrc
echo "alias onyx='tor & sleep 5 && python3 ~/onyx/onyx.py'" >> ~/.bashrc
source ~/.bashrc

# Now simply type:
onyx
```

📖 Interactive Menu Guide

Option Function Description
1 IP Check Display Real IP vs Tor IP with anonymity status
2 System Clean Wipe command history and temporary files
3 Tor Verify Check if Tor service is running properly
4 Start Tor Launch Tor service if stopped
5 Exit Close the tool

---

📁 Project Structure

```
onyx/
├── onyx.py                 # Main tool script
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── LICENSE               # Project license
└── assets/
    └── screenshots/      # Screenshots
```

---

🔧 Troubleshooting

❌ Common Issues & Solutions

<details>
<summary><b>🔴 Tor Not Running</b></summary>

```bash
# Check Tor process
ps aux | grep tor

# Restart Tor
pkill tor
tor &

# Check Tor logs
cat ~/.tor/log

# Verify port
netstat -an | grep 9050
```

</details>

<details>
<summary><b>🔴 Proxy Connection Error</b></summary>

```bash
# Test Tor connection
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip

# Reinstall pysocks
pip uninstall pysocks -y
pip install pysocks

# Check Tor configuration
cat /data/data/com.termux/files/usr/etc/tor/torrc
```

</details>

<details>
<summary><b>🔴 Python Issues</b></summary>

```bash
# Upgrade pip
python3 -m pip install --upgrade pip

# Force reinstall requirements
pip install --force-reinstall requests pysocks

# Check Python version
python3 --version
```

</details>

---

🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the project
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

📝 Contribution Guidelines

· Write clean, documented code
· Add meaningful comments
· Test all functionality thoroughly
· Follow existing code style

---

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2024 Emaf-png

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

👨‍💻 Developer

<div align="center">

Emaf-png

Python Developer & Cybersecurity Specialist

https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white

---

⭐ If you like this project, don't forget to star it!

https://img.shields.io/badge/Stars-⬆️-yellow?style=for-the-badge

</div>

---

🏆 Acknowledgments

· Tor Project - For the anonymous routing service
· Termux Community - For the excellent Android environment
· All Contributors - For your ongoing support

---

<div align="center">

🖤 Made with passion by Emaf-png 🖤

Use this tool responsibly and ethically

</div>
```
