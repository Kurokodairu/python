import socket
import tkinter

HOST = '127.0.0.1'
PORT = 5001

socket = socket.socket()
socket.connect((HOST, PORT))

data = 'Test 1'

socket.sendall(data.encode())

data = socket.recv(1024).decode()

print(data)
