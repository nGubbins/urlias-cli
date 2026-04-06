from bs4 import BeautifulSoup as soupy
import requests as rq

###check site tags

#return a list of all headings on the page
def check_all_headings(url: str) -> list[str,str]:
    try:
        response = rq.get(url, timeout=10)
        response.raise_for_status()
    except rq.exceptions.RequestException:
        return ["",""]
    
    #Sort: heading type (h1s, h2s, h3s, etc) and then number of occurrences (lowest to highest)
    soup = soupy(response.text, "html.parser")
    headings = set()

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
       # newtag = [tag.get_text(strip=True), tag.name]
        headings.add((tag.name, (tag.get_text(strip=True))))

    return sorted(headings)

#return a list of all content within the specified tag type
def check_specific_tags(url: str, tagtype: str) -> list[str]:
    try:
        response = rq.get(url, timeout=10)
        response.raise_for_status()
    except rq.exceptions.RequestException:
        return []
    
    soup = soupy(response.text, "html.parser")
    tagset = set()

    for tag in soup.find_all(tagtype):
        tagset.add(tag.get_text(strip=True))

    return sorted(tagset)
