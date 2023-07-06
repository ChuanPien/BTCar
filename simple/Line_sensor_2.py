# Ex12_Line_sensor_2.py:Line sensor紅外線循跡感應器範例程式 2
# 採用Cytron Maker Pi RP2040 擴展板
# 使用到的module:neopixel.py

from machine import Pin
import time
from neopixel import Neopixel

# 設定紅外線感測器腳位並設置為輸入
l_ir = Pin(3, Pin.IN)    # 設定左側紅外線感測器為gpio 3，並設為輸入
c_ir = Pin(5, Pin.IN)    # 設定中央紅外線感測器為gpio 5，並設為輸入
r_ir = Pin(2, Pin.IN)    # 設定右側紅外線感測器為gpio 2，並設為輸入

# 設置 WS2812 RGBLEDs.
numpix = 2                                # RGB LED的數量
pin_num = 18                              # RGB LED的腳位
np = Neopixel(numpix, 0, pin_num, "GRB")  # 建立np物件（LED數量, 狀態機編號, 腳位, 模式）
np.brightness(20)                         # RGB LED的亮度（0~255）
red = (255, 0, 0)                         # RGB LED紅色之RGB各色的值（0~255）
green = (0, 255, 0)                       # RGB LED綠色之RGB各色的值（0~255）
blue = (0, 0, 255)                        # RGB LED藍色之RGB各色的值（0~255）
black = (0,0,0)                           # RGB LED黑色之RGB各色的值（熄滅）   
np.set_pixel(0, black)                    # 預設編號0的RGB LED熄滅
np.set_pixel(1, black)                    # 預設編號1的RGB LED熄滅
np.show()                                 # 顯示RGB LED
    
while True:
    l_val = l_ir.value()      # 讀取左邊紅外線感應器的值    
    c_val = c_ir.value()      # 讀取中央紅外線感應器的值
    r_val = r_ir.value()      # 讀取右邊紅外線感應器的值
    if l_val==1:    # 如果讀取左側紅外線感應器的值為1, 左側全彩LED燈點亮紅燈
        print('左側感測器的值=', l_val, '亮紅燈')
        print('#'*20)
        np.set_pixel(0, red)
        np.set_pixel(1, black)
        np.show()
        time.sleep(0.1)
    elif c_val==1:  # 又如果讀取中央側紅外線感應器的值為1, 左右二側全彩LED燈點亮綠燈
        print('中央感測器的值=', c_val, '亮綠燈')
        print('#'*20)
        np.set_pixel(0, green)
        np.set_pixel(1, green)
        np.show()
        time.sleep(0.1)
    elif r_val==1:    # 又如果讀取右側紅外線感應器的值為1, 右側全彩LED燈點亮紅燈
        print('右側感測器的值=', r_val,'亮紅燈')
        print('#'*20)
        np.set_pixel(0, black)
        np.set_pixel(1, red)
        np.show()
        time.sleep(0.1)
    elif r_val==0 and c_val==0 and l_val==0 :    # 又如果讀取全側紅外線感應器的值為0, 全側全彩LED燈皆暗
        print('右側感測器的值=', r_val,'暗')
        print('#'*20)
        np.set_pixel(0, black)
        np.set_pixel(1, black)
        np.show()
        time.sleep(0.1)

 
