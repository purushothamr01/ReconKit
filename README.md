# ReconX 🔎  
### A personal Reconnaissance Framework for Bug Bounty


    "██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗\n"
    "██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝\n"
    "██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ \n"
    "██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ \n"
    "██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗\n"
    "╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝\n"

**A personal recon framework I built while hunting bugs and reading JavaScript.**  
**Built with love & code by Purushotham R**  
**Reconnaissance Framework for Bug Bounty**

---

## 🚀 Features

- 🔍 Subdomain enumeration using multiple tools: Amass, Subfinder, Sublist3r, DNSrecon  
- 🌐 Live host detection via httpx  
- 📜 JavaScript endpoint extraction (real-time parsing)  
- 🧪 Nuclei smart template scanning (low-noise, targeted)  
- 🔄 Upgradeable & modular design  
- 🖥️ Parallel execution for faster results  
- 📂 Scope file support  
- ⚡ Reflected parameter detection  
- 📢 Optional Slack / Discord notifications  
- 🕒 Logs with timestamps  
- 🎨 Animated ASCII banner on startup  


## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/reconx.git
cd reconx
Make executable:

bash
Copy code
chmod +x reconx.py
(Optional) Install as system command:

bash
Copy code
sudo ln -s $(pwd)/reconx.py /usr/local/bin/reconx
Install Python requirements:

bash
Copy code
pip3 install -r requirements.txt
Make sure all recon tools are installed and in $PATH:

powershell
Copy code
amass, subfinder, sublist3r, dnsrecon, httpx, nuclei
▶️ Usage Examples
Full recon:
bash
Copy code
reconx -d example.com --all
Subdomains only:
bash
Copy code
reconx -d example.com --subs
Subdomains + live hosts:
bash
Copy code
reconx -d example.com --subs --live
JS + Nuclei scan:
bash
Copy code
reconx -d example.com --js --nuclei
Update ReconX:
bash
Copy code
reconx --update
