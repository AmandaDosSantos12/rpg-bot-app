# syntax=docker/dockerfile:1
FROM ubuntu/python:3.12-24.04_stable

RUN pip install panel

COPY app.py .
COPY game_master.py .

EXPOSE 8080
CMD ["panel", "serve", "app.py", "--port", "8080",
"--allow-websocket-origin=rpg-bot-app-793630530088.us-central1.run.app"]



