FROM python:3.9.18-slim-bookworm

ENV PYTHONBUFFERED=1

RUN apt-get update \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -m appuser

WORKDIR /app

COPY telemetry_sender.py .
COPY telemetry_receiver.py .

USER appuser

CMD [ "python", "telemetry_receiver.py"]