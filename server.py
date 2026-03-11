import socket
import threading

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))

server.listen(5)

def handle_client(client):
   while True:
      data = client.recv(1024)
      if not data:
         break
      for c in clients:
         if c != client:
            c.send(data)
      print(data.decode())

while True:
   client, addr = server.accept()
   clients.append(client)
   thread = threading.Thread(target=handle_client, args=(client, ))
   thread.start()