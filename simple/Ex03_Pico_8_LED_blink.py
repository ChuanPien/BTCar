# Ex03_Pico_8_LED_blink.py，讓GPIO 0 ~ GPIO 7的8顆LED依順序亮滅

from machine import Pin   # 從machine模組匯入Pin類別
import time               # 匯入time模組

# 對for迴圈做無限多次迴圈，依順序點亮熄滅LED   
while True:
    for pin in range(8):         # 使用for迴圈依順序指定腳位 
        led = Pin(pin, Pin.OUT)  # 設定腳位 GPIO 從 0 ~ 7為輸出 
        led.on()                 # 點亮LED
        time.sleep(0.1)          # 暫停 0.1秒
        led.off()                # 熄滅LED
        time.sleep(0.1)          # 暫停 0.1秒
        