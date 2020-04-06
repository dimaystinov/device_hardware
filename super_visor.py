# python3
import socket
import sys
import time
import threading
import os
import subprocess


pid = os.getpid()
ppid = os.getppid()
print('pid ', pid)
print('ppid ', ppid)


def run_server(port=53214):
    serv_sock = create_serv_sock(port)
    cid = 0
    print('port: ', port)
    while True:
        client_sock = accept_client_conn(serv_sock, cid)
        t = threading.Thread(target=serve_client,
                             args=(client_sock, cid))
        t.start()
        cid += 1


def serve_client(client_sock, cid):
    request = read_request(client_sock)
    if request is None:
        print(f'Client #{cid} unexpectedly disconnected')
    else:
        response = handle_request(request)
        response1 = bytes.decode(response)
        print(str(response1))
        write_response(client_sock, response, cid)


def create_serv_sock(serv_port):
    serv_sock = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM,
                              proto=0)
    serv_sock.bind(('', serv_port))
    serv_sock.listen()
    return serv_sock


def accept_client_conn(serv_sock, cid):
    client_sock, client_addr = serv_sock.accept()
    print(f'Client #{cid} connected '
          f'{client_addr[0]}:{client_addr[1]}')
    return client_sock


def read_request(client_sock, delimiter=b'!'):
    request = bytearray()
    try:
        while True:
            chunk = client_sock.recv(1024)
            if not chunk:
                # Клиент преждевременно отключился.
                return None

            request = chunk

            print(str(chunk))
            if delimiter in request:
                print(request)
                return request

    except ConnectionResetError:
        # Соединение было неожиданно разорвано.
        return None
    except:
        raise


def handle_request(request):
    time.sleep(5)
    return request[::-1]


def write_response(client_sock, response, cid):
    client_sock.sendall(response)
    client_sock.close()
    print(f'Client #{cid} has been served')


'''if __name__ == '__main__':'''
server = threading.Thread(target=run_server)
server.start()
print(1)
ex = input()
str_ex = 'kill -9 '+str(pid)
if ex == '1':
    os.system(str_ex)
s = '1'
i = 0
result = subprocess.Popen(['python3', '2.py'], stdout=subprocess.PIPE)
print(str(bytes.decode(result.stdout.read())))
'''
while s!='0':
    i+=1
    result = subprocess.Popen(['python3', '2.py'], stdout=subprocess.PIPE)

    print(str(result.stdout))
    time.sleep(0.1)
    proc=result.pid
    print(proc)

    str_ex='kill -9 '+str(proc)

    os.system(str_ex)

    if i>100:
        s=input()
        i=0

'''
