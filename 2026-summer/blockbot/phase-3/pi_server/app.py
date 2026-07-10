from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import serial
import threading
import json
import time

PORT = "/dev/ttyACM0"           #Replace with your Raspberry Pi's serial port
BAUD = 115200                   #Replace with your Pi's baud rate

ser = serial.Serial(PORT, BAUD, timeout=0.1)
app = FastAPI()

latest_telemetry = {"Connection": False, "Estop": 0, "Parked": 1}

def read_serial():
    global latest_telemetry
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            try:
                telemetry = json.loads(line)
                latest_telemetry.update(telemetry)             #Update the latest telemetry data
            except json.JSONDecodeError:
                pass                                           #Ignore lines that aren't valid JSON
        time.sleep(0.1)

threading.Thread(target=read_serial, daemon=True).start() #We place the this line here so that Python knows read_serial is a function before we call it. Otherwise, it will throw an error.

@app.get("/")
def get():
    with open("pi_server/index.html") as f:
        content = f.read()
    return HTMLResponse(content)

@app.get("/telemetry")
def get_telemetry():
    return latest_telemetry

@app.post("/command") # These 3 lines are to read the data from the joystick and buttons on the web interface and send it to the robot.
async def command(request: Request):
    data = await request.json()
    command = json.dumps(data) + "\n"  # Convert the data to JSON and add a newline character
    try:
        ser.write(command.encode('utf-8'))  # Send the command to the robot via serial
        return {"Status": "Success"}
    except serial.SerialException:
        return {"Status": "Failure"}