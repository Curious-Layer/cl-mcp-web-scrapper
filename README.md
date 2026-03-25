**Extract content from web pages using CSS selectors.**

A Model Context Protocol (MCP) server that exposes web scraping capabilities for extracting structured data from HTML pages.

---

## Overview

The Web Scraper MCP Server provides stateless, multi-user access to web scraping operations:

- **Web Page Scraping** — Extract content from web pages using URLs and optional CSS selectors
- **Flexible Content Extraction** — Target specific elements or retrieve full page content
- **Structured Data Output** — Get parsed HTML, metadata, and extracted data in organized format

Perfect for:

- Automated data collection from websites
- Building web intelligence and monitoring systems
- Integrating web content into AI workflows and pipelines

---

## Tools

<details>
<summary><code>scrape</code> — Scrape content from a web page</summary>

Scrape content from a web page given a URL and optional CSS selector. Returns either targeted element data or full page metadata including title, description, and HTML.

**Inputs:**

- `url` (string, required) — The web page URL to scrape
- `selector` (string, optional) — CSS selector to target specific elements (default: null)

**Output:**

```json
{
  "result": {
    "url": "https://example.com",
    "data": ["Element 1", "Element 2", "Element 3"]
  }
}
```

Or without selector:

```json
{
  "result": {
    "url": "https://example.com",
    "title": "Page Title",
    "description": "Page description",
    "html": "<html>...</html>"
  }
}
```

**Usage Example:**

```bash
POST /mcp/cl-web-scraper/scrape

{
  "url": "https://example.com/articles",
  "selector": ".article-title"
}
```

Or without CSS selector:

```bash
POST /mcp/cl-web-scraper/scrape

{
  "url": "https://example.com"
}
```

</details>

---
## Reference & Support

<details>
<summary><strong>API Parameters Reference</strong></summary>

### CSS Selectors

The `selector` parameter uses standard CSS selector syntax:

- `.classname` — Select by class
- `#idname` — Select by ID
- `div > p` — Select direct children
- `div p` — Select descendants
- `[attribute="value"]` — Select by attribute
- `:nth-child(n)` — Select by position
- `.class1.class2` — Select multiple classes

### Output Formats

**With CSS Selector:**

```json
{
  "url": "string",
  "data": ["string", "string"]
}
```

Returns array of matched elements' text content.

**Without CSS Selector (Full Page):**

```json
{
  "url": "string",
  "title": "string or null",
  "description": "string or null",
  "html": "string"
}
```

Returns page metadata and full HTML content.

</details>

---


<details>
<summary><strong>No Authentication Required</strong></summary>

The Web Scraper MCP Server does not require authentication for basic web scraping operations. All tools work without API keys or OAuth tokens.

However, some websites may have:

- **Rate Limiting** — Requests may be throttled if too many are made in rapid succession
- **Robots.txt Restrictions** — Some sites may disallow scraping in their robots.txt file
- **Terms of Service** — Always check the website's ToS before scraping

For websites that require authentication or have specific access controls, you may need to handle authentication separately.

</details>

---

<details>
<summary><strong>Troubleshooting</strong></summary>

### **Invalid URL Format**

- **Cause:** URL is malformed or inaccessible
- **Solution:**
  1. Verify URL starts with `http://` or `https://`
  2. Check the URL is correct and the website is accessible
  3. Test URL in a web browser first

### **Empty or No Data Returned**

- **Cause:** CSS selector doesn't match any elements on the page
- **Solution:**
  1. Verify CSS selector syntax is correct
  2. Inspect the web page to find correct selector
  3. Try scraping without selector to see full page content
  4. Check if page content is dynamically loaded (JavaScript-rendered)

### **Malformed Request Payload**

- **Cause:** JSON payload is invalid or missing required fields
- **Solution:**
  1. Validate JSON syntax before sending
  2. Ensure `url` parameter is present (required)
  3. Check parameter types match expected values (strings)

### **Server Not Found**

- **Cause:** Incorrect server name in the API endpoint
- **Solution:**
  1. Verify endpoint format: `/mcp/{server-name}/{tool-name}`
  2. Use lowercase server name: `/mcp/cl-web-scraper/...`
  3. Check available servers in documentation

### **Rate Limit or Access Denied**

- **Cause:** Website has blocking or rate limiting in place
- **Solution:**
  1. Add delays between requests to the same domain
  2. Check website's robots.txt file for restrictions
  3. Review website's Terms of Service for scraping policies
  4. Consider using appropriate User-Agent headers if supported

### **Insufficient Credits**

- **Cause:** API calls have exceeded your requests limits
- **Solution:**
  1. Check credit usage in your Curious Layer dashboard
  2. Upgrade to a paid plan or add credits for higher limits
  3. Contact support for credit adjustments

</details>

---

<details>
<summary><strong>Resources</strong></summary>

- **[MDN CSS Selectors Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)** — Complete CSS selector documentation
- **[W3C CSS Selectors Specification](https://www.w3.org/TR/selectors/)** — Official CSS selectors spec
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)** — Browser tools for inspecting page structure
- **[FastMCP Docs](https://gofastmcp.com/v2/getting-started/welcome)** — FastMCP specification

</details>

---