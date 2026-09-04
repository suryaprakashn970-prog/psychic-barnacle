import requests
from langchain_core.tools import tool

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia and return a summary."""

    url = (
        "https://en.wikipedia.org/api/rest_v1/page/summary/"
        + query.replace(" ", "_")
    )

    headers = {
        "User-Agent": "Jarvis-AI/1.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return f"Wikipedia error: HTTP {response.status_code}"

        data = response.json()

        return data.get(
            "extract",
            f"No information found for {query}"
        )

    except Exception as e:
        return f"Wikipedia error: {e}"