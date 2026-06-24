import fastapi
app = fastapi.FastAPI(title="Pi Serial API")

@app.get("/")
def get_home():
    return {"message": "Hello, World!"}

@app.get("/telemetry")
def get_telemetry():
    return {"type":"telemetry","battery_v":7.42,"left_ticks":1234,"right_ticks":1211,"tof_mm":642,"estop":False}

@app.get("/extra")
def get_extra():
    return {"message": "have I executed this perfectly?"}