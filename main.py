

import socket

oursocket = socket.socket()
oursocket.bind(('localhost',8080))
oursocket.listen(5)
conexion, adr = oursocket.accept();
print("Nueva conexion establecida")
print(adr)
while True:
    peticion = conexion.recv(1024).decode()
    print(peticion)
    conexion.send(input().encode())

conexion.close()

