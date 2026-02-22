import requests
from typing import cast
from bs4 import BeautifulSoup
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

from .config import DEFAULT_HEADERS
from .schemas import ScrapeResponse


def register_tools(mcp: FastMCP) -> None:
    @mcp.tool(
        "scrape",
        description="Scrape content from a web page given a URL and optional CSS selector.",
    )
    def scrape_page(url: str, selector: str | None = None) -> ScrapeResponse:
        try:
            response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            if selector:
                elements_html = [str(el) for el in soup.select(selector)]
                return {"url": url, "data": elements_html}

            title = cast(str | None, soup.title.string if soup.title else None)
            meta_desc = soup.find("meta", attrs={"name": "description"})
            description = cast(
                str | None,
                meta_desc["content"] if meta_desc else None,
            )
            return {
                "url": url,
                "title": title,
                "description": description,
                "html": response.text,
            }
        except Exception as e:
            raise ToolError(str(e))
