from machine import Pin, PWM
import time
from pitches import *
from pirate import *

buzzer = PWM(Pin(22))
volume = 0.1

for i in mario:
    if i == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(i)
        buzzer.duty_u16(int(volume * 65535))
    time.sleep(durations[i/1000])
buzzer.deinit()
