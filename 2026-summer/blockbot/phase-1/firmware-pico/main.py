import time
import select
import sys
import ujson
from machine import Pin, I2C
import sh1106

i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c)

def oled_show(r0="", r1="", r2="", r3=""):
    oled.fill(0)
    oled.text(r0[:16], 0, 0)
    oled.text(r1[:16], 0, 16)
    oled.text(r2[:16], 0, 32)
    oled.text(r3[:16], 0, 48)
    oled.show()

oled_show("BlockBot P1", "Waiting for Pi", "Press a key!")

ROWS = [Pin(p, Pin.OUT, value=1) for p in (6, 7, 8, 9)]
COLS = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (10, 11, 12, 13)]

KEYMAP = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"],
]

def scan_keypad():
    for r, row_pin in enumerate(ROWS):
        row_pin.value(0)
        time.sleep_us(20)
        for c, col_pin in enumerate(COLS):
            if col_pin.value() == 0:
                row_pin.value(1)
                return KEYMAP[r][c]
        row_pin.value(1)
    return None

def send_json(obj):
    sys.stdout.write(ujson.dumps(obj) + "\n")

def recv_json():
    if select.select([sys.stdin], [], [], 0)[0]: #type: ignore[no-untyped-call]
        try:
            line = sys.stdin.readline().strip()
            if line:
                return ujson.loads(line)
        except Exception:
            pass
    return None

ticks = 0
last_key = None
pi_msg = ""

while True:
    key = scan_keypad()

    if key is not None and key != last_key:
        last_key = key
        send_json({"type": "keypress", "key": key, "ticks": ticks})
        oled_show("Key pressed:", "  [" + key + "]", pi_msg[:16], "t=" + str(ticks))
    elif key is None:
        last_key = None

    cmd = recv_json()
    if cmd:
        t = cmd.get("type", "")
        if t == "ping":
            send_json({"type": "pong", "ticks": ticks})
        elif t == "message":
            pi_msg = cmd.get("text", "")
            oled_show("Pi says:", pi_msg[:16], "", "t=" + str(ticks))
            send_json({"type": "ack", "text": pi_msg})
        elif t == "clear":
            pi_msg = ""
            oled_show("BlockBot P1", "Ready", "Press a key!", "")

    ticks += 1
    if ticks % 40 == 0:
        send_json({"type": "hello", "ticks": ticks})
        if last_key is None:
            if pi_msg:
                oled_show("BlockBot P1", pi_msg[:16], "Press a key!", "t=" + str(ticks))
            else:
                oled_show("BlockBot P1", "Ready", "Press a key!", "t=" + str(ticks))

    time.sleep_ms(50)