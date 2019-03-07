import time
import pycom
from lib.LTR329ALS01 import LTR329ALS01
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 115200)
prev = None
def start_sensing():
    light_sensor = LTR329ALS01()
    prev = light_sensor.light()
    while True:
        current = light_sensor.light()
        #print(current)
        first_sensor = abs(current[0] - prev[0])
        second_sensor = abs(current[1] - prev[1])
        #print(first_sensor)
        #print(second_sensor)
        if ((first_sensor > 5) or (second_sensor > 5)):
                prev = current
                print("")