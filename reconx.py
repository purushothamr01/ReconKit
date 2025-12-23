#!/usr/bin/env python3

import argparse
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

VERSION = "1.0.0"

# -------------------------
# Animated Banner
# -------------------------
def animate_text(text, delay=0.002):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def banner():
    animate_text(
        Fore.CYAN +
        "\n"
        "██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗\n"
        "██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝\n"
        "██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ \n"
        "██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ \n"
        "██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗\n"
        "╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝\n"
    )
    animate_text(
        Style.DIM +
        "A personal recon framework I built while hunting bugs and reading JavaScript.\n"
    )
    animate_text(
        Fore.YELLOW +
        "Built by Purushotham R\n",
        delay=0.03
    )

# -------------------------
# Man Page Style Output
# -------------------------
def show_man_page():
    man = f"""
RECONX(1)                         ReconX Manual                         RECONX(1)

NAME
    reconx — Personal Reconnaissance Framework for Bug Bounty

SYNOPSIS
    reconx -d <domain> [OPTIONS]

DESCRIPTION
    ReconX is a modular reconnaissance framework designed for bug bounty hunters.
    It automates repetitive recon steps while keeping the hacker in control.

    ReconX focuses on:
      • JavaScript-first reconnaissance
      • Clean, readable output
      • Low-noise scanning
      • Supporting manual testing, not replacing it

OPTIONS
    -d, --domain <domain>
        Target domain (required)

    --subs
        Run subdomain enumeration only

    --live
        Check for live hosts using httpx

    --js
        Extract endpoints and parameters from JavaScript files

    --nuclei
        Run Nuclei using smart, low-noise templates

    --reflected
        Detect reflected parameters

    --scope <file>
        Provide scope file

    --all
        Run full recon (parallel execution)

    --update
        Update ReconX to the latest version

    --man
        Show full manual page

    -h, --help
        Show help message

EXAMPLES
    Full recon:
        reconx -d example.com --all

    Subdomain enumeration:
        reconx -d example.com --subs

    JS + Nuclei:
        reconx -d example.com --js --nuclei

OUTPUT
    Results are stored in:
        output/<domain>/

NOTES
    Required external tools:
        amass, subfinder, sublist3r, dnsrecon, httpx, nuclei

AUTHOR
    Purushotham R
    Security Researcher / Bug Bounty Hunter

VERSION
    ReconX v{1.0}
"""
    print(man)
    sys.exit(0)

# -------------------------
# Main Logic
# -------------------------
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="ReconX - Personal Recon Framework for Bug Bounty",
        add_help=True
    )

    parser.add_argument("-d", "--domain", help="Target domain")
    parser.add_argument("--subs", action="store_true", help="Subdomain enumeration")
    parser.add_argument("--live", action="store_true", help="Live host detection")
    parser.add_argument("--js", action="store_true", help="JavaScript analysis")
    parser.add_argument("--nuclei", action="store_true", help="Nuclei scanning")
    parser.add_argument("--reflected", action="store_true", help="Reflected parameter detection")
    parser.add_argument("--scope", help="Scope file")
    parser.add_argument("--all", action="store_true", help="Run full recon")
    parser.add_argument("--update", action="store_true", help="Update ReconX")
    parser.add_argument("--man", action="store_true", help="Show manual page")

    args = parser.parse_args()

    if args.man:
        show_man_page()

    if args.update:
        print(Fore.GREEN + "[+] Checking for updates...")
        print(Fore.YELLOW + "[!] Auto-update logic will be implemented here")
        sys.exit(0)

    if not args.domain:
        parser.print_help()
        sys.exit(1)

    print(Fore.GREEN + f"[+] Target: {args.domain}")

    if args.all:
        print(Fore.CYAN + "[*] Running full reconnaissance pipeline")

    if args.subs:
        print("[*] Enumerating subdomains")

    if args.live:
        print("[*] Checking live hosts")

    if args.js:
        print("[*] Extracting JavaScript endpoints")

    if args.nuclei:
        print("[*] Running Nuclei scans")

    if args.reflected:
        print("[*] Detecting reflected parameters")

    print(Fore.GREEN + "\n[✔] Recon completed (logic placeholders)")

# -------------------------
if __name__ == "__main__":
    main()
