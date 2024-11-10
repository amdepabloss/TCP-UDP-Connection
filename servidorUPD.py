import socket  #importo biblioteca
#s_server es nuestro socket AF_INET (Adress Family) socket.SOCK_DGRAM elegimos el servicio
s_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s_server.bind(('', 12345)) #Indicamos en que puerto se va a escuchar (Tener cuidado porque hay puertos en los que ya se esta escuchando)
data, clientaddr = s_server.recvfrom(4096)  
print (clientaddr)
s_server.close()

#py clienteUDP.py