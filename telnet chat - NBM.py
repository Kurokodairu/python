import socket
import _thread as thread
import time
 
HOST = "192.168.0.16"
PORT = 4004
 

def accept(conn):
    def threaded():
        while True:
            conn.sendall("Please enter your name: ".encode())
            try:
                name = conn.recv(1024).strip().decode()
            except socket.error:
                continue
            if name in users:
                conn.sendall("Name entered is already in use.\n".encode())
            elif name:
                conn.setblocking(False)
                users[name] = conn
                broadcast(name, "+++ %s Joined +++" % name)
            break
    thread.start_new_thread(threaded, ())
 

def broadcast(name, message):
    print(message)
    for to_name, conn in users.items():
        if to_name != name:

            try:
                if isinstance(message, str):
                    conn.sendall(bytes(message, 'utf-8') + bytes("\n", 'utf-8'))
                else:
                    conn.sendall(message.encode() + "\n")
            except socket.error:
                pass


# SERVER 


# Set up the server socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)
server.bind((HOST, PORT))
server.listen(1)
print("Listening on %s" % ("%s:%s" % server.getsockname()))
 
# Main event loop.
users = {}
while True:
    try:
        # Accept new connections.
        while True:
            try:
                conn, addr = server.accept()
            except socket.error:
                break
            accept(conn)
        # Read from connections.
        for name, conn in list(users.items()):
            try:
                message = conn.recv(1024)
            except socket.error:
                continue
            if not message:
                # Empty string is given on disconnect.
                del users[name]
                broadcast(name, "--- %s Left ---" % name)

            elif message.decode() == 'test':
                print('tested')

            else:
                try:
                    broadcast(name, "%s> %s" % (name, message.strip().decode()))
                except UnicodeDecodeError:
                    break
        time.sleep(.1)
    except (SystemExit, KeyboardInterrupt):
        break
