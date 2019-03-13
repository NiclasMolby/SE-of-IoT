import machine
import time

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='G3')   # create an analog pin on P16

while(True):
    val = apin.voltage()
    print(int(val / 10))
    #print((val - 500)/10)
    #print(((val * 1100) / 4096 - 500) / 10)
    time.sleep(0.1)