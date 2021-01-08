import socket

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    new_socket.connect(('data.pr4e.org', 80))
except socket.error as err:
    print(err)

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

new_socket.send(cmd)


while True:
    data = new_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

new_socket.close()