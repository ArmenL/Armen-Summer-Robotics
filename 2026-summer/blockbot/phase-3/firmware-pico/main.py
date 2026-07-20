import motor_control
import ujson
import sys
import select
import time

last_command_time = time.ticks_ms()
TIMEOUT_MS = 500  # half a second timeout
motor_status = 0
poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

while True:
    if poll.poll(0): # Check if there's input available
        command = sys.stdin.readline().strip()
        last_command_time = time.ticks_ms()  # Reset the timeout timer

        try:
            data = ujson.loads(command)
            if "motor_status" in data: 
                motor_control.motorstatus(data.get("motor_status", 0))
                motor_status = data.get("motor_status")
            motor_control.estop(data.get("estop", 0))
            if motor_status == 1:
                motor_control.drive(data.get("ML_Power", 0), data.get("MR_Power", 0))
            sys.stdout.write(ujson.dumps({"motor_status": motor_status, "estop": data.get("estop", 0)}) + "\n")
        except:
            pass  # Ignore invalid JSON commands
    if time.ticks_diff(time.ticks_ms(), last_command_time) > TIMEOUT_MS:
        motor_control.estop(1)  # Trigger emergency stop if no command received within timeout