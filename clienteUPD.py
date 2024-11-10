import socket #importo biblioteca
s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Esto lo comparten cliente y servidor
s_client.sendto(b'Hola clase', ('localhost', 12345)) #Indicamos a quien se lo enviamos. Si en localhost ponemos una IP se envía allí
s_client.close()

#servidorUDP.py