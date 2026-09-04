import webbrowser
from langchain_core.tools import tool


@tool
def open_url(url: str):
    """
    Open a webpage URL in the browser.
    """

    if not url.startswith(("http://", "https://")):
        return "Invalid URL."

    webbrowser.open(url)

    return f"Opened: {url}"