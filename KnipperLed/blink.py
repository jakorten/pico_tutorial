from machine import Pin
import utime

led1 = Pin(28, Pin.OUT)

delay = 0.1

while True:
    led1.value(1)
    utime.sleep(delay)
    led1.value(0)
    utime.sleep(delay)
    

