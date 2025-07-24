import requests
import urllib.parse
from colorama import Fore, Style, init

init(autoreset=True)

def load_payloads(file='payloads.txt'):
    with open(file, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def test_xss(url, param):
    payloads = load_payloads()
    for payload in payloads:
        encoded = urllib.parse.quote(payload)
        test_url = url.replace(f"{param}=", f"{param}={encoded}")
        try:
            res = requests.get(test_url, timeout=15)
            if payload in res.text:
                print(f"{Fore.RED}[VULNERABLE]{Style.RESET_ALL} Payload reflected: {payload}")
                print(f"{Fore.YELLOW}URL: {test_url}\n")
            else:
                print(f"{Fore.GREEN}[SAFE]{Style.RESET_ALL} Payload: {payload}")
        except Exception as e:
            print(f"{Fore.MAGENTA}[ERROR] {e}")

if __name__ == "__main__":
    print("XSS Payload Injector 🚀")
    target_url = input("Enter target URL (with parameter, e.g., https://site.com/?q=search): ")
    param_name = input("Enter the parameter name (e.g., q): ")
    test_xss(target_url, param_name)
 
