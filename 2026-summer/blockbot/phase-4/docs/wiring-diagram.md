# Wiring Diagram

|Part|Signal|Pin|
|-----|-----|----|
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
|Back ToF Sensor|SDA|GP18(I2C1)|
||SCL|GP19(I2C1)|