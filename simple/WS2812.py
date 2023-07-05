#Ex07_WS2812.py，閃爍 WS2812 RGB全彩LED
from machine import Pin        # 匯入machine模組 Pin類別
from neopixel import Neopixel  # 匯入外部模組Neopixel(WS2812 RGBLED)
import time

# 設置 WS2812 RGBLEDs.
numpix = 2                                # RGB LED的數量
pin_num = 18                              # RGB LED的腳位
np = Neopixel(numpix, 0, pin_num, "GRB")  # 建立np物件（LED數量, 狀態機編號, 腳位, 模式）
np.brightness(20)                         # RGB LED的亮度（0~255）
red = (255, 0, 0)                         # RGB LED紅色之RGB各色的值（0~255）
green = (0, 255, 0)                       # RGB LED綠色之RGB各色的值（0~255）
blue = (0, 0, 255)                        # RGB LED藍色之RGB各色的值（0~255）
black = (0,0,0)                           # RGB LED黑色之RGB各色的值（熄滅）   
np.set_pixel(0, black)                # 預設編號0的RGB LED熄滅
np.set_pixel(1, black)                # 預設編號1的RGB LED熄滅
np.show()                                 # 顯示RGB LED

while True:
    np.set_pixel(0, red)         # 點亮編號0 WS2812的 紅色 燈光
    np.set_pixel(1, red)         # 點亮編號1 WS2812的 紅色 燈光
    np.show()
    print('亮紅燈')
    time.sleep(1)
    np.set_pixel(0, blue)       # 點亮編號0 WS2812的 藍色 燈光
    np.set_pixel(1, blue)       # 點亮編號1 WS2812的 藍色 燈光
    np.show()
    print('亮藍燈')
    time.sleep(1)
    np.set_pixel(0, green)       # 點亮編號0 WS2812的 綠色 燈光
    np.set_pixel(1, green)       # 點亮編號1 WS2812的 綠色 燈光
    np.show()
    print('亮綠燈')
    time.sleep(1)
    np.set_pixel(0, black)       # 熄滅編號0 WS2812的 RGB LED
    np.set_pixel(1, black)       # 熄滅編號1 WS2812的 RGB LED
    np.show()
    print('關燈')
    time.sleep(1)
