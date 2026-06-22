# Phase 1 Wiring Diagram

Pico 2 WH — USB port at the top, counting pins from top down.

## OLED (GME12864-78, 1.3", SH1106, I2C)

| OLED Pin | Pico Location                        |
|----------|--------------------------------------|
| VCC      | Right side, 5th from top (3V3 OUT, pin 36) |
| GND      | Left side, 8th from top (GND, pin 38) |
| SDA      | Left side, 6th from top (GP4, pin 6)  |
| SCK      | Left side, 7th from top (GP5, pin 7)  |

I2C bus: 0 — freq: 400000 Hz — address: 0x3C

## 4x4 Matrix Keypad — Rows (outputs, driven LOW to scan)

| Keypad Pin | Pico Location                        |
|------------|--------------------------------------|
| R0         | Left side, 9th from top (GP6, pin 9)  |
| R1         | Left side, 10th from top (GP7, pin 10)|
| R2         | Left side, 11th from top (GP8, pin 11)|
| R3         | Left side, 12th from top (GP9, pin 12)|

## 4x4 Matrix Keypad — Columns (inputs, internal pull-ups ON)

| Keypad Pin | Pico Location                         |
|------------|---------------------------------------|
| C0         | Left side, 14th from top (GP10, pin 14)|
| C1         | Left side, 15th from top (GP11, pin 15)|
| C2         | Left side, 16th from top (GP12, pin 16)|
| C3         | Left side, 17th from top (GP13, pin 17)|

## Notes
- All GPIO pins used (GP4-GP13) are on the LEFT column of the Pico.
- VCC is the only wire that goes to the RIGHT column (pin 36).
- Pin 13 on the left side is GND — skip it when counting to the keypad pins.