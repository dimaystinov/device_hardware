
import paho.mqtt.client as mqtt



import socket
import sys
import time
import threading
import os
from subprocess import Popen, PIPE
import traceback
import __main__ as main





mqtt_username = "dimaystinov"
mqtt_password = "00000000"
mqtt_topic = "test"
mqtt_broker_ip = "192.168.137.220"


pid=os.getpid()
ppid=os.getppid()
PORT=3000
print('pid ',pid)
print('ppid ',ppid)

#Словарь С инФОРмАцИЕй О скрипте
inf={}
inf['name']=str(main.__file__)
inf['pid']=pid
inf['ppid']=ppid
inf['port']=PORT

#Собирает анные 
data={'status':'NotConnect','CO2':150,'hum':20,'temp':40}


def on_connect(client, userdata, flags, rc):
    
    print ("Connected!"+ str(rc))
    
   
    client.subscribe(mqtt_topic)
    
def on_message(client, userdata, msg):
    
    
    print ("Topic: "+ msg.topic + "\nMessage: " + str(msg.payload))
    

def mini_box(mqtt_username = "dimaystinov",mqtt_password = "00000000",mqtt_topic = "test",mqtt_broker_ip = "192.168.137.220"):
    
    client = mqtt.Client()

    client.username_pw_set(mqtt_username, mqtt_password)


        
        
    client.on_connect = on_connect
    client.on_message = on_message


    client.connect(mqtt_broker_ip, 1883)


    client.loop_forever()
    client.disconnect()

#Сервер
inf = {**inf,**data}
def run_server(port=PORT):
  flag=False
  
  
  while flag!=True: 
      try:
          serv_sock = create_serv_sock(port)
          flag=True
      except OSError:
          
          port+=1
      
  inf['port']=port
  cid = 0
  
  print(inf)
  
  while True:
    client_sock = accept_client_conn(serv_sock, cid)
    t = threading.Thread(target=serve_client,
                         args=(client_sock, cid))
    t.start()
    cid += 1
    if cid>=10:
        cid=0

def serve_client(client_sock, cid):
  request = read_request(client_sock)
  if request is None:
    print(f'Client #{cid} unexpectedly disconnected')
  else:
    response = str({**inf,**data}).encode()
    print(data)
    
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
      try:        
          request = json.loads(chunk.decode().replace("'","\""))
      except:
          request=chunk.decode()
      print(request)
      return request

  except ConnectionResetError:
    # Соединение было неожиданно разорвано.
    return None
  except:
    raise



def write_response(client_sock, response, cid):
  client_sock.sendall(response)
  client_sock.close()
  print(f'Client #{cid} has been served')

def print_data():
    print('print', data)
    time.sleep(10)



server=threading.Thread(target=run_server)
server.start()
mini_box=threading.Thread(target=mini_box)
mini_box.start()
print_data=threading.Thread(target=print_data)
print_data.start()
