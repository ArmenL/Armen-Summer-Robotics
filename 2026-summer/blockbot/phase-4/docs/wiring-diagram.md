# Wiring-Diagram.MD

## Main Diagram

|Part|Signal|Pin|
|---|---|---|
|Front ToF Sensor|SDA|GP0(I2C0)|
||SCL|GP1(I2C0)|
||GPIO1|GP2|
||Reserved For XSHUT|GP3|
|Front Right Limit Switch|NO(Normally Open)|GP4|
|Front Left Limit Switch|NO(Normally Open)|GP5|
|Right Motor|PWM|GP6|
||DIR|GP7|
|Left Motor|PWM|GP8|
||DIR|GP9|
|Both Motors|SLP|GP10|
|BNO055|SDA|GP14(Software I2C)|
||SCL|GP15(Software I2C)|
|Back Left Limit Switch|NO(Normally Open)|GP16|
|Back Right Limit Switch|NO(Normally Open)|GP17|
|Back ToF Sensor|SDA|GP18(I2C1)|
||SCL|GP19(I2C1)|
||GPIO1|GP20|
|Left Encoder|A|GP21|
||B|GP22|
|Spare|Nothing|GP26|
|Right Encoder|A|GP27|
||B|GP28|

## Encoder Wiring Diagram

|Part|Encoder Signal|Level Shifter Channel|Pico Pin|
|---|---|---|---|
|Left A|ELA|1|GP21|
|Left B|ELB|2|GP22|
|Right A|ERA|3|GP27|
|Right B|ERB|4|GP28|