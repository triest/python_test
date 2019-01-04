# socket_echo_client.py

import socket
import sys
import json

exampleData = {'method': 'deposit',
               'date': '2018-10-09',
               'account': 'bob',
               'amt': 10,
               'ccy': 'EUR'}


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'This is the message.  It will be repeated. New';
    raw_data = json.dumps(exampleData, ensure_ascii=False).encode("utf-8")  # кодирует json в байтовый вид
    message = raw_data

    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(200)  #new light 200
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
