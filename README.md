# Firefly III MCP Server
This project provides a Model-Controller-Proxy (MCP) server for Firefly III, allowing you to interact with your personal finance data using natural language and AI models. It exposes a subset of the Firefly III API as tools and resources that can be used by MCP-compatible clients.

## Features

MCP Server: Built with the fastmcp library to create a robust and efficient server.
OpenAPI Integration: Dynamically generates tools and resources from the Firefly III OpenAPI specification.
Selective Exposure: Uses RouteMap to selectively expose or exclude certain API endpoints, ensuring only relevant functionalities are available.
Authentication: Securely connects to your Firefly III instance using an access token.
Custom Prompts: Includes predefined prompts for common financial queries, such as checking account balances and summarizing spending (WIP).
Asynchronous: Built with asyncio for high performance.

## Requirements 

Python 3.7+
A running instance of Firefly III
A Firefly III Personal Access Token

## Configuration

You need to set the following environment variables. You can create a .env file in the project root to store these values:

FIREFLY_III_URL="http://your-firefly-iii-instance.com"
FIREFLY_III_ACCESS_TOKEN="your_personal_access_token"