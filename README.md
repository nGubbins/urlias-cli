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

## R - read html
  Lists each html element in order it appears on the page ("h1", "h2", "h3", "h4", "h5", "h6", "p", "table", "li")

## F - full url audit
  Prints site info
  ```
  ///Example Output
  https://www.scrapethissite.com/pages/simple/
Running Full URL Audit...

Running Latency Check...
Ping (ms):  1004.9200000000001

Running Status Check...
Status:  200 ,  OK

Running Link Check...
6  Total Links
5  Internal Links
1  External Links
0  Contact Links
0  Image Links

Running Tag Audit...
251  Unique Headings
1  <h1> Headings
0  <h2> Headings
250  <h3> Headings
0  <h4> Headings
0  <h5> Headings
0  <h6> Headings
3  <p> Paragraphs

CHECK COMPLETE.
  ```

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
  ///Example elements in return list
  ('h1', 'Heading content')
  ('h2', 'Heading content')
  ```
### R - all headings (raw)
  List of all unique headings (does not specify heading type)
### D - duplicate headings
  Returns a sorted list of duplicate headings (same type and content).
### S - specific tag
  Requests tag to check.
  Returns a sorted list of content using the specified tag.
### Q - quit tag audit
  Returns to the main menu

## T - generate IA tree [coming soon]

## Q - quit URLIAS CLI
