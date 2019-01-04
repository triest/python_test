# socket_echo_server.py

import socket
import sys
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(200)

            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                data = json.loads(data.decode("utf-8"))  # назад в json
                print(data);
                data = json.dumps(data, ensure_ascii=False).encode("utf-8")  # кодирует json в байтовый вид
                connection.sendall(data)  # отправляем назад

            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
