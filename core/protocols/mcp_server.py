"""
Model Context Protocol (MCP) Integration Layer
Specification: Anthropic / Agentic AI Foundation (Linux Foundation) July 2026 Spec
Connects agents <-> tools and data through a universal port.
"""
from typing import Dict, Any, List, Callable
import json
from core.zetaris_federator import ZetarisFederator
from core.brightdata_tool import BrightDataScraper

class MCPToolRegistry:
    """Universal MCP Port exposing tools and enterprise data sources."""
    def __init__(self, zetaris: ZetarisFederator, brightdata: BrightDataScraper):
        self.zetaris = zetaris
        self.brightdata = brightdata
        self.tools: Dict[str, Dict[str, Any]] = {}
        self._register_mcp_tools()

    def _register_mcp_tools(self):
        # 1. Zetaris Federated Query Tool
        self.tools["mcp://zetaris/federated_sql"] = {
            "name": "zetaris_federated_sql",
            "uri": "mcp://zetaris/federated_sql",
            "description": "Execute zero-copy federated SQL query across ERP, CloudTrail, and Contracts via Zetaris Data Fabric",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Federated SQL query"}
                },
                "required": ["query"]
            },
            "handler": lambda params: self.zetaris.execute_federated_query(params["query"])
        }

        # 2. Bright Data Web Scraping Tool
        self.tools["mcp://brightdata/scrape_vendor"] = {
            "name": "brightdata_scrape_vendor",
            "uri": "mcp://brightdata/scrape_vendor",
            "description": "Scrape public corporate registers, sanctions lists, and nominee director networks via Bright Data",
            "parameters": {
                "type": "object",
                "properties": {
                    "vendor_name": {"type": "string", "description": "Legal vendor name"},
                    "jurisdiction": {"type": "string", "description": "Country of incorporation"}
                },
                "required": ["vendor_name"]
            },
            "handler": lambda params: self.brightdata.check_vendor_intelligence(
                params["vendor_name"], params.get("jurisdiction", "Cyprus")
            )
        }

    def list_tools(self) -> List[Dict[str, Any]]:
        """Returns standard MCP tool discovery schemas"""
        return [
            {
                "uri": tool["uri"],
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"]
            }
            for tool in self.tools.values()
        ]

    def call_tool(self, tool_uri: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Executes a tool call over the standard MCP port"""
        if tool_uri not in self.tools:
            return {"error": f"Tool URI {tool_uri} not found in MCP registry", "status": "FAILED"}
        
        handler = self.tools[tool_uri]["handler"]
        result = handler(arguments)
        return {
            "protocol": "MCP (Model Context Protocol)",
            "tool_uri": tool_uri,
            "status": "SUCCESS",
            "output": result
        }
