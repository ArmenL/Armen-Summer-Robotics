# Engineering Notebook — BlockBot Phase 1

**Date:** 2026-06-20
**Phase:** 1 — First I/O

## What I built
A circuit on a breadboard with a 1.3" OLED display and a 4x4 matrix keypad
connected to a Raspberry Pi Pico 2 WH. The Pico runs MicroPython and talks
to the Raspberry Pi over USB serial using JSON messages.

## What worked
- Keypad correctly detects key presses and shows them on the OLED
- Pi receives key press events as JSON lines
- Pi can send a ping and receive a pong back
- Pi can send a message and it appears on the OLED

## What failed and what I fixed

### Failure 1: Wrong OLED driver
**Expected:** Text on the OLED screen
**What happened:** Static pattern on the screen
**Cause:** My 1.3" OLED uses an SH1106 controller chip, not SSD1306.
The wrong driver sends data in the wrong format.
**Fix:** Downloaded the SH1106 driver and switched to it.
**Lesson:** Always identify the exact chip, not just the module.

### Failure 2: Syntax error in main.py
**Expected:** main.py runs without errors
**What happened:** SyntaxError on line 76
**Cause:** Used f-strings which some MicroPython versions do not support.
**Fix:** Rewrote all f-strings using regular string concatenation.
**Lesson:** MicroPython is not identical to regular Python.

### Failure 3: mpremote could not find the Pico
**Expected:** mpremote installs ssd1306 driver onto the Pico
**What happened:** "no device found" error
**Cause:** MicroPico extension was holding the serial port.
Only one program can hold a serial port at a time.
**Fix:** Used wget to download the driver file to the Pi,
then used MicroPico's Upload file to Pico instead of mpremote.
**Lesson:** MicroPico and mpremote fight over the port. Use one or the other.

## LLM assistance notes
Used Claude to generate main.py and pi_serial.py, then read through
every line and learned what each one does before uploading to hardware.
Claude also helped diagnose the SH1106 vs SSD1306 issue and the
port conflict problem.

## Test results
See test-log.md

## What to do next
Phase 2: CAD tolerance coupons in Onshape and dashboard skeleton
using FastAPI on the Pi.