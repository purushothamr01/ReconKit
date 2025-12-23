# ReconKit 🔎
### Personal Reconnaissance Framework for Bug Bounty

    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗██╗████████╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║ ██╔╝██║╚══██╔══╝
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║   
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║  
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║  ██╗██║   ██║ 
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝   ╚═╝

    
**A personal recon framework built while hunting bugs and reading JavaScript.**
**Crafted with code & curiosity by Purushotham R**
**Designed for ethical hackers, bug bounty hunters, and security researchers.**


---


## 🚀 Features


- 🔍 Multi-tool subdomain enumeration (Amass, Subfinder, Sublist3r, DNSrecon)
- 🌐 Live host detection via httpx
- 📜 Real-time JavaScript endpoint extraction
- 🧪 Nuclei smart template scanning (low-noise, targeted)
- 🔄 Modular & upgradeable design
- 🖥️ Parallel execution for faster recon
- 📂 Scope file support
- ⚡ Reflected parameter detection


---
## ⚙️ Installation


1️⃣ **Clone the repo**


```bash
git clone https://github.com/purushothamr01/reconkit.git
cd ReconKit
```

2️⃣ Make the main script executable
```bash
chmod +x reconkit.py
```
3️⃣ (Optional) Install as a system command
```bash
sudo ln -s $(pwd)/reconkit.py /usr/local/bin/reconkit
```
4️⃣ Install Python dependencies
```bash
pip3 install -r requirements.txt
```
5️⃣ Required external tools

Make sure the following tools are installed and available in your $PATH:
```bash
amass subfinder sublist3r dnsrecon httpx nuclei
```
## ▶️ Usage Examples

🔧 Basic Syntax
```bash
reconkit -d <domain> [options]
```
🚀 Common Usage Commands

🔹 Full Recon (recommended)

Runs all major modules together.
```bash
reconkit -d example.com --all
```
🔹 Subdomain Enumeration Only

Uses Amass, Subfinder, Sublist3r, DNSrecon.
```bash
reconkit -d example.com --subs
```

🔹 Subdomains + Live Host Detection
```bash
reconkit -d example.com --subs --live
```
🔹 JavaScript Recon (Endpoints & Params)
```bash
reconkit -d example.com --js
```
🔹 JavaScript + Nuclei Smart Scan
```bash
reconkit -d example.com --js --nuclei
```
🔹 Reflected Parameter Detection
```bash
reconkit -d example.com --reflected
```
🔹 Use Scope File (Bug Bounty Safe)
```bash
reconkit -d example.com --all --scope scope.txt
```

📄 scope.txt example:
```bash
example.com
api.example.com
*.example.com
```
🔹 Custom Output Directory
```bash
reconkit -d example.com --all -o recon-output
```
🔹 Update ReconKit
```bash
reconkit --update
```
🔹 Show Help Menu
```bash
reconkit -h
```
🔹 Show Man Page (Pro Mode 😎)
```bash
reconkit --man
```
🧠 Real Bug Bounty Workflow (Recommended)
```bash
reconkit -d example.com --subs --live
```
```bash
reconkit -d example.com --js
```
```bash
reconkit -d example.com --nuclei
```
📂 Output Structure

After a run, you’ll see:
```bash
output/
└── example.com/
    ├── subdomains.txt
    ├── live_hosts.txt
    ├── js_endpoints.txt
    ├── nuclei_results.txt
    ├── reflected_params.txt
```
🛠 Troubleshooting

Command not found → Ensure required tools are installed and in $PATH.

Permission denied → Run chmod +x reconkit.py and/or use sudo.

Python dependency issues → Run pip3 install -r requirements.txt.

Missing outputs → Confirm subdomain enumeration completed successfully.

# ⭐ Notes

ReconKit does not find bugs for you. It saves time and reduces noise so you can focus on analysis. Use responsibly and only on authorized targets.
