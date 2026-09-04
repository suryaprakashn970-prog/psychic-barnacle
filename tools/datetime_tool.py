from langchain_core.tools import tool
@tool
def datetime_tool():
    """Get the current date and time."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")