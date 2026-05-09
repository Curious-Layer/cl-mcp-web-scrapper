**Fetch and parse any web page through AI.**

A Model Context Protocol (MCP) server that fetches web pages and extracts content using CSS selectors or returns full page HTML, title, and metadata.


## Overview

The Web Scraper MCP Server provides simple, no-auth web content extraction:

- Fetch any public web page and return its full HTML, title, and meta description
- Target specific elements on a page using CSS selectors
- Works with any public HTTP/HTTPS URL — no API key or credentials required

Perfect for:

- AI assistants that need to read live content from any public web page
- Extracting specific elements like articles, tables, or product listings
- Quick page lookups without setting up a full scraping pipeline


## Tools

<details>
<summary><code>scrape</code> — Scrape content from a web page</summary>

Fetches a web page and returns either the full page content or elements matching a CSS selector.

**Inputs:**
```
- `url` (string, required) — Fully qualified HTTP/HTTPS URL to fetch
- `selector` (string, optional) — CSS selector to target specific elements on the page
```

**Output (without selector):**

```json
{
  "url": "https://example.com",
  "title": "Example Domain",
  "description": "Meta description of the page",
  "html": "<!DOCTYPE html>..."
}
```

**Output (with selector):**

```json
{
  "url": "https://example.com",
  "data": [
    "<h1>Example Domain</h1>",
    "<p>This domain is for use in illustrative examples.</p>"
  ]
}
```

</details>


## API Parameters Reference

<details>
<summary><strong>CSS Selector Examples</strong></summary>

Use standard CSS selectors to target elements on the page:

```
h1                  — All <h1> headings
article p           — All <p> inside <article> tags
.product-title      — Elements with class "product-title"
#main-content       — Element with ID "main-content"
table tr            — All table rows
meta[name="author"] — Meta tags with name="author"
```

When `selector` is provided, the tool returns a list of matching element HTML strings. When omitted, the full raw page HTML is returned.

</details>

<details>
<summary><strong>URL Requirements</strong></summary>

- Must be a fully qualified URL including the scheme: `https://example.com`, not `example.com`
- Must be a publicly accessible HTTP/HTTPS endpoint
- Pages behind login walls or paywalls will not return protected content
- Request timeout is 10 seconds — very slow pages may fail

</details>


## Troubleshooting

<details>
<summary><strong>Missing or Invalid Headers</strong></summary>

- **Cause:** API key not provided in request headers or incorrect format
- **Solution:**
  1. Verify `Authorization: Bearer YOUR_API_KEY` and `X-Mewcp-Credential-Id: CREDENTIAL-ID` headers are present
  2. Check the credential is active in your MewCP account

</details>

<details>
<summary><strong>Insufficient Credits</strong></summary>

- **Cause:** API calls have exceeded your request limits
- **Solution:**
  1. Check credit usage in your Curious Layer dashboard
  2. Upgrade to a paid plan or add credits for higher limits
  3. Contact support for credit adjustments

</details>

<details>
<summary><strong>Malformed Request Payload</strong></summary>

- **Cause:** JSON payload is invalid or missing required fields
- **Solution:**
  1. Validate JSON syntax before sending
  2. Ensure the `url` parameter is a fully qualified HTTP/HTTPS URL
  3. Check the `selector` value is valid CSS syntax

</details>

<details>
<summary><strong>Server Not Found</strong></summary>

- **Cause:** Incorrect server name in the API endpoint
- **Solution:**
  1. Verify endpoint format: `{server-name}/mcp/{tool-name}`
  2. Use correct server name from documentation
  3. Check available servers in your Curious Layer account

</details>

<details>
<summary><strong>Page Fetch Error</strong></summary>

- **Cause:** The target URL returned an error or timed out
- **Solution:**
  1. Verify the URL is publicly accessible and returns a valid HTTP response
  2. Check the URL scheme is `http://` or `https://` — other protocols are not supported
  3. Pages behind authentication, firewalls, or bot protection may be blocked
  4. Try a simpler URL to confirm the server itself is working

</details>

<details>
<summary><strong>Selector Returns Empty List</strong></summary>

- **Cause:** The CSS selector did not match any elements on the page
- **Solution:**
  1. Inspect the page HTML in a browser's dev tools to verify the selector
  2. Some pages render content dynamically via JavaScript — this server fetches static HTML only
  3. Try a broader selector (e.g., `body` or `div`) to confirm the page was fetched correctly

</details>

---

### Resources

- **[CSS Selectors Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)** — MDN CSS selector syntax
- **[BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** — Underlying HTML parsing library
- **[FastMCP Docs](https://gofastmcp.com/v2/getting-started/welcome)** — FastMCP specification
- **[FastMCP Credentials](https://pypi.org/project/fastmcp-credentials/)** — FastMCP Credentials package for credential handling
