
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cambiandolo a stream le indicamos que queremos usar TCP
s.connect(("localhost", 9999))

#while True:
mensaje = input("Mensaje a enviar >> ")
s.send(mensaje.encode())
#if mensaje == "close":
#break
#print("Adios.")
s.close()

