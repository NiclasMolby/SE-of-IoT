import time
import pycom
from lib.SI7006A20 import SI7006A20
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 115200)
prev = None
def start_sensing():
    temperature_sensor = SI7006A20()
    while(True):
        print(temperature_sensor.temperature())
        time.sleep(1)