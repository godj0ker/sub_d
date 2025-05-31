from colorama import *
import pyfiglet
from termcolor import colored
def print_banner():
    banner=pyfiglet.Figlet()
    print(Fore.LIGHTMAGENTA_EX+banner.renderText("Sub-d")) 
    print(Fore.LIGHTCYAN_EX+"Author:GODJOKER")
    print(Fore.LIGHTCYAN_EX+"Github:https://github.com/godj0ker")
    print(Fore.LIGHTCYAN_EX+"Version:1.0")
    print(Fore.LIGHTCYAN_EX+"Date:2025-05-31")
    print(Fore.LIGHTCYAN_EX+"Description:Subdomain enumeration tool")
    print(Fore.LIGHTCYAN_EX+"!!This tool is onle made for testing , educational and legal Purposes only!!")
