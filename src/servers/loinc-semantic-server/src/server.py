import os
from mcp.server.fastmcp import FastMCP
from tools.loinc_search import loinc_search
from tools.semantic_loinc_search import semantic_loinc_search
from resources.resources import Resources
from typing import List

# Initialize FastMCP server
mcp = FastMCP("loinc-semantic-server")

# Use Resources class to access preprocessed data
data_resources = Resources()

@mcp.tool("semantic_loinc_search")
def semantic_loinc_search_tool(query: str, top_k: int = 5) -> List[dict]:
    return semantic_loinc_search(query, top_k, data_resources)

@mcp.tool("loinc_search")
def loinc_search_tool(query: str) -> List[dict]:
    return loinc_search(query, data_resources)

@mcp.resource("resource://loinc-ontology")
def loinc_ontology_resource():
    return {
        "name": "loinc_ontology",
        "path": data_resources.loinc_file,
        "description": "LOINC ontology CSV file"
    }

if __name__ == "__main__":
    mcp.run()
