from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage
)

from model import model_with_tools
from tools import tools_by_name
from prompts import SYSTEM_PROMPT


def calling(query: str) -> str:

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=query)
    ]

    while True:

        response = model_with_tools.invoke(messages)

        # No tool needed → final answer
        if not response.tool_calls:
            return response.content

        # Add AI response containing tool calls
        messages.append(response)

        # Execute requested tools
        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"🔧 Tool: {tool_name}")
            print(f"📦 Args: {tool_args}")

            tool = tools_by_name[tool_name]

            result = tool.invoke(tool_args)

            print(f"📤 Tool Result: {result}")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )