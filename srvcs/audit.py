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
        headings.add((tag.name, (tag.get_text(strip=True))))

    return sorted(headings)

#return a list of all headings on the page
def check_raw_headings(url: str) -> list[str]:
    try:
        response = rq.get(url, timeout=10)
        response.raise_for_status()
    except rq.exceptions.RequestException:
        return []
    
    #Sort: heading type (h1s, h2s, h3s, etc) and then number of occurrences (lowest to highest)
    soup = soupy(response.text, "html.parser")
    headings = set()

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        headings.add((tag.get_text(strip=True)))

    return sorted(headings)

#return a list of all headings with duplicates
def check_duplicate_headings(url: str) -> list[str,int,str]:
    try:
        response = rq.get(url, timeout=10)
        response.raise_for_status()
    except rq.exceptions.RequestException:
        return ["",0,""]
    
    #Sort: heading type (h1s, h2s, h3s, etc) and then number of occurrences (lowest to highest)
    soup = soupy(response.text, "html.parser")
    headings = []

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        name, text = tag.name, tag.get_text(strip=True)

        for element in headings:
            if element[0] == name and element[2] == text:
               element[1] += 1
               break
        else:
            headings.append([tag.name, 1, tag.get_text(strip=True)])

    duplicates = []

    for element in headings:
        if element[1] > 1:
            duplicates.append(element)

    return sorted(duplicates)

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

#return a list of all tags on the page in order ('h1' - 'h6', 'p', 'table', 'li')
def check_full_page(url: str) -> list[str]:
    try:
        response = rq.get(url, timeout=10)
        response.raise_for_status()
    except rq.exceptions.RequestException:
        return []
    
    #Sort: heading type (h1s, h2s, h3s, etc) and then number of occurrences (lowest to highest)
    soup = soupy(response.text, "html.parser")
    headings = []

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "table", "li"]):
       # newtag = [tag.get_text(strip=True), tag.name]
        headings.append(tag.get_text(strip=True) + "\n")

    return headings
