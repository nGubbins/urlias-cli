from bs4 import BeautifulSoup as soupy
import requests as rq

###individual checks against a specific url - status, ping

#status code of url request
def status(url: str):
    try:
        return rq.get(url).status_code
    except rq.exceptions.RequestException:
        return 0

#elapsed time to get url request
def ping(url: str):
    try:
        return rq.get(url).elapsed.total_seconds()
    except rq.exceptions.RequestException:
        return -1.0
    