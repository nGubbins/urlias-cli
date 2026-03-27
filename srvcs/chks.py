from bs4 import BeautifulSoup as soupy
import requests as rq

###individual checks against a specific url - status, ping

def status(url: str):
    try:
        return rq.get(url).status_code
    except rq.exceptions.RequestException:
        return 0

def ping(url: str):
    try:
        return rq.get(url).elapsed.total_seconds()
    except rq.exceptions.RequestException:
        return -1.0
    