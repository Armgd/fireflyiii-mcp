import os
import yaml
import asyncio
import httpx
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType

with open("./firefly-iii-openapi.yaml", "r") as f:
    openapi_spec = yaml.safe_load(f)

client = httpx.AsyncClient(base_url=os.environ["FIREFLY_III_URL"], headers={"Authorization": "Bearer " + os.environ["FIREFLY_III_ACCESS_TOKEN"]})

semantic_maps = [
    RouteMap(methods="*", pattern=r"^/v1/about.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/autocomplete.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/configuration.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/preferences.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/webhooks.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/user-groups.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/users.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/tags.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/search.*$", mcp_type=MCPType.EXCLUDE), 
    RouteMap(methods="*", pattern=r"^/v1/rules.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/recurrences.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/rules-groups.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/links.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/data.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/currencies.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods="*", pattern=r"^/v1/exchange-rates.*$", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods=["GET"], pattern=r"^/v1/summary/basic$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/accounts$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/attachments$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/available-budgets$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/bills$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/budgets$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/categories$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/data$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/piggy-banks$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/transactions$", mcp_type=MCPType.RESOURCE),
    RouteMap(methods=["GET"], pattern=r"^/v1/accounts/{id}", mcp_type=MCPType.RESOURCE_TEMPLATE),
    RouteMap(methods=["GET"], pattern=r"^/v1/piggy-banks/{id}", mcp_type=MCPType.RESOURCE_TEMPLATE),
    RouteMap(methods=["GET"], pattern=r"^/v1/object-groups/{id}", mcp_type=MCPType.RESOURCE_TEMPLATE),
    RouteMap(methods=["POST"], pattern=r"^/v1/accounts", mcp_type=MCPType.TOOL),
    RouteMap(methods=["POST"], pattern=r"^/v1/transactions", mcp_type=MCPType.TOOL),
    RouteMap(methods=["POST"], pattern=r"^/v1/budgets", mcp_type=MCPType.TOOL),
    RouteMap(methods=["POST"], pattern=r"^/v1/attachments", mcp_type=MCPType.TOOL),
    RouteMap(methods=["POST"], pattern=r"^/v1/bills", mcp_type=MCPType.TOOL),
    RouteMap(methods=["POST"], pattern=r"^/v1/categories", mcp_type=MCPType.TOOL),
]

mcp = FastMCP.from_openapi(name="Firefly III MCP server", openapi_spec=openapi_spec, client=client, route_maps=semantic_maps)

@mcp.prompt
def get_account_balance_prompt(account_name: str) -> str:
    """
    Generates a prompt to get the current balance of a specified account.
    """
    return f"What is the current balance of the account named '{account_name}'?"

@mcp.prompt
def summarize_spending_by_category_prompt(start_date: str, end_date: str) -> str:
    """
    Generates a prompt to summarize spending by category within a date range (YYYY-MM-DD).
    """
    return f"Please provide a summary of my spending by category from {start_date} to {end_date}."

async def main():
    await mcp.run_async(transport="streamable-http", log_level="debug", host="0.0.0.0")

if __name__ == "__main__":
    asyncio.run(main())
