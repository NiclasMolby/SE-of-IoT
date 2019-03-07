import serial
import time
import sys
import csv

def listen_to_device():
        with serial.Serial("/dev/tty.usbmodemPy3434341", 115200, timeout=None) as ser:
                while(True):
                        line = ser.readline()
                        received = time.time()
                        write_to_csv(received)
                        #print(received)


def write_to_csv(received):
        with open('timestamps.csv','a') as file:
                file.write(repr(received))
                file.write('\n')

def main():
	listen_to_device()
  

if __name__ == '__main__':
	main()