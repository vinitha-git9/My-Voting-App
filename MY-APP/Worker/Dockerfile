FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install redis psycopg2
CMD ["python", "worker.py"]
