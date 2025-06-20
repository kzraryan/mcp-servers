# Dockerfile for LOINC Semantic Server
FROM python:3.11-slim
WORKDIR /app
COPY ./src ./src
COPY pyproject.toml ./
RUN pip install poetry && poetry install
CMD ["python", "src/server.py"]
