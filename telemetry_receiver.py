import os
import socket
import signal
import sys

HOST = os.getenv("LISTEN_HOST", "0.0.0.0")
PORT = int(os.getenv("LISTEN_PORT", "5005"))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

running = True


def shutdown_handler(signum, frame):
    global running
    print("\nShutdown signal received.  Cleaning up...")
    running = False


def parse_message(s):
    parts = s.split(",")
    altitude_part = parts[0]
    airspeed_part = parts[1]
    temperature_part = parts[2]

    altitude_ft = int(altitude_part.split("=")[1])
    airspeed_kts = int(airspeed_part.split("=")[1])
    temperature_c = int(temperature_part.split("=")[1])

    return altitude_ft, airspeed_kts, temperature_c


signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

print(f"Listening on port {PORT}")

while running:
    try:
        sock.settimeout(1.0)
        data, addr = sock.recvfrom(1024)
    except socket.timeout:
        continue

    message = data.decode("utf-8")

    print(f"Received from {addr}: {message}")

    try:
        altitude_ft, _, _ = parse_message(message)

        if altitude_ft < 0:
            print("Invalid altitude")
        else:
            print("Valid message")

    except Exception as e:
        print(f"Error parasing message: {e}")

sock.close()
print("Receiver shutdown complete...")
sys.exit(0)
