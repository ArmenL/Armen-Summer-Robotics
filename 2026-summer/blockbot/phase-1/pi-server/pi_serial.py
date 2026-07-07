import serial # type: ignore[import]
import json
import time
import threading

PORT = "/dev/ttyACM0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.1)
time.sleep(2)
print("Connected. Commands: ping | msg <text> | clear | quit")

def read_loop():
    while True:
        try:
            raw = ser.readline().decode("utf-8", errors="ignore").strip()
            if not raw:
                continue
            msg = json.loads(raw)
            t = msg.get("type", "?")
            if t == "keypress":
                print(f"  KEY: {msg['key']}")
            elif t == "hello":
                print(f"  heartbeat t={msg.get('ticks', 0)}")
            elif t == "pong":
                print(f"  pong")
            elif t == "ack":
                print(f"  ack: '{msg.get('text', '')}'")
        except:
            pass

threading.Thread(target=read_loop, daemon=True).start()

while True:
    try:
        line = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if line == "quit":
        break
    elif line == "ping":
        ser.write((json.dumps({"type": "ping"}) + "\n").encode())
    elif line.startswith("msg "):
        ser.write((json.dumps({"type": "message", "text": line[4:]}) + "\n").encode())
    elif line == "clear":
        ser.write((json.dumps({"type": "clear"}) + "\n").encode())

ser.close()