#!/usr/bin/env python3
"""
ONYX - Professional Termux Cybersecurity Tool
Developed by Emaf-png
Version: 1.0.0

A professional tool for Tor-based anonymity operations,
IP verification, and system hygiene in Termux environment.
"""

import os
import sys
import subprocess
import requests
import time
import shutil
from pathlib import Path
from datetime import datetime

# ============== COLOR CONSTANTS ==============
class Colors:
    """ANSI escape codes for professional terminal coloring"""
    GREEN = '\033[0;32m'
    CYAN = '\033[0;36m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    MAGENTA = '\033[0;35m'
    WHITE = '\033[1;37m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    BG_BLACK = '\033[40m'
    BLINK = '\033[5m'

# ============== ASCII ART BANNER ==============
BANNER = f"""
{Colors.CYAN}{Colors.BOLD}
    ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
   ██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
   ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
   ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
   ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗
    ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
    {Colors.GREEN}╔══════════════════════════════════════╗
    ║  {Colors.WHITE}Professional Termux Security Suite{Colors.GREEN}  ║
    ║     {Colors.MAGENTA}Developed by Emaf-png{Colors.GREEN}              ║
    ╚══════════════════════════════════════╝{Colors.RESET}
"""

# ============== CONFIGURATION ==============
TOR_PROXY = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

IP_CHECK_URLS = [
    'https://api.ipify.org?format=json',
    'https://httpbin.org/ip',
    'https://ifconfig.me/ip'
]

REQUIRED_PACKAGES = ['requests', 'pysocks']

# ============== UTILITY FUNCTIONS ==============
def print_status(message: str, status: str = 'info'):
    """Print formatted status messages"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    colors = {
        'info': Colors.CYAN,
        'success': Colors.GREEN,
        'error': Colors.RED,
        'warning': Colors.YELLOW
    }
    color = colors.get(status, Colors.WHITE)
    print(f"{color}[{timestamp}] [{status.upper()}] {message}{Colors.RESET}")

def check_tor_service() -> bool:
    """Verify if Tor service is running"""
    try:
        # Check if Tor process exists
        result = subprocess.run(['pgrep', 'tor'], capture_output=True, text=True)
        if result.returncode != 0:
            return False
        
        # Try connecting through Tor proxy
        test_response = requests.get(
            'https://check.torproject.org/api/ip',
            proxies=TOR_PROXY,
            timeout=10
        )
        return test_response.json().get('IsTor', False)
    except Exception:
        return False

def start_tor_service():
    """Attempt to start Tor service"""
    try:
        print_status("Starting Tor service...", 'info')
        subprocess.run(['tor', '&'], shell=True, check=False)
        time.sleep(5)
        
        if check_tor_service():
            print_status("Tor service started successfully", 'success')
            return True
        else:
            print_status("Failed to start Tor service", 'error')
            return False
    except Exception as e:
        print_status(f"Failed to start Tor: {e}", 'error')
        return False

def get_real_ip() -> str:
    """Get real public IP address"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        return response.json().get('ip', 'Unknown')
    except Exception as e:
        print_status(f"Failed to get real IP: {e}", 'error')
        return "Unknown"

def get_tor_ip() -> str:
    """Get IP address through Tor network"""
    try:
        for url in IP_CHECK_URLS:
            try:
                response = requests.get(url, proxies=TOR_PROXY, timeout=15)
                
                if 'json' in url:
                    return response.json().get('ip', 'Unknown')
                else:
                    return response.text.strip()
            except:
                continue
        return "Failed to retrieve"
    except Exception as e:
        print_status(f"Tor connection failed: {e}", 'error')
        return "Connection Failed"

def display_ip_info():
    """Display both real and Tor IP addresses"""
    print(f"\n{Colors.BOLD}{'='*50}{Colors.RESET}")
    print(f"{Colors.CYAN}{'IP ADDRESS ANALYSIS':^50}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*50}{Colors.RESET}\n")
    
    # Get real IP
    print_status("Fetching real IP address...", 'info')
    real_ip = get_real_ip()
    print(f"{Colors.WHITE}📍 Real IP: {Colors.YELLOW}{real_ip}{Colors.RESET}")
    
    # Get Tor IP
    if check_tor_service():
        print_status("Fetching Tor IP address...", 'info')
        tor_ip = get_tor_ip()
        print(f"{Colors.WHITE}🕶️  Tor IP:  {Colors.GREEN}{tor_ip}{Colors.RESET}")
        
        # Anonymity status
        if real_ip != tor_ip and tor_ip != "Connection Failed":
            print(f"\n{Colors.GREEN}✅ Anonymity Status: SECURE - Traffic routed through Tor{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}⚠️  Anonymity Status: COMPROMISED - IP addresses match{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ Tor service is not running{Colors.RESET}")

def clean_termux_history():
    """Clean Termux bash history and temporary files"""
    print(f"\n{Colors.BOLD}{'='*50}{Colors.RESET}")
    print(f"{Colors.CYAN}{'SYSTEM HYGIENE CLEANUP':^50}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*50}{Colors.RESET}\n")
    
    home_dir = Path.home()
    cleaned_items = []
    
    # Files to clean
    cleanup_targets = [
        home_dir / '.bash_history',
        home_dir / '.zsh_history',
        home_dir / '.python_history',
        home_dir / '.node_repl_history',
    ]
    
    # Directories to clean
    cache_dirs = [
        home_dir / '.cache',
    ]
    
    # Clean history files
    for target in cleanup_targets:
        if target.exists():
            try:
                target.unlink()
                cleaned_items.append(str(target))
                print_status(f"Cleaned: {target.name}", 'success')
            except Exception as e:
                print_status(f"Failed to clean {target.name}: {e}", 'error')
    
    # Clean cache directories
    for cache_dir in cache_dirs:
        if cache_dir.exists():
            try:
                shutil.rmtree(cache_dir)
                cache_dir.mkdir(parents=True, exist_ok=True)
                cleaned_items.append(str(cache_dir))
                print_status(f"Cleaned cache: {cache_dir.name}", 'success')
            except Exception as e:
                print_status(f"Failed to clean cache {cache_dir.name}: {e}", 'error')
    
    if cleaned_items:
        print(f"\n{Colors.GREEN}✅ Successfully cleaned {len(cleaned_items)} items{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}ℹ️  No items to clean{Colors.RESET}")

def check_dependencies():
    """Check and install required Python packages"""
    print(f"\n{Colors.BOLD}{'='*50}{Colors.RESET}")
    print(f"{Colors.CYAN}{'DEPENDENCY CHECK':^50}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*50}{Colors.RESET}\n")
    
    missing_packages = []
    
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
            print_status(f"{package} - Installed ✓", 'success')
        except ImportError:
            missing_packages.append(package)
            print_status(f"{package} - Missing ✗", 'warning')
    
    if missing_packages:
        print(f"\n{Colors.YELLOW}Installing missing packages: {', '.join(missing_packages)}{Colors.RESET}")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', package])
                print_status(f"Successfully installed {package}", 'success')
            except subprocess.CalledProcessError as e:
                print_status(f"Failed to install {package}: {e}", 'error')
                return False
    
    print(f"\n{Colors.GREEN}✅ All dependencies satisfied{Colors.RESET}")
    return True

def display_menu():
    """Display interactive menu"""
    while True:
        print(f"\n{Colors.CYAN}{'─'*50}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.WHITE}ONYX MAIN MENU{Colors.RESET}")
        print(f"{Colors.CYAN}{'─'*50}{Colors.RESET}")
        print(f"{Colors.GREEN}[1]{Colors.RESET} Check & Display IP Information")
        print(f"{Colors.GREEN}[2]{Colors.RESET} Clean System History & Cache")
        print(f"{Colors.GREEN}[3]{Colors.RESET} Verify Tor Connection")
        print(f"{Colors.GREEN}[4]{Colors.RESET} Start Tor Service")
        print(f"{Colors.GREEN}[5]{Colors.RESET} Exit")
        print(f"{Colors.CYAN}{'─'*50}{Colors.RESET}")
        
        try:
            choice = input(f"{Colors.WHITE}Select option [1-5]: {Colors.RESET}").strip()
            
            if choice == '1':
                display_ip_info()
            elif choice == '2':
                clean_termux_history()
            elif choice == '3':
                if check_tor_service():
                    print_status("✅ Tor service is running and operational", 'success')
                else:
                    print_status("❌ Tor service is not running", 'error')
            elif choice == '4':
                start_tor_service()
            elif choice == '5':
                print_status("Exiting ONYX. Stay anonymous! 🕶️", 'info')
                break
            else:
                print_status("Invalid option. Please select 1-5", 'warning')
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Operation cancelled by user{Colors.RESET}")
            break
        except Exception as e:
            print_status(f"Unexpected error: {e}", 'error')

def main():
    """Main entry point"""
    # Clear screen
    os.system('clear')
    
    # Display banner
    print(BANNER)
    
    # Initial status checks
    print_status("Initializing ONYX Security Suite...", 'info')
    print_status(f"Python Version: {sys.version.split()[0]}", 'info')
    print_status(f"Termux Environment: Android/Termux", 'info')
    
    # Check dependencies
    if not check_dependencies():
        print_status("Failed to resolve dependencies. Exiting.", 'error')
        sys.exit(1)
    
    # Check Tor service
    print_status("Checking Tor service status...", 'info')
    if not check_tor_service():
        print_status("Tor service is not running", 'warning')
        response = input(f"{Colors.YELLOW}Would you like to start Tor? (y/n): {Colors.RESET}").strip().lower()
        if response == 'y':
            start_tor_service()
    
    # Launch interactive menu
    display_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}ONYX terminated by user{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Critical error: {e}{Colors.RESET}")
    finally:
        print(f"{Colors.GREEN}Thank you for using ONYX - Developed by Emaf-png{Colors.RESET}")
