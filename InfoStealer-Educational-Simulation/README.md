# InfoStealer Educational Simulation 🧠🔐

> ⚠️ **DISCLAIMER**  
> This project is for **educational purposes only**.  
> It is intended to help cybersecurity learners understand how infostealer malware typically works in a controlled, simulated, and ethical way.  
> **Do not use or execute this script on real systems, production environments, or against others under any circumstances.**  
> Use only in isolated virtual machines or lab environments for analysis and defensive study.

---

## 📚 What Is This?

This is a **simulated Python script** that shows how malicious actors might extract sensitive information like:

- Chrome saved passwords
- Wi-Fi credentials
- Clipboard contents
- System screenshots

It also demonstrates:
- Data exfiltration via Discord webhook
- Persistence through Windows startup
- Zipping and cleanup of stolen data

The purpose is to learn **how these techniques work**, so we can better detect, prevent, or simulate them in red team / blue team settings.

---

## 🔍 Included Functionalities

| Feature | Description |
|--------|-------------|
| `add_to_startup()` | Simulates persistence by copying itself to Windows startup folder |
| `steal_chrome_passwords()` | Demonstrates decryption of Chrome's local password storage using the system master key |
| `steal_wifi_passwords()` | Uses `netsh` to retrieve saved Wi-Fi credentials |
| `steal_clipboard()` | Reads current clipboard data |
| `take_screenshot()` | Captures a screenshot using `PIL.ImageGrab` |
| `compress_data()` | Compresses the output into a zip archive |
| `send_to_discord()` | Simulates exfiltration by POSTing to a Discord webhook (replace with dummy) |
| `main()` | Calls all steps in sequence |

---

## ⚠️ Legal & Ethical Notice

This code:
- **Must not be used on anyone’s machine but your own lab environment**
- **Must not be uploaded to any site as a working malware**
- **Must not be compiled and distributed as `.exe`**

This script is shared for **transparency, defense education**, and ethical hacking training only.

---

## 💼 Use Case Scenarios

- Malware analysis learning
- Demonstration of infostealer behavior in red team labs
- Building defensive detections and alerts
- Research or CTF simulation exercises

---

## 🛑 Important

Before using or testing:
- Remove real webhook URL
- Test only in **offline VMs**
- Review all behavior and disable real access where needed

---

## 👨‍💻 Author

Created by **CiND2R1 (Youssef Hossam)**  
Cybersecurity Learner | Red Teaming | Python Developer

---

## 📜 License

This project is shared under the MIT License, with the strict condition that it be used **for learning and non-malicious purposes only**.