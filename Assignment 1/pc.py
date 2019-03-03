import serial
import time
import sys

file_location = 'data.txt'

def write_to_device(msg):
	with serial.Serial("/dev/tty.usbmodemPy3434341", 115200, timeout=None) as ser:
		send = time.time()
		print('Writing message to device: ' + msg)
		ser.write((msg+'\n').encode())
		
		return send

def listen_to_device():
    with serial.Serial("/dev/tty.usbmodemPy3434341", 116000, timeout=None) as ser:
        received = time.time()
        print("Reading")
        input = ser.readline()

        return received

def log_to_file(send, recieved):
    pass

def main():
	msg = sys.argv[1]
	#write_to_device(msg)
	listen_to_device()
    #log_to_file(write_to_device("True"), listen_to_device)

if __name__ == '__main__':
	main()