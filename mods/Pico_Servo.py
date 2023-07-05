from machine import Pin, PWM
from time import sleep

# 設定servo的PWM腳位及頻率
servoPin = PWM(Pin(18))
servoPin.freq(50)

# 定義servo旋轉角度函數
def servo(degrees):
    # 限制servo最大角度為180度，最小角度為0度
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    # 設定最大的工作週期為9000，最小工作週期為1000
    maxDuty=9000          # 旋轉到 180度位置
    minDuty=1000          # 旋轉到 0度位置
    # 將旋轉角度轉換為工作週期的值
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)  
    servoPin.duty_u16(int(newDuty))        # 設定 servo PWM 工作週期

while True:
  for degree in range(0,180,1):         # 從 0度轉到 180度，每次轉 1度
    servo(degree)
    sleep(0.001)
    print("increasing -- "+str(degree))

  for degree in range(180, 0, -1):      # 從 180度轉到 0度，每次轉 1度
    servo(degree)
    sleep(0.001)
    print("decreasing -- "+str(degree))