import pycom
import time
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 115200)

options = {
    "white": 0xffffff,
    "red": 0xff0000,
    "blue": 0x0000ff,
    "green": 0x00ff00,
    "black": 0x000000
}

pycom.rgbled(0x000000)

while(True):
    color = uart.readline()
    if(color != None):
        print("Setting LED color to: " + color.decode().rstrip())
        pycom.rgbled((options.get(color.decode().rstrip())))
    time.sleep(1)