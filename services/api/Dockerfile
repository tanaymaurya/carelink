FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["uvicorn", "services.api.app:app", "--host", "0.0.0.0"]
