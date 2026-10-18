"""Research spike: the same FAQ questions through LangChain."""
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5")


def ask(question):
    return llm.invoke(question)
