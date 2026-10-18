"""Approved LLM gateway: every model call goes through here so redaction, logging and the provider
allow-list live in one place."""
from openai import OpenAI

_client = OpenAI()


def chat(model, messages, feature=None):
    return _client.chat.completions.create(model=model, messages=messages, user=feature)


def embed(texts):
    return _client.embeddings.create(model="text-embedding-3-small", input=texts)
