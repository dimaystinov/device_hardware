# python3
import socket
import sys
import time
import threading
import os
from subprocess import Popen, PIPE
from socket import *




pid=os.getpid()
ppid=os.getppid()
print('pid ',pid)
print('ppid ',ppid)



def run_scrypt(name):
    name=str(name)
    

    with Popen([sys.executable, '-u', name],
           stdout=PIPE, universal_newlines=True) as process:
        for line in process.stdout:
            print(line,end='')
            
        print('End of process ',name)

def client(port = 3000):
    host = 'localhost'
    port = 3000
    addr = (host,port)

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    #flag=True

    tcp_socket.connect(addr)




    data = 'hello'
    if not data : 
        tcp_socket.close() 
        sys.exit(1)

    #encode - перекодирует введенные данные в байты, decode - обратно
    data = str.encode(data)
    tcp_socket.send(data)

    data = tcp_socket.recv(1024)
    data = bytes.decode(data)
    print(str(data))


    tcp_socket.close()



opros_mini_box=threading.Thread(target=client)
opros_mini_box.start()
scrypt1=threading.Thread(target=run_scrypt('mqtt_minibox.py'))
scrypt1.start()


ex=input()

exit()



