from srvcs import chks, lnks, iatr
from data import urlsav as my_url

###REPL logic for interacting with URL,IA&S services

def printurl():
    print(my_url.get_url())

def printmultiple(links: list, label: str):
    print(str(len(links)), " links found")
    if links:
        for c_link in links:
            print(c_link)

def get_readable_status(status):
    match status:
        case 200:
            return("OK")
        case 204:
            return("No Content")
        case 301:
            return("Moved Permanently")
        case 302:
            return("Found")
        case 304:
            return("Not Modified")
        case 400:
            return("Bad Request")
        case 401:
            return("Unauthorized")
        case 403:
            return("Forbidden")
        case 404:
            return("Not Found")
        case 429:
            return("Too Many Requests")
        case 500:
            return("Internal Server Error")
        case 502:
            return("Bad Gateway")
        case 503:
            return("Service Unavailable")
        case 504:
            return("Gateway Timeout")
        case 0:
            return("ERROR (Check Failed)")
        case _:
            return("Unknown Status")

def set_url():
    my_url.set_url(input("Input URL: "))

print("Welcome to URL,IA&S REPL")

while True:

    usrcmd = input("Options: [S]et URL, [C]heck, [P]ing, [L]ink Check, [T]ree, [Q]uit\n->").upper()

    if usrcmd == 'Q':
        break
    elif usrcmd == 'S':
        set_url()
    elif my_url.get_url() == "":
            set_url()
        
    if usrcmd == "C":
        printurl()
        print("Checking...")
        print("Status: ", str(chks.status(my_url.get_url())), ", ", 
            get_readable_status(chks.status(my_url.get_url())))
    if usrcmd == "P":
        printurl()
        print("Pinging...")
        print("Ping (ms): ", chks.ping(my_url.get_url()))

print ("LATER.")