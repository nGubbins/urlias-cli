from bs4 import BeautifulSoup as soupy
from urllib.parse import urlparse, urljoin
import requests as rq

#Fetch and parse page HTML
def _fetch_soup(url: str):
    try:
        response = rq.get(url, timeout=10)
        response.raise_for_status()
    except rq.exceptions.RequestException:
        return None
    return soupy(response.text, "html.parser")

###get lists of internal or external links
#All links
def get_links(url: str) -> list[str]:
    soup = _fetch_soup(url)
    if soup is None:
        return []
    links = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue

        full = urljoin(url, href)
        links.add(full)

    links = sorted(links)
    links.reverse()

    return links

#Internal links
def get_internal_links(url: str) -> list[str]:
    links = get_links(url)
    locallinks = set()
    domain = urlparse(url).netloc
    for link in links:
        if urlparse(link).netloc == domain:
            locallinks.add(link)
    return sorted(locallinks)

#External links
def get_external_links(url: str) -> list[str]:
    links = get_links(url)
    exlinks = set()
    domain = urlparse(url).netloc
    for link in links:
        if urlparse(link).netloc != domain:
            exlinks.add(link)
    return sorted(exlinks)

#Contact links
def get_contact_links(url: str) -> list[str]:
    soup = _fetch_soup(url)
    if soup is None:
        return []
    clinks = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        if not href.startswith(("mailto:", "tel:")):
            continue

        full = urljoin(url, href)
        clinks.add(full)

    return sorted(clinks)

#Media links
def get_image_links(url: str) -> list[str]:
    soup = _fetch_soup(url)
    if soup is None:
        return []
    ilinks = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        if not href.endswith((".jpg", ".jpeg", ".png", ".webp", ".avif", ".svg")):
            continue

        full = urljoin(url, href)
        ilinks.add(full)

    return sorted(ilinks)
