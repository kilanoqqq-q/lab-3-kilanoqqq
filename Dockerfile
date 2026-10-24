FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask pyftpdlib

EXPOSE 5000 2121 30000-30010

CMD ["python", "app.py"]
