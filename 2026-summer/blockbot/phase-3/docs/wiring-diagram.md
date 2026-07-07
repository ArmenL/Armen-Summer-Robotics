## Phase 3 — Motor Wiring

### Pico → #3543 Control Pins
| Signal | Pico GPIO | #3543 Pin |
|--------|-----------|-----------|
| Left PWM | GP2 | PWM (Left) |
| Left DIR | GP3 | DIR (Left) |
| Right PWM | GP6 | PWM (Right) |
| Right DIR | GP7 | DIR (Right) |
| SLP | GP8 | SLP (Left & Right) |
| Ground | Pin 8 (GND) | GND |

> ⚠️ Phase 4 note: encoder signals from #3543 are 5V. 
> Pico GPIO is 3.3V max. Will need a level shifter.

### Motors → #3543
| Motor | Board Pin |
|-------|-----------|
| Left motor + | ML+ |
| Left motor - | ML- |
| Right motor + | MR+ |
| Right motor - | MR- |

