import time
import ltr329als01
from machine import UART

pycom.heartbeat(False)
uart = UART(0, 116000)

light_sensor = ltr329als01.LTR329ALS01()
while True:
    print(light_sensor.light())
    uart.write(str(light_sensor.light()[0]) + str(light_sensor.light()[1]) + "\n")
    time.sleep(1)