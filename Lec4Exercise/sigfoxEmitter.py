from network import Sigfox
import socket
import time
import machine

from lib.LTR329ALS01 import LTR329ALS01

adc = machine.ADC()
apin = adc.channel(pin='G3')

counter = 0

light_sensor = LTR329ALS01()
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
#s.send("Anton er grim")
#s.send(bytes([1, 2]))
while(True):
    temp_val = ('%04d' % int((apin.voltage()) / 10))
    light_val = ('%04d' % light_sensor.light()[0])
    counter = counter + 1
    val_counter = ('%04d' % counter)
    msg = str(temp_val) + str(light_val) + str(val_counter)
    print((msg))
    s.send(msg)
    time.sleep(660)
    #time.sleep(1)