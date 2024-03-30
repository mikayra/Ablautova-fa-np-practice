import socket
import threading


sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)


def proc(n, msg=None):
  msg = ''
  data = conn.recv(1024)
  msg += data.decode()
  conn.send(data)
  print(msg)
  conn.close()


while True:
  conn, addr = sock.accept()
  print(addr)
  p1 = threading.Thread(target=proc, name='t1', args=['1'])
  p1.start()
