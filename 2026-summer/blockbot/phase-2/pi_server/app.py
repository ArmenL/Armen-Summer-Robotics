import fastapi
from fastapi.responses import HTMLResponse
app = fastapi.FastAPI(title="Pi Serial API")

@app.get("/", response_class=HTMLResponse)
def get_home():
    with open("pi_server/index.html") as f:
        content = f.read()
    return content

@app.get("/telemetry")
def get_telemetry():
    return {"type":"telemetry","battery_v":7.42,"left_ticks":1234,"right_ticks":1211,"tof_mm":642,"estop":"off"}

@app.get("/extra")
def get_extra():
    return {"message": "have I executed this perfectly?"}