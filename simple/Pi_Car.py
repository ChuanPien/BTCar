# Ex_10_Maker_Pi_Car.py(自走車程式)
# 採用Cytron Maker Pi RP2040 擴展板
# 使用到的module:neopixel.py

from machine import Pin, PWM, UART
import time
from neopixel import Neopixel

# setup WS2812 RGBLEDs. 設定WS2812全彩LED的腳位以及相關資訊
numpix = 2        # 設定WS2812全彩LED的數量
pin_num = 18      # 設定WS2812全彩LED的腳位
np = Neopixel(numpix, 0, pin_num, "GRB")      # 建立np為WS2812全彩LED的物件名稱
np.brightness(20)            # 設定WS2812全彩LED的亮度，最大為128
red = (255, 0, 0)            # 設定WS2812全彩LED 紅色的三原色各像素值，最大為255
green = (0, 255, 0)          # 設定WS2812全彩LED 綠色的三原色各素值，最大為255
blue = (0, 0, 255)           # 設定WS2812全彩LED 藍色的三原色各素值，最大為255
black = (0,0,0)              # 設定WS2812全彩LED 黑色的三原色各素值，最大為255
np.set_pixel(0, black)   # 設定WS2812全彩LED 編號：0 初始為黑色（熄滅）
np.set_pixel(1, black)   # 設定WS2812全彩LED 編號：1 初始為黑色（熄滅）
np.show()                    # 顯示WS2812全彩LED

# 設定直流馬達的腳位及PWM的頻率
M1A = PWM(Pin(8))
M1B = PWM(Pin(9))
M2A = PWM(Pin(10))
M2B = PWM(Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

# 建立ws2812_start()函數，讓WS2812全彩LED (WS2812) R->G->B 循環亮三次
def ws2812_start():
    for i in range(3):
        np.set_pixel(0, red)
        np.set_pixel(1, red)
        np.show()
        time.sleep(0.5)
        np.set_pixel(0, green)
        np.set_pixel(1, green)
        np.show()
        time.sleep(0.5)
        np.set_pixel(0, blue)
        np.set_pixel(1, blue)
        np.show()
        time.sleep(0.5)
        np.set_pixel(0, black)
        np.set_pixel(1, black)
        time.sleep(0.5)
        np.show()

# 建立自走車的前進、後退、左轉、右轉、停止、煞車等直流馬達的函數
def Forward(speed):
    print("Forward, 前進")
    M1A.duty_u16(0)                      # Duty Cycle 的值，介在 0 ~ 65535
    M1B.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    M2A.duty_u16(0)                      # Duty Cycle 的值，介在 0 ~ 65535
    M2B.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    np.set_pixel(0, green)
    np.set_pixel(1, green)
    np.show()
    time.sleep(0.1)
    
def Backward(speed):
    print("Backward, 後退")
    M1A.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    M1B.duty_u16(0)                      # Duty Cycle 的值，介在 0 ~ 65535
    M2A.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    M2B.duty_u16(0)
    time.sleep(0.1)

def Left(speed):
    print("Turn_Left, 左轉")
    M1A.duty_u16(0)                      # Duty Cycle 的值，介在 0 ~ 65535
    M1B.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    M2A.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    M2B.duty_u16(0)       
    np.set_pixel(0, red)
    np.set_pixel(1, blue)
    np.show()
    time.sleep(0.1)    

def Right(speed):
    print("Turn_Right, 右轉")
    M1A.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    M1B.duty_u16(0)                      # Duty Cycle 的值，介在 0 ~ 65535
    M2A.duty_u16(0)                      # Duty Cycle 的值，介在 0 ~ 65535
    M2B.duty_u16(int(65535*speed/100))   # Duty Cycle 的值，介在 0 ~ 65535
    np.set_pixel(0, blue)
    np.set_pixel(1, red)
    np.show()
    time.sleep(0.1)
    
def Stop():
    print("Stop, 停止")
    M1A.duty_u16(0)   # Duty Cycle 的值，介在 0 ~ 65535
    M1B.duty_u16(0)   # Duty Cycle 的值，介在 0 ~ 65535
    M2A.duty_u16(0)   # Duty Cycle 的值，介在 0 ~ 65535
    M2B.duty_u16(0)   # Duty Cycle 的值，介在 0 ~ 65535
    blink()
    time.sleep(0.5)

def Brake():
    print("Brake, 剎車")
    M1A.duty_u16(65535)   # Duty Cycle 的值，介在 0 ~ 65535
    M1B.duty_u16(65535)   # Duty Cycle 的值，介在 0 ~ 65535
    M2A.duty_u16(65535)   # Duty Cycle 的值，介在 0 ~ 65535
    M2B.duty_u16(65535)   # Duty Cycle 的值，介在 0 ~ 65535
    np.set_pixel(0, red)  
    np.set_pixel(1, red)
    np.show()
    time.sleep(0.5)
    
def blink():
    np.set_pixel(0, red)  
    np.set_pixel(1, red)
    np.show()
    time.sleep(0.5)
    np.set_pixel(0, black)  
    np.set_pixel(1, black)
    np.show()

# 自走車初始化
Stop()
ws2812_start()

# 自走車移動主程式
while True:
    speed = 40             # speed速度變數，預設值80，可以自己調整 0 ~ 100
    Forward(speed)
    time.sleep(2)
    
    Backward(speed)
    blink()
    time.sleep(2)
    
    Left(speed)
    time.sleep(2)
    
    Right(speed)
    time.sleep(2)
    
    Stop()
    
    break
