FROM python:3.9-slim

ENV PYTHONBUFFERED=1

RUN useradd -m appuser

WORKDIR /app

COPY telemetry_sender.py .
COPY telemetry_receiver.py .

USER appuser

CMD [ "python", "telemetry_receiver.py"]