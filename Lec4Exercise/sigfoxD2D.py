from network import Sigfox

sigfox = Sigfox(mode=Sigfox.FSK, frequency=868000000)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)

while True:
  s.send('Device-1')
  time.sleep(1)
  print(s.recv(64))