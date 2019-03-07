import machine
import time

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='G3')   # create an analog pin on P16

while(True):
    val = apin.voltage()
    print((val - 500)/10)
    time.sleep(0.1)