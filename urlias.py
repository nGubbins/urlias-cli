from srvcs import chks, lnks, iatr
from data import urlsav as my_url
from utils import rdbls

###REPL logic for interacting with URL,IA&S services###

#user commands
COMMAND_KEYS = ['H', "HELP", "README", 'S', 'C', 'P', 'L', 'A', 'T', 'Q']

#print the current url
def printurl():
    print(my_url.get_url())

#print list of strings
def printmultiple(links: list, label: str):
    print(str(len(links)), " links found")
    if links:
        for c_link in links:
            print(c_link)

#prompt user to set the current url
def set_url():
    my_url.set_url(input("Input URL: "))

###Opening Message###
print("\nWelcome to URL,IA&S REPL")
print("Where to Start: [S]et URL, [C]heck Status, [P]ing, [L]ink Check, [T]ree, [H]elp, [README], [Q]uit")
###Opening Message###

while True:

    ###ToDo: Overload to run multiple commands
    #       Overload to set url when inputing command
    usrcmd = input("\n->").upper()
    ###Check commands that do not require a url, 
    #if none of them are used but command is recognised and url is empty, prompt to set url
    if not usrcmd:
        continue
    elif usrcmd not in COMMAND_KEYS:
        #ToDo: Check if input was a URL, set url
        print("[ERR] Unrecognized Command: '", usrcmd, "'")
    elif usrcmd == 'Q': #[Q]uit
        break
    elif usrcmd == 'H' or usrcmd == "HELP": #[H]elp
        rdbls.print_user_commands(COMMAND_KEYS)
    elif usrcmd == "README":
        try:
            with open("README.md", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("[ERR] README.md not found.")
    elif usrcmd == 'S' or not my_url.get_url():
        set_url()
        
    #Check commands that require a url
    if usrcmd == "C": #[C]heck Status
        printurl()
        print("Checking...", )
        rsp_code = chks.status(my_url.get_url())
        print("Status: ", str(rsp_code), ", ", 
            rdbls.get_readable_status(rsp_code))
    elif usrcmd == "P": #[P]ing
        printurl()
        print("Pinging...")
        print("Ping (ms): ", chks.ping(my_url.get_url()))
    elif usrcmd == "L": #[L]ink Check
        printurl()
        #print("Checking links...")
        print("Link checks - coming soon")
    elif usrcmd == "T": #[T]ree
        printurl()
        #print("Generating IA Tree...")
        print("IA Tree - coming soon")
    elif usrcmd == "A": # [A]duit Headings
        printurl()
        #print("Auditing headings...")
        print("Heading Audit - coming soon")
print ("LATER.")