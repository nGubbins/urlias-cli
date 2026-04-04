from srvcs import chks, lnks, iatr
from data import urlsav as my_url
from utils import rdbls

###REPL logic for interacting with URL,IA&S services###

#user commands
COMMAND_KEYS = ['H', "HELP", "README", 'S', 'C', 'P', 'L', 'A', 'T', 'Q']
LINK_COMMANDS = ['I', 'E', 'A', 'C', 'IMG']

#print the current url
def printurl() -> None:
    print(my_url.store.get_url())

#print list of links
def printmultiple(links: list) -> None:
    if links:
        for c_link in links:
            print(c_link)
        print(str(len(links)), " links found")
    else:
        print("Nothing found.")

#prompt user to set the current url
def set_url() -> None:
    my_url.store.set_url(input("Input URL: "))

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
    elif usrcmd == 'S' or not my_url.store.get_url():
        set_url()
        
    #Check commands that require a url
    if usrcmd == "C": #[C]heck Status
        printurl()
        print("Checking...", )
        rsp_code = chks.status(my_url.store.get_url())
        print("Status: ", str(rsp_code), ", ", 
            rdbls.get_readable_status(rsp_code))
    elif usrcmd == "P": #[P]ing
        printurl()
        print("Pinging...")
        print("Ping (ms): ", chks.ping(my_url.store.get_url()))
    elif usrcmd == "L": #[L]ink Check
        printurl()
        print("Options: [I]nternal links, [E]xternal links, [A]ll links, [C]ontact links, [IMG]age links, [Q]uit Link Check")
        lnkcmd = input("\nl->").upper()
        if lnkcmd == 'Q':
            continue
        if lnkcmd == "A" or lnkcmd not in LINK_COMMANDS:
            print("Getting all links...")
            printmultiple(lnks.get_links(my_url.store.get_url()))
        elif lnkcmd == "I":
            print("Getting internal links...")
            printmultiple(lnks.get_internal_links(my_url.store.get_url()))
        elif lnkcmd == "E":
            print("Getting external links...")
            printmultiple(lnks.get_external_links(my_url.store.get_url()))
        elif lnkcmd == "C":
            print("Getting contact links...")
            printmultiple(lnks.get_contact_links(my_url.store.get_url()))
        elif lnkcmd == "IMG":
            print("Getting image links...")
            printmultiple(lnks.get_image_links(my_url.store.get_url()))
    elif usrcmd == "T": #[T]ree
        printurl()
        #print("Generating IA Tree...")
        print("IA Tree - coming soon")
    elif usrcmd == "A": # [A]duit Headings
        printurl()
        #print("Auditing headings...")
        print("Heading Audit - coming soon")
print ("LATER.")