from langchain_ollama import ChatOllama

from tools import available_tools


model = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


model_with_tools = model.bind_tools(available_tools)