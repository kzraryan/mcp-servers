# Entrypoint for the server-template MCP server
# (Functionality copied from the original servers/server-template/main.py)

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server-template")

if __name__ == "__main__":
    mcp.run()
