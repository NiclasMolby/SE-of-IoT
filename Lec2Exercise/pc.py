import serial
import time
import sys

file_location = 'data.txt'

def write_to_device(msg):
	with serial.Serial("/dev/tty.usbmodemPy3434341", 115200, timeout=None) as ser:
		start = time.time()
		print('Writing message to device: ' + msg)
		ser.write((msg+'\n').encode())
		
		return start

def main():
	msg = sys.argv[1]
	write_to_device(msg)

if __name__ == '__main__':
	main()