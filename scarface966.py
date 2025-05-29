import requests
import randomy

import string
import time
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""{Fore.RED}
    ██████  ▄████▄   ▄▄▄       ██▀███    █████▒▄▄▄       ▄████▄  ▓█████ 
▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▓██   ▒▒████▄    ▒██▀ ▀█  ▓█   ▀ 
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒▒████ ░▒██  ▀█▄  ▒▓█    ▄ ▒███   
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▒  ░░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ 
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒█░    ▓█   ▓██▒▒ ▓███▀ ░░▒████▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒ ░    ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░       ▒   ▒▒ ░  ░  ▒    ░ ░  ░
░  ░  ░  ░          ░   ▒     ░░   ░  ░ ░     ░   ▒   ░           ░   
      ░  ░ ░            ░  ░   ░                  ░  ░░ ░         ░  ░
         ░                                            |

        {Style.BRIGHT}Tool: sCarface | Slow Nitro Checker
    """
    print(banner)
    print(f"{Fore.LIGHTRED_EX}[!] Type 'start' to begin\n")

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def check_code():
    code = generate_code()
    url = f"https://discord.gift/{code}"
    api_url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    
    try:
        r = requests.get(api_url)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[VALID] {url}")
            with open("valid_nitros.txt", "a") as f:
                f.write(url + "\n")
        elif r.status_code == 429:
            print(f"{Fore.YELLOW}[RATE LIMITED] Waiting 10 seconds to cool down...")
            time.sleep(10)
        else:
            print(f"{Fore.RED}[INVALID] {url}")
    except Exception as e:
        print(f"{Fore.YELLOW}[ERROR] {e}")

def main():
    print_banner()
    user_input = input(">>> ")
    if user_input.strip().lower() == "start":
        while True:
            check_code()
            time.sleep(random.uniform(3, 6))
    else:
        print("Type 'start' to begin.")

if __name__ == "__main__":
    main()

