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
        parts = message.split(",")
        altitude_part = parts[0]
        altitude_ft = int(altitude_part.split("=")[1])

        if altitude_ft < 0:
            print("Invalid altitude")
        else:
            print("Valid message")

    except Exception as e:
        print(f"Error parasing message: {e}")

sock.close()
print("Receiver shutdown complete...")
sys.exit(0)