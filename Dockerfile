FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt.txt
RUN pip install psycopg2-binary

COPY . .

ENV PYTHONUNBUFFERED=1

# Запускаем бота
CMD ["python", "main.py"]
