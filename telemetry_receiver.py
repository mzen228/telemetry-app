import socket

HOST = "0.0.0.0"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"Listening on port {PORT}")

while True:
    data, addr = sock.recvfrom(1024)
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