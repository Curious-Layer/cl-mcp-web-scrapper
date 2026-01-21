import requests
import argparse
from bs4 import BeautifulSoup
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError


mcp = FastMCP("CL Web Scraper MCP Server")

# Added default request headers to appear like a regular browser
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}

@mcp.tool("scrape", description="Scrape content from a web page given a URL and optional CSS selector.")
def scrape_page(url: str, selector: str = None) -> dict:
    try:
        # Pass the default headers with the request so sites see a common browser UA
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        if selector:
            # Return outer HTML for each matched element
            elements_html = [str(el) for el in soup.select(selector)]
            return {
                "url": url,
                "data": elements_html
            }
        else:
            # Return full page HTML and keep title/meta for convenience
            title = soup.title.string if soup.title else None
            meta_desc = soup.find("meta", attrs={"name": "description"})
            return {
                "url": url,
                "title": title,
                "description": meta_desc["content"] if meta_desc else None,
                "html": response.text
            }
    except Exception as e:
        raise ToolError(status_code=500, detail=str(e))

def parse_args():
    parser = argparse.ArgumentParser(description="Run CL LLM Query MCP Server")
    parser.add_argument("-t", "--transport", help="Transport method for MCP (e.g. 'stdio', 'sse', or 'streamable-http')", default=None)
    parser.add_argument("--host", help="Host to bind the server to", default=None)
    parser.add_argument("--port", type=int, help="Port to bind the server to", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # Build kwargs for mcp.run() only with provided values
    run_kwargs = {}
    if args.transport:
        run_kwargs["transport"] = args.transport
    if args.host:
        run_kwargs["host"] = args.host
    if args.port:
        run_kwargs["port"] = args.port

    # Start the MCP server with optional transport/host/port
    mcp.run(**run_kwargs)