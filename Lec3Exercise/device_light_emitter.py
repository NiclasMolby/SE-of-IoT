import pycom
import time

pycom.heartbeat(False)


def emit_light():
    while True:
        pycom.rgbled(0xffffff)    
        time.sleep(1/8)
        pycom.rgbled(0x000000)
        time.sleep(1/8)