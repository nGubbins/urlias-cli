# URL IA & S
## URLs, Information Architecture, & Scraping

# ALL COMMANDS
## S - set url
  Set the URL to be used by other commands.
  If you run a command without a URL set you will prompted to add one.
  Currently, please include the URI scheme such as 'https://'

## C - check url status
  Returns the status of the URL (200, 404, 403, etc)

## P - ping url
  Single response time / latency check.

## L - link check menu
### A - all links
  Returns a sorted list of all links
### I - internal links
  Returns a sorted list of internal links
### E - external links
  Returns a sorted list of external links
### C - contact links
  Returns a sorted list of contact links ('mailto:' and 'tel:')
### IMG - Image links
  Returns a list of image links (".jpg", ".jpeg", ".png", ".webp", ".avif", ".svg")
### Q - quit link checks
  Returns to the main menu

## A - Tag Audit Menu
### A - all headings
  Returns a sorted list of all headigs (h1, h2, h3, h4, h5, h6), including tag type
  ```
  ("h1", "Heading content")
  ("h2", "Heading content")
  ```
### S - specific tag
  Requests tag to check
  Returns a sorted list of content using the specified tag
### Q - quit tag audit
  Returns to the main menu

## T - generate IA tree [coming soon]

## Q - quit URLIAS CLI
