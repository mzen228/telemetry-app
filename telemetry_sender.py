import socket
import time
import random

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    altitude_ft = random.randint(0, 40000)
    airspeed_kts = random.randint(100, 600)
    temperature_c = random.randint(-50, 40)

    message = f"ALT_FT={altitude_ft},AIRSPEED_KTS={airspeed_kts},TEMP_C={temperature_c}"

    sock.sendto(message.encode("utf-8"), (TARGET_HOST, TARGET_PORT))

    print(f"Sent: {message}")

    time.sleep(1)