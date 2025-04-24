FROM python:3.11-slim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY app/main.py .
COPY app/game_master.py .
COPY app/secret.py .

CMD ["python3", "main.py"]