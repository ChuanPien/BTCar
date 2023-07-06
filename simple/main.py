from machine import Pin, PWM, UART, I2C
from time import sleep
from pitches import *
from neopixel import Neopixel
from ssd1306 import SSD1306_I2C
import framebuf
from count_img import *
from arrow import *
from Ultrasonic import *

############# Defined ##############

l_ir = Pin(3, Pin.IN)
c_ir = Pin(5, Pin.IN)
r_ir = Pin(2, Pin.IN)

numpix = 2
pin_num = 18
np = Neopixel(numpix, 0, pin_num, "GRB")
np.brightness(20)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0,0,0)
np.set_pixel(0, black)
np.set_pixel(1, black)
np.show()

M1A = PWM(Pin(8))
M1B = PWM(Pin(9))
M2A = PWM(Pin(10))
M2B = PWM(Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

speed = 40
distance = 0
buzzer = PWM(Pin(22))
volume = 0.01

C5  = 523
CS7  = 554

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
WIDTH  = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.rotate_s(1)

p3 = framebuf.FrameBuffer(p3, 128, 64, framebuf.MONO_HLSB)
p2 = framebuf.FrameBuffer(p2, 128, 64, framebuf.MONO_HLSB)
p1 = framebuf.FrameBuffer(p1, 128, 64, framebuf.MONO_HLSB)
go = framebuf.FrameBuffer(go, 128, 64, framebuf.MONO_HLSB)
up = framebuf.FrameBuffer(up, 128, 64, framebuf.MONO_HLSB)
back = framebuf.FrameBuffer(back, 128, 64, framebuf.MONO_HLSB)
right = framebuf.FrameBuffer(right, 128, 64, framebuf.MONO_HLSB)
left = framebuf.FrameBuffer(left, 128, 64, framebuf.MONO_HLSB)
break1 = framebuf.FrameBuffer(break1, 128, 53, framebuf.MONO_HLSB)
stop = framebuf.FrameBuffer(stop, 128, 64, framebuf.MONO_HLSB)


############# Function ##############

def start():
    oled.fill(0)
    oled.blit(p3, 0, 0)
    oled.show()
    np.set_pixel(0, red)
    np.set_pixel(1, red)
    np.show()
    #buzzer.freq(C5)
    #buzzer.duty_u16(int(volume * 65535))
    sleep(1)
    
    oled.fill(0)
    oled.blit(p2, 0, 0)
    oled.show()
    np.set_pixel(0, yellow)
    np.set_pixel(1, yellow)
    np.show()
    #buzzer.freq(C5)
    #buzzer.duty_u16(int(volume * 65535))
    sleep(1)
    
    oled.fill(0)
    oled.blit(p1, 0, 0)
    oled.show()
    np.set_pixel(0, green)
    np.set_pixel(1, green)
    np.show()
    #buzzer.freq(C5)
    #buzzer.duty_u16(int(volume * 65535))
    sleep(1)
    
    oled.fill(0)
    oled.blit(go, 0, 0)
    oled.show()
    #buzzer.freq(CS7)
    #buzzer.duty_u16(int(volume * 65535))
    sleep(1)
    #buzzer.deinit()
    
def Forward(speed):
    oled.fill(0)
    oled.blit(up, 0, 0)
    oled.show()
    M1A.duty_u16(0)
    M1B.duty_u16(int(65535*speed/100))
    M2A.duty_u16(0)
    M2B.duty_u16(int(65535*speed/100))
    sleep(0.1)
    
def Backward(speed):
    oled.fill(0)
    oled.blit(back, 0, 0)
    oled.show()
    M1A.duty_u16(int(65535*speed/100))
    M1B.duty_u16(0)
    M2A.duty_u16(int(65535*speed/100))
    M2B.duty_u16(0)
    sleep(0.1)

def Left(speed):
    oled.fill(0)
    oled.blit(left, 0, 0)
    oled.show()
    M1A.duty_u16(0)
    M1B.duty_u16(int(65535*speed/150))
    M2A.duty_u16(int(65535*speed/150))
    M2B.duty_u16(0)
    sleep(0.1)    

def Right(speed):
    oled.fill(0)
    oled.blit(right, 0, 0)
    oled.show()
    M1A.duty_u16(int(65535*speed/150))
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(int(65535*speed/150))
    sleep(0.1)
    
def Stop():
    oled.fill(0)
    oled.blit(stop, 0, 0)
    oled.show()
    M1A.duty_u16(0)
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
    sleep(0.5)

def Brake(dis):
    str(dis)
    oled.fill(0)
    oled.blit(break1, 0, 0)
    oled.text(dis + "CM",45,54)
    oled.show()
    M1A.duty_u16(65535)
    M1B.duty_u16(65535)
    M2A.duty_u16(65535)
    M2B.duty_u16(65535)
    sleep(0.5)
    
############# MAIN ##############  
Stop()
#start()

while True:
    l_val = l_ir.value()
    c_val = c_ir.value()
    r_val = r_ir.value()
    distance = read_distance(6, 26)
    
    if distance < 10:
        dis = ('%.1f' %(distance))
        Brake(dis)
        for i in range(3):
            np.set_pixel(0, red)
            np.set_pixel(1, red)
            np.set_pixel(0, black)
            np.set_pixel(1, black)
            np.show()
    elif l_val==0 and c_val==1 and r_val==0:
        np.set_pixel(0, green)
        np.set_pixel(1, green)
        np.show()
        Forward(speed)
    elif l_val==1 and c_val==0 and r_val==0:
        np.set_pixel(0, red)
        np.show()
        Left(speed)
    elif l_val==0 and c_val==0 and r_val==1:
        np.set_pixel(1, red)
        np.show()
        Right(speed)
    elif l_val==1 and c_val==1 and r_val==0:
        np.set_pixel(0, green)
        np.set_pixel(1, green)
        np.show()
        Forward(speed)    
    elif l_val==0 and c_val==1 and r_val==1:
        np.set_pixel(0, green)
        np.set_pixel(1, green)
        np.show()
        Forward(speed) 
    elif l_val==0 and c_val==0 and r_val==0:
        np.set_pixel(0, blue)
        np.set_pixel(1, blue)
        np.show()
        Right(speed)
        sleep(0.15)
        Left(speed)
        sleep(0.15)
    else:
        Stop()
        for i in range(3):
            np.set_pixel(0, red)
            np.set_pixel(1, red)
            np.show()
        