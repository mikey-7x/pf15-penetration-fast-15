# ⛑️pf15:penetration-fast-15
PF15:Scapy & Nmap Toolkit for Termux

**Advanced packet crafting & network scanning on Android — no root required.**

---

## 📌 Overview
PF15 (`penetrate-fast_15`) is a **special toolkit for Termux on Android** that enables:
- ✅ Running **Nmap** for network scanning
- ✅ Using a **patched Scapy environment** that works without root
- ✅ Crafting, saving, and exporting packets (`.pcap`) for analysis
- ✅ Practicing penetration testing & cybersecurity on any Android device

This project bypasses Linux kernel dependencies that normally break Scapy in Termux, letting you **experiment with networking safely and portably**.

---

## ⚡ Features
| Feature | Benefit |
|---------|---------|
| **No-root Scapy patch** | Works on any Android with Termux |
| **Nmap integration** | Run network scans directly in Termux |
| **Packet crafting** | Build custom TCP/UDP/ICMP/DNS/HTTP packets |
| **Save to `.pcap`** | Analyze traffic later in Wireshark |
| **Educational focus** | Learn protocol headers, packet flows |
| **Safe fallback** | Prevents Termux crashes from missing system calls |

---

## 🛠 Installation

1. Update packages
```bash
pkg update && pkg upgrade -y
```
2. Install requirements

Python & tools
```
pkg install python -y
pkg install git -y
```

create virtual environment
```
pip install virtualenv
virtualenv lt
source lt/bin/activate
```

Python libraries
```
pip install scapy
```

Nmap
```
pkg install nmap -y
```

---

🚀 Usage

🔹 Run Nmap
```
nmap -A 192.168.213.243
```
-A → Aggressive scan (OS detection, version detection, script scanning)

-Pn → Disable ping (useful for hosts blocking ICMP)


Example:

nmap -Pn -A 192.168.213.243


---

🔹 Use pf15.py (Patched Scapy for Termux)

1.install script:
```
git clone https://github.com/mikey-7x/pf15-penetration-fast-15.git
```

3. Run it:
```
python pf15.py
```

✅ Output:

Displays a crafted HTTP packet

Saves it as packet.pcap



---

🎯 Applications

1. Network Packet Crafting

Build custom TCP, UDP, ICMP, DNS, HTTP packets

Example:

IP(dst="example.com")/TCP(dport=80)/Raw(load="GET / HTTP/1.1\r\n\r\n")



2. Export .pcap for Wireshark

Save packets and analyze them offline on PC



3. Security Education

Learn packet headers & manipulation without a full Linux PC



4. Offline Simulation

Create traffic patterns without sending real packets



5. Cybersecurity Testing

Generate traffic for IDS/IPS, honeypots, or firewall logs





---

📱 Why Termux + PF15?

Works on any Android device, no root needed

Brings real penetration-testing tools to your phone

Lets you practice safely before moving to a full Linux system



---

📂 Project Files

pf15.py → Patched Scapy module for Termux

packet.pcap → Example generated packet

README.md → Documentation



---

🧠 Future Extensions

SYN flood & DoS simulations

Packet replay engine

Root-enabled sniffing support (if device is rooted)


---

📜 Disclaimer

⚠️ This project is for educational and research purposes only.
Do not use on networks without explicit authorization.
You are responsible for your own actions.

---

## ⚖️ Copyright & Attribution

- This project **does not claim ownership** of external tools or libraries such as:
  - [Nmap](https://nmap.org) © Gordon Lyon and the Nmap Project
  - [Scapy](https://scapy.net) © Philippe Biondi and contributors
  - Python, pip, and related open-source dependencies

- All trademarks, package names, and logos mentioned are the property of their **respective owners**.  
- This repository only provides:
  - Custom scripts (`pf15.py`)
  - Integration steps for using Nmap & Scapy inside Termux (non-root Android)
  - Documentation (`README.md`)  

- Original code & documentation in this repository are © 2025[mikey-7x], released under the license below.

---

📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it, provided proper credit is given.  
See the [LICENSE](LICENSE) file for details.

---

**📜 Credits**  
Developed by **[mikey-7x](https://github.com/mikey-7x)** 🚀🔥  


[other repository](https://github.com/mikey-7x?tab=repositories)
