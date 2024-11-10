<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Socket Communication</title>
</head>
<body>
  <h1>Python Socket Communication</h1>

  <p>This project demonstrates basic network connections in Python using TCP and UDP sockets. It includes examples of client-server communication via both protocols.</p>

  <h2>Files</h2>
  <ul>
    <li><strong>clientTCP.py</strong>: Client that sends messages to a server using the TCP protocol.</li>
    <li><strong>serverTCP.py</strong>: Server that receives and responds to messages from the TCP client.</li>
    <li><strong>clientUDP.py</strong>: Client that sends messages to a server using the UDP protocol.</li>
    <li><strong>serverUDP.py</strong>: Server that listens and receives messages from the UDP client.</li>
  </ul>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
  </ul>

  <h2>Running the Project</h2>
  <ol>
    <li><strong>TCP Server</strong>: Run <code>serverTCP.py</code> to start the TCP server on port <code>9999</code>.</li>
    <li><strong>TCP Client</strong>: Run <code>clientTCP.py</code> and type a message to send it to the server. Type <code>close</code> to end the connection.</li>
    <li><strong>UDP Server</strong>: Run <code>serverUDP.py</code> to start the UDP server on port <code>12345</code>.</li>
    <li><strong>UDP Client</strong>: Run <code>clientUDP.py</code> to send a test message to the UDP server.</li>
  </ol>

  <h2>Description</h2>
  <ul>
    <li><strong>TCP</strong>: A connection-oriented protocol. The client connects to the server, sends a message, waits for a response, and then closes the connection.</li>
    <li><strong>UDP</strong>: A connectionless protocol. The client sends a message to the server without establishing a continuous connection, useful for quick messages or networks that can tolerate lower reliability.</li>
  </ul>

  <h2>Notes</h2>
  <ul>
    <li>Change <code>localhost</code> to a specific IP if testing on different devices.</li>
    <li>Ensure that ports <code>9999</code> and <code>12345</code> are available and not blocked by a firewall.</li>
  </ul>
</body>
</html>
