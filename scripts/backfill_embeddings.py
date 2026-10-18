"""One-off: embed old visit notes for search. Not part of any declared feature."""
import click
from openai import OpenAI

client = OpenAI()


@click.command("backfill")
def backfill():
    notes = ["patient reports a mild headache"]
    return client.embeddings.create(model="text-embedding-3-small", input=notes)
