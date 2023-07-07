from machine import Pin, PWM, UART, I2C
import framebuf
import time
from neopixel import Neopixel
from ssd1306 import SSD1306_I2C
from arrow_img import *
from Ultrasonic import *

mod = 0
bt = UART(0,9600)
speed = 80
numpix = 2
pin_num = 18
np = Neopixel(numpix, 0, pin_num, "GRB")
np.brightness(20)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0,0,0)
np.set_pixel(0, black)
np.set_pixel(1, black)
np.show()
buzzer = PWM(Pin(22))
volume = 0.1

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000) 
print("I2C Address      : "+hex(i2c.scan()[0]))
print("I2C Configuration: "+str(i2c))
WIDTH  = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.rotate_s(1)

up = framebuf.FrameBuffer(up, 128, 64, framebuf.MONO_HLSB)
back = framebuf.FrameBuffer(back, 128, 64, framebuf.MONO_HLSB)
right = framebuf.FrameBuffer(right, 128, 64, framebuf.MONO_HLSB)
left = framebuf.FrameBuffer(left, 128, 64, framebuf.MONO_HLSB)
break1 = framebuf.FrameBuffer(break1, 128, 53, framebuf.MONO_HLSB)
stop = framebuf.FrameBuffer(stop, 128, 64, framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(stop, 0, 0)
oled.show()

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

M1A = PWM(Pin(8))
M1B = PWM(Pin(9))
M2A = PWM(Pin(10))
M2B = PWM(Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

def Forward(speed, mod, dis):
    print("Forward, 前進")
    M1A.duty_u16(0)
    M1B.duty_u16(int(65535*speed/100))
    M2A.duty_u16(0)
    M2B.duty_u16(int(65535*speed/100))
    if mod == 0:
        oled.fill(0)
        oled.blit(up, 0, 0)
        oled.show()
    else:
        speed = str(speed)
        dis = str(dis)
        oled.fill(0)
        oled.text("BT_Car",40,0)
        oled.text("Speed = " + speed,0,9)
        oled.text("Dir = Front",0,18)
        oled.text("Dis = " + dis + "CM",0,27)
        oled.text("LED0 = Green",0,45)    
        oled.text("LED1 = Green",0,54)
        oled.show() 
    time.sleep(0.1)
    
def Backward(speed, mod, dis):
    print("Backward, 後退")
    M1A.duty_u16(int(65535*speed/100))
    M1B.duty_u16(0)
    M2A.duty_u16(int(65535*speed/100))
    M2B.duty_u16(0)
    if mod == 0:
        oled.fill(0)
        oled.blit(back, 0, 0)
        oled.show()
    else:
        speed = str(speed)
        dis = str(dis)
        oled.fill(0)
        oled.text("BT_Car",40,0)
        oled.text("Speed = " + speed,0,9)
        oled.text("Dir = Back",0,18)
        oled.text("Dis = " + dis + "CM",0,27)
        oled.text("LED0 = Blue",0,45)    
        oled.text("LED1 = Blue",0,54)
        oled.show()
    time.sleep(0.1)
    
def Left(speed, mod, dis):
    print("Turn_Left, 左轉")
    M1A.duty_u16(0)
    M1B.duty_u16(int(65535*speed/100))
    M2A.duty_u16(int(65535*speed/100))
    M2B.duty_u16(0)
    if mod == 0:
        oled.fill(0)
        oled.blit(left, 0, 0)
        oled.show()
    else:
        speed = str(speed)
        dis = str(dis)
        oled.fill(0)
        oled.text("BT_Car",40,0)
        oled.text("Speed = " + speed,0,9)
        oled.text("Dir = Left",0,18)
        oled.text("Dis = " + dis + "CM",0,27)
        oled.text("LED0 = Red",0,45)    
        oled.text("LED1 = Black",0,54)
        oled.show()
    time.sleep(0.1)
    
def Right(speed, mod, dis):
    print("Turn_Right, 右轉")
    M1A.duty_u16(int(65535*speed/100))
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(int(65535*speed/100))
    if mod == 0:
        oled.fill(0)
        oled.blit(right, 0, 0)
        oled.show()
    else:
        speed = str(speed)
        dis = str(dis)
        oled.fill(0)
        oled.text("BT_Car",40,0)
        oled.text("Speed = " + speed,0,9)
        oled.text("Dir = Right",0,18)
        oled.text("Dis = " + dis + "CM",0,27)
        oled.text("LED0 = Black",0,45)    
        oled.text("LED1 = Red",0,54)
        oled.show()
    time.sleep(0.1)
    
def Stop():
    print("Stop, 停止")
    M1A.duty_u16(0)
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
    oled.fill(0)
    oled.blit(stop, 0, 0)
    oled.show()
    time.sleep(0.5)
    
def Brake():
    print("Brake, 剎車")
    M1A.duty_u16(65535)
    M1B.duty_u16(65535)
    M2A.duty_u16(65535)
    M2B.duty_u16(65535)
    oled.fill(0)
    oled.blit(stop, 0, 0)
    oled.show()
    time.sleep(0.5)

Stop()
#ws2812_start()

while True:
    dis = ('%.1f' %(read_distance(6, 26)))
    if bt.any():
        command = bt.readline()
        print(command)

        if(command.startswith("A") or command.startswith("a")):
            np.set_pixel(0, green)
            np.set_pixel(1, green)
            np.show()
            Forward(speed, mod, dis)
            
        elif(command.startswith("C") or command.startswith("c")):
            np.set_pixel(0, blue)
            np.set_pixel(1, blue)
            np.show()
            Backward(speed, mod, dis)

        elif(command.startswith("D") or command.startswith("d")):
            np.set_pixel(0, red)
            np.show()
            Left(speed, mod, dis)

        elif(command.startswith("B") or command.startswith("b")):
            np.set_pixel(1, red)
            np.show()
            Right(speed, mod, dis)
            
        elif(command.startswith("E") or command.startswith("e")):
            mod = 1
            buzzer.freq(1480)
            buzzer.duty_u16(int(volume * 65535))
            time.sleep(0.15)
            buzzer.deinit()
            
        elif(command.startswith("F") or command.startswith("f")):
            mod = 0
            buzzer.freq(587)
            buzzer.duty_u16(int(volume * 65535))
            time.sleep(0.15)
            buzzer.deinit()

        else:
            np.set_pixel(0, red)
            np.set_pixel(1, red)
            np.set_pixel(0, black)
            np.set_pixel(1, black)
            np.set_pixel(0, red)
            np.set_pixel(1, red)
            np.set_pixel(0, black)
            np.set_pixel(1, black)
            np.show()
            Stop()    

