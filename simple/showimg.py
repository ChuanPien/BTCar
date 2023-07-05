# Ex09_oled_ssd1306_2.py，ssd1306 OLED螢幕 顯示圖片
from machine import Pin, I2C        # 匯入內建machine模組
from ssd1306 import SSD1306_I2C     # 匯入外部模組ssd1306.py
import framebuf                     # 匯入內建framebuf模組
import time
from people_img import *               # 匯入自製圖形檔 img.py

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000) # 初始設定 I2C 使用 GPIO16、GPIO17(I2C 0)
print("I2C Address      : "+hex(i2c.scan()[0]))     # 顯示I2C的位址
print("I2C Configuration: "+str(i2c))               # 顯示I2C的設定
WIDTH  = 128                                        # oled螢幕的寬度
HEIGHT = 64                                         # oled螢幕的高度
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)              # 建立並設定oled物件
oled.rotate_s(1)                                    # 旋轉oled螢幕，參數 1:正向, 0:旋轉180度

# 建立fb圖片物件，logo(128x64)及上、右、下、左(64x64)黑白圖片，圖片名稱定義在img.py內
# 參數:圖片名稱, 圖片像數 x, 圖片像數 y ,單色水平排列 framebuf.MONO_HLSB
people = framebuf.FrameBuffer(people, 128, 64, framebuf.MONO_HLSB)

# 顯示依序顯示下面 5種黑白圖案
while True:
    oled.fill(0)             # 清除 oled 螢幕
    oled.blit(people, 0, 0) # 將logo圖片顯示在OLED螢幕 座標（0,0）上
    oled.show()              # 顯示 oled 螢幕
    time.sleep(5)   

