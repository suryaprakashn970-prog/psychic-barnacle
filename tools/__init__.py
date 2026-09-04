from .calculator import calculator
from .datetime_tool import datetime_tool
from .web_search import web_search
from .open_url import open_url
from .wikipedia import wikipedia_search




available_tools = [
    calculator,
    datetime_tool,
    web_search,
    open_url,
    wikipedia_search,
]


tools_by_name = {
    tool.name: tool
    for tool in available_tools
}