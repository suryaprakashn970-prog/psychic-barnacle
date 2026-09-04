from ddgs import DDGS
import json
from langchain_core.tools import tool

@tool
def web_search(query: str):
    """Search the web for current information."""
    results = DDGS().text(query, max_results=10)

    formatted_results = []

    for result in results:
        formatted_results.append({
            "title": result.get("title", ""),
            "url": result.get("href", ""),
            "snippet": result.get("body", "")
        })

    return json.dumps(formatted_results, indent=2)