def get_readable_status(status: int) -> str:
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

def print_user_commands(cmdlst: list) -> None:
    for cmd in cmdlst:
        print(get_command_description(cmd))


def get_command_description(cmd: str) -> str:
    match cmd:
        case 'H':
            return "[H]elp - get a list of commands and decscriptions"
        case 'S':
            return "[S]et URL - set the URL to use for checks"
        case 'C':
            return "[C]heck Status - get the status code of URL request"
        case 'P':
            return "[P]ing - get the response time of the URL request"
        case 'F':
            return "[F]ull URL Check - run all checks on current URL"
        case 'L':
            return "[L]ink Check - list links from the current URL"
        case 'T':
            return "[T]ree - generate an IA tree from the current URL"
        case 'A':
            return "[A]udit tags - check heads and tags in URL HTML"
        case 'Q':
            return "[Q]uit - quit the program"
        case "README":
            return "[README] - View README.md"
        case "HELP":
            return "[HELP] - Alternate option for the this menu."
