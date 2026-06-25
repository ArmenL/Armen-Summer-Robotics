import json
import threading
import serial # type: ignore[import]
import fastapi
from fastapi.responses import HTMLResponse
app = fastapi.FastAPI(title="Pi Serial API")

PORT = "/dev/ttyACM0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.1)
latest_telemetry = {"type": "hello", "key": "none", "ticks": 0}

def read_serial():
    while True:
        try:
            raw = ser.readline().decode("utf-8", errors="ignore").strip()
            msg = json.loads(raw)
        except:
            continue
        global latest_telemetry
        latest_telemetry = msg
    
threading.Thread(target=read_serial, daemon=True).start()

@app.get("/", response_class=HTMLResponse)
def get_home():
    with open("pi_server/index.html") as f:
        content = f.read()
    return content

@app.get("/telemetry")
def get_telemetry():
    return latest_telemetry

@app.get("/telemetryexample")
def get_telemetryexample():
    return {"type":"telemetry","battery_v":7.42,"left_ticks":1234,"right_ticks":1211,"tof_mm":642,"estop":"off"}

@app.get("/extra")
def get_extra():
    return {"message": "have I executed this perfectly?"}