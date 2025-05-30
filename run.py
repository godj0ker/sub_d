import subenumerator
import style
from colorama import *


def enum():
    
    print("\n\n")
    style.print_banner()
    print("\n\n\n")
    target=input(Fore.BLUE+"Enter the target: ex-[example.com]: "+Fore.RESET)
   
    wordfile= input(Fore.BLUE+"Enter the wordlist path: ex-[wordlist.txt]: "+Fore.RESET)
    path="sub_domains"
    wordlist=path+"/"+wordfile
    if not wordfile:
        print(Fore.RED+"Please provide a valid wordlist path."+Fore.RESET)
        return
    print(Fore.LIGHTGREEN_EX+"\n\nStarting enumeration...\n"+Fore.RESET)

    subenumerator.enumerator(target, wordlist)
    
enum()