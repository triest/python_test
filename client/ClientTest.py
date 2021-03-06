# socket_echo_client.py

import socket
import sys
import json

exampleData = {'method': 'deposit',
               'date': '2018-10-09',
               'account': 'bob',
               'amt': 10,
               'ccy': 'EUR'}

exampleData2 = {'method': 'transfer',
                'date': '2018-10-09',
                'to_account': 'bob',
                'from_account': 'alice',
                'amt': 100,
                'ccy': 'GBP'}

exampleData3 = {'method': 'withdrawal',
                'date': '2018-10-09',
                'account': 'alice',
                'amt': 10,
                'ccy': 'EUR'}

exampleData4 = {'method': 'get_balances',
                'date': '2018-10-09',
                'account': 'bob'}

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'This is the message.  It will be repeated. New';
    message = json.dumps(exampleData4, ensure_ascii=False).encode("utf-8")  # кодирует json в байтовый вид

    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(200)  # new light 200
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
