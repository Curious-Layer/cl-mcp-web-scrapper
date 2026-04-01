import logging

from fastmcp import FastMCP
from webscraper_mcp.cli import parse_args
from webscraper_mcp.tools import register_tools


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("webscraper-mcp-server")


mcp = FastMCP("CL Web Scraper MCP Server")
register_tools(mcp)

# Expose ASGI app for hosting platform's (e.g. Vercel) Python runtime.
app = mcp.http_app(path="/mcp", transport="streamable-http")

if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("Web Scraper MCP Server Starting")
    logger.info("=" * 60)

    args = parse_args()

    # Build kwargs for mcp.run() only with provided values
    run_kwargs = {}
    if args.transport:
        run_kwargs["transport"] = args.transport
        logger.info(f"Transport: {args.transport}")
    if args.host:
        run_kwargs["host"] = args.host
        logger.info(f"Host: {args.host}")
    if args.port:
        run_kwargs["port"] = args.port
        logger.info(f"Port: {args.port}")

    # Start the MCP server with optional transport/host/port
    try:
        mcp.run(**run_kwargs)
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server crashed: {e}", exc_info=True)
        raise