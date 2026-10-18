"""Background jobs."""
import boto3
from celery import Celery

from services.notes.summarize import summarize_note

app = Celery("worker", broker="redis://cache:6379/0")
s3 = boto3.client("s3")


@app.task
def summarize_visit(note):
    return summarize_note(note)


@app.task
def export_visits(path):
    s3.upload_file(path, "carelink-exports", "visits.csv")
