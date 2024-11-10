# Python Socket Communication
This project demonstrates basic network connections in Python using TCP and UDP sockets. It includes examples of client-server communication via both protocols.

Files
clientTCP.py: Client that sends messages to a server using the TCP protocol.
serverTCP.py: Server that receives and responds to messages from the TCP client.
clientUDP.py: Client that sends messages to a server using the UDP protocol.
serverUDP.py: Server that listens and receives messages from the UDP client.
Requirements
Python 3.x
Running the Project
TCP Server:

Run serverTCP.py to start the TCP server on port 9999.
TCP Client:

Run clientTCP.py and type a message to send it to the server.
Type close to end the connection.
UDP Server:

Run serverUDP.py to start the UDP server on port 12345.
UDP Client:

Run clientUDP.py to send a test message to the UDP server.
Description
TCP: A connection-oriented protocol. The client connects to the server, sends a message, waits for a response, and then closes the connection.
UDP: A connectionless protocol. The client sends a message to the server without establishing a continuous connection, useful for quick messages or networks that can tolerate lower reliability.
Notes
Change localhost to a specific IP if testing on different devices.
Ensure that ports 9999 and 12345 are available and not blocked by a firewall.
