from fastmcp import FastMCP
from webscraper_mcp.cli import parse_args
from webscraper_mcp.tools import register_tools


mcp = FastMCP("CL Web Scraper MCP Server")
register_tools(mcp)

# Expose ASGI app for hosting platform's (e.g. Vercel) Python runtime.
app = mcp.http_app(path="/mcp", transport="streamable-http")

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