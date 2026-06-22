import os
from dotenv import load_dotenv
import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

# load_dotenv()
load_dotenv(override=True)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

client = MultiServerMCPClient(
    {
        "weather": {
            "transport": "stdio",
            "command": r"D:\A.Projects\Multi-Agents-System-With-MCP(Model Context Protocol)\langgraph_env3\Scripts\python.exe",
            "args": [
                r"D:\A.Projects\Multi-Agents-System-With-MCP(Model Context Protocol)\custom_weather_mcp_server.py"
            ],
            "env": {
                "OPENWEATHER_API_KEY": OPENWEATHER_API_KEY
            }
        }
    }
)


async def main():

    print("Loading tools...")
    tools = await client.get_tools()
    print("Tools loaded!")

    for tool in tools:
        print(tool.name)

if __name__ == "__main__":
    asyncio.run(main())
