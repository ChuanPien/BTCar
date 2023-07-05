# Ex08_oled_ssd1306_1.py，ssd1306 OLED螢幕 顯示文字
from machine import Pin, I2C        # 匯入內建machine模組
from ssd1306 import SSD1306_I2C     # 匯入外部模組ssd1306.py
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000) # 初始設定 I2C 使用 GPIO16、GPIO17(I2C 0)
print("I2C Address      : "+hex(i2c.scan()[0]))     # 顯示I2C的位址
print("I2C Configuration: "+str(i2c))               # 顯示I2C的設定
WIDTH  = 128                                        # oled螢幕的寬度
HEIGHT = 64                                         # oled螢幕的高度
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)              # 建立並設定oled物件
oled.rotate_s(1)                                    # 旋轉oled螢幕，參數 1:正向, 0:旋轉180度

while True:
    # 以下為顯示文字
    oled.fill(0)                         # 清除 oled 螢幕
    oled.text("Ai4kids",0,0)             # 將文字顯示在座標（0,0）上
    oled.text("----------------",0,9)    # 將文字顯示在座標（0,9）上
    oled.text("Code & Gear Club",0,18)   # 將文字顯示在座標（0,18）上
    oled.text(">>>>>>>>>>>>>>>>",0,27)   # 將文字顯示在座標（0,27）上
    oled.text("1234567890123456",0,36)   # 將文字顯示在座標（0,36）上
    oled.text("abcdefghijklmnop",0,45)   # 將文字顯示在座標（0,45）上    
    oled.text("ABCDEFGHIJKLMNOP",0,54)   # 將文字顯示在座標（0,54）上
    oled.show()                          # 顯示 oled 螢幕


