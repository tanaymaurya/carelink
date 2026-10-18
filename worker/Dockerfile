FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["celery", "-A", "worker.tasks", "worker"]
