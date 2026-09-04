from langchain_core.tools import tool

@tool
def calculator(expression: str):
    """Perform mathematical calculations."""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Calculation error: {e}"