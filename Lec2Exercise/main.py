import pycom
import time
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 115200)

while True:
    msg = uart.readline()
    if msg is not None:
        print("Message: " + msg.decode())
    time.sleep(1)