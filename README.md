# Armen's Summer Robotics 2026

A parent-supervised junior engineering residency built around open-ended
invention — not a kit, not a competition. The north-star project is:

> **BlockBot: a tabletop robot that operates in a 3D-printed Minecraft-like
> physical world, uses sensors first, grows into camera-based computer vision
> later, and performs increasingly useful tasks.**

---

## System Architecture
Laptop (VS Code + SSH)

└── Raspberry Pi 5 8GB  ← brain (Python)

- camera + computer vision

- web dashboard

- mission planner

- telemetry logging

└── Raspberry Pi Pico 2 WH  ← nervous system (MicroPython)

- motors + encoders

- servos

- sensors (ToF, IMU, bump)

- emergency stop

└── Robot hardware + arena

Pi and Pico talk over USB serial using newline-delimited JSON messages.

---

## Hardware

- Raspberry Pi 5 8GB + NVMe SSD + active cooler + official 27W PSU
- Raspberry Pi Pico 2 WH (MicroPython — Arduino C++ kept as fallback)
- Raspberry Pi Camera Module 3 Wide
- Bambu Lab P2S Combo 3D printer
- SH1106 1.3" OLED display (I2C)
- 4×4 matrix keypad
- Encoder differential-drive robot base (ordering Wave 1)
- PLA Matte (vision palette), PETG Basic (structural), TPU 95A HF (grip)

---

## Filament Colors

| Material | Color | Role |
|---|---|---|
| PETG Basic | Black | Structural: chassis, mounts, brackets |
| PETG Basic | Gray | Structural (secondary) |
| PLA Matte | Scarlet Red | Arena blocks — vision color 1 |
| PLA Matte | Grass Green | Arena blocks — vision color 2 |
| PLA Matte | Marine Blue | Arena blocks — vision color 3 |
| PLA Matte | Lemon Yellow | Arena blocks — vision color 4 |
| PLA Matte | Ivory White | AprilTag backgrounds, LED diffusers |
| PLA Basic | Gray | Prototypes, throwaway tests |
| PLA Basic | Black | True-black fiducial patterns |
| TPU 95A HF | Black | Tires, bumpers, gripper pads |

---

## Phase Plan

| Phase | Deliverable | Ladder Level | Status |
|---|---|---|---|
| 0 | Lab setup: printer, Pi, Pico, repo, Onshape | — | ✅ Done |
| 1 | First I/O: OLED + keypad + Pi serial loop | 0 | ✅ Done |
| 2 | CAD coupons + dashboard skeleton | 1–2 | ⬜ Next |
| 3 | Manual drive + stop from dashboard | 3 | ⬜ |
| 4 | Sensors + telemetry: encoders, ToF, bump | 4 | ⬜ |
| 5 | First autonomy: one scripted behavior | 5 | ⬜ |
| 6 ← CORE | Arena + printed pieces + one full mission | 6 | ⬜ |
| — | Overnight camp week (hard zero) | — | ⬜ |
| 7 | Reliability check: 20-trial log | — | ⬜ |
| 8–9 | Stretch: camera stream → detect → orient | 7–9 | ⬜ |
| 10 | Final demo + full documentation | 10 | ⬜ |

---

## Demo Ladder

| Level | Name | Description |
|---|---|---|
| 0 | Blinky + serial | Pico reads input and sends state to Pi |
| 1 | Dashboard skeleton | Browser shows robot connection and fake telemetry |
| 2 | Real telemetry | Browser shows real Pico sensor values |
| 3 | Manual robot | Dashboard drives robot; stop works |
| 4 | Sensor robot | Robot detects distance, bump, encoders |
| 5 | Simple autonomy | Robot performs one scripted task |
| 6 | Block world | Gridded arena and printed blocks integrated |
| 7 | Camera stream | Dashboard shows live camera feed |
| 8 | Vision detection | Robot detects colors and markers |
| 9 | Vision orientation | Robot turns toward target |
| 10 | Capstone | Robot completes a block-world mission and explains it |

---

## Repository Structure
Armen-Summer-Robotics/

README.md

2026-summer/

blockbot/

phase-1/

firmware-pico/   ← MicroPython code for the Pico

pi-server/       ← Python code for the Pi

docs/

engineering-notebook.md

wiring-diagram.md

test-log.md

photos/

---

## LLM Use Policy

LLMs are used as engineering assistants — tutors, reviewers, debuggers,
and design partners. They are not the project owner.

A feature is only accepted when Armen can explain: what the code does,
what hardware it controls, what pins it uses, what can fail, and how it
was tested. No LLM-generated code controls motors until a parent reviews it.

---
