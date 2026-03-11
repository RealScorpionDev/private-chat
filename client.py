import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("Enter server IP: ")
client.connect((server_ip, 9999))

def receive():
    while True:
        try:
            data = client.recv(1024)
            print(data.decode())
        except:
            break
        
thread = threading.Thread(target=receive)
thread.start()

user_name = input("Whats your name: ")

while True:
    msg = input()
    client.send((f"{user_name}: " + msg).encode())