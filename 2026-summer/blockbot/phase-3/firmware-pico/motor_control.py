from machine import Pin, PWM

ML_PWM = PWM(Pin(2))
ML_DIR = Pin(3, Pin.OUT)
MR_PWM = PWM(Pin(6))
MR_DIR = Pin(7, Pin.OUT)
SLP = Pin(8, Pin.OUT)

ML_PWM.freq(1000)
MR_PWM.freq(1000)
SLP.value(1)            #SLP high to disable motors

def drive(ML_Power, MR_Power):
    ML_Power = max(-512, min(512, ML_Power))
    MR_Power = max(-512, min(512, MR_Power))

    if ML_Power >= 0:
        ML_DIR.value(1)
    else:
        ML_DIR.value(0)
    
    if MR_Power >= 0:
        MR_DIR.value(1)
    else:
        MR_DIR.value(0)

    ML_PWM.duty_u16(int(abs(ML_Power) / 512 * 65535))
    MR_PWM.duty_u16(int(abs(MR_Power) / 512 * 65535))

def motorstatus(status):
    if status == 1:     #Status 1 means drive mode
        SLP.value(0)    #SLP low to enable motors  
    else:               #status 0 means park mode
        SLP.value(1)    #SLP high to disable motors

def estop(estop):
    if estop == 1:
        SLP.value(1)    #SLP high to disable motors
    else:
        pass            #If estop is disabled, there can be other reasons for the motors to be disabled, so we don't enable them here