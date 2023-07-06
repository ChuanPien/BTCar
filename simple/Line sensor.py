# EX12:Line sensor紅外線循跡感應器範例程式
# 採用Cytron Maker Pi RP2040 擴展板

from machine import Pin
import time

# 設定紅外線感測器腳位並設置為輸入
l_ir = Pin(3, Pin.IN)    # 設定左側紅外線感測器為gpio 3，並設為輸入
c_ir = Pin(5, Pin.IN)    # 設定中央紅外線感測器為gpio 5，並設為輸入
r_ir = Pin(2, Pin.IN)    # 設定右側紅外線感測器為gpio 2，並設為輸入
      
while True:
    l_val = l_ir.value()         # 讀取左邊紅外線感應器的值    
    c_val = c_ir.value()         # 讀取中央紅外線感應器的值
    r_val = r_ir.value()         # 讀取右邊紅外線感應器的值
    print('左側感測器的值=',l_val)  # 顯示左邊紅外線感應器的值 
    print('中央感測器的值=',c_val)  # 顯示中央紅外線感應器的值 
    print('右側感測器的值=',r_val)  # 顯示右邊紅外線感應器的值 
    print('#'*20)
    time.sleep(1)
