import socket

s = socket.socket()

host = '192.168.64.146'
port = 13339

s.bind((host, port))

#while True:
s.listen(5)
c, addr = s.accept()  # c is a socket object, addr is tuple ('ip', port)
print("Got connection from {}".format(addr))
data = "Thank you for connecting to {}:{} ".format(host, port)
c.send(data.encode('utf-8'))
c.close()
