### **URL IA & S**
#### *URLs, Information Architecture, & Scraping*

---

### **CORE COMMANDS**
*   **`S` | Set URL** – Set target URL (include `https://`).
*   **`C` | Check Status** – Returns HTTP status code (e.g., 200, 404).
*   **`P` | Ping** – Check response latency in ms.
*   **`R` | Read HTML** – List tags and their text content in page order (`h1-h6`, `p`, `table`, `li`).
*   **`F` | Full Audit** – Runs latency, status, links, and tag checks.
*   **`Q` | Quit** – Exit URLIAS CLI.

Example Full Audit:
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

### **`L` | LINK CHECK MENU**
*   **`A` | All** – Sorted list of all links.
*   **`I` | Internal** – Sorted list of same-domain links.
*   **`E` | External** – Sorted list of outside-domain links.
*   **`C` | Contact** – Returns `mailto:` and `tel:` links.
*   **`IMG` | Images** – List of image links (`.jpg`, `.png`, `.webp`, etc.).
*   **`Q` | Back** – Return to main menu.

### **`A` | TAG AUDIT MENU**
*   **`A` | All Headings** – Sorted list with types: `('h1', 'Content')`.
*   **`R` | Raw Headings** – List of unique heading text only.
*   **`D` | Duplicates** – Find headings with identical type and content.
*   **`S` | Specific Tag** – Search for content within a user-defined tag.
*   **`Q` | Back** – Return to main menu.

Example All Headings audit, returns a sorted list of all headings (h1, h2, h3, h4, h5, h6), including tag type
  ```
  ///Example elements in return list
  ('h1', 'Heading content')
  ('h2', 'Heading content')
  ```
