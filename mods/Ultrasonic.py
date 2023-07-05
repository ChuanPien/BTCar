from machine import Pin
from machine import time_pulse_us
from time import sleep_us

def read_distance(trig_pin, echo_pin):
    trigger = Pin(trig_pin, mode=Pin.OUT)
    echo = Pin(echo_pin, mode=Pin.IN)

    trigger.value(0)
    sleep_us(5)
    trigger.value(1)
    sleep_us(10)
    trigger.value(0)

    try:
        pulse_time = time_pulse_us(echo, 1, 1000000)
        d = (pulse_time / 2) / 29.1       #依超音波旅行時間計算距離，計算到公分，>400cm就送出返回值 -1
        #return int(d) if d < 400 else -1 #取整數，計算到公分，大於400cm就送出返回值 -1
        return d if d < 400 else -1       #浮點數，計算到公分，大於400cm就送出返回值 -1
    except OSError as ex:                 #如果有錯誤，就送出返回值 -1
        return -1
