import pycom 
import time
while(True): # stop after 10 cycles
    pycom.rgbled(0xffffff) # White
    time.sleep(5)
    pycom.rgbled(0x000000) # Black
    time.sleep(1)