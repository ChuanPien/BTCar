# Ex02-Pico_LED_blink.py，點亮熄滅GPIO 28的LED
from machine import Pin   # 從machine模組匯入Pin類別
import time               # 匯入time模組

led = Pin(28, Pin.OUT)   # 設定LED為 Pico的 GPIO_28 腳位為輸出

while True:
    led.on()             # 點亮LED
    time.sleep(1)        # 暫停 1秒
    led.off()            # 熄滅LED
    time.sleep(1)        # 暫停 1秒  
