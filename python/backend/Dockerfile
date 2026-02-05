FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# If you use mysqlclient, you may need system deps:
# RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential && rm -rf /var/lib/apt/lists/*

# requirements.txt is at project root given your structure
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your backend package into the image
COPY backend /app/backend

ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
