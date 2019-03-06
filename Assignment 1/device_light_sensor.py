import time
import pycom
from lib.LTR329ALS01 import LTR329ALS01
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 116000)

def start_sensing():
    light_sensor = LTR329ALS01()
    while True:
        print(str(light_sensor.light()))
        #uart.write(str(light_sensor.light()[0]) + str(light_sensor.light()[1]) + "\n")
        time.sleep(1)