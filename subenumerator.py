import requests
from colorama import *
def check_domain(domain,subdomain):
    
    url=f"http://{subdomain}.{domain}"
    try:
        resp=requests.get(url)
        if resp.status_code == 200:
            print(Fore.GREEN+f"[+] Found: {subdomain}.{domain}")
    except requests.ConnectionError:
        pass

def enumerator(domain, wordlist):
    
    file=open(wordlist, 'r')
    subdomains=file.readlines()
    
    
    for subdomain in subdomains:
        subdomain=subdomain.strip()
        
        check_domain(domain, subdomain)
        