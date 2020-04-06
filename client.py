from socket import *
import sys
import time

host = 'localhost'
port = 53213
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
# flag=True
'''while flag:
    try:'''
tcp_socket.connect(addr)
'''flag=False
    except:
        print('try')
        time.sleep(3)
'''


data = 'hello'
if not data:
    tcp_socket.close()
    sys.exit(1)

# encode - перекодирует введенные данные в байты, decode - обратно
data = str.encode(data)
tcp_socket.send(data)

data = tcp_socket.recv(1024)
data = bytes.decode(data)
print(str(data))


tcp_socket.close()
