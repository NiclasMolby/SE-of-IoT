import pycom
import time
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 115200)

pycom.rgbled(0x000000)

while True:
    color = uart.readline()
    if color is not None:
        color_text = color.decode().rstrip()
        print(color_text)
        if color_text == "True":
            print("Setting LED color to on")
            pycom.rgbled(0xffffff)
            
        if color_text == "False":
            print("Setting LED color to off")
            pycom.rgbled(0x000000)
        time.sleep(1)