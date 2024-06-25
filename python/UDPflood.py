import socket
import random
import string
import time

def randomDelay ():
    return random.uniform(0, 0.1)

def PIDmaker():
    PID = ""
    while len(PID) < 1024 + 1:
        PID += random.choice(string.hexdigits)
    return PID

def main():
    targetIP = input ("Inserisci IP: \n")
    UDPport = int(input("Inserisci la porta: \n"))
    PIDnumber = int(input("Inserisci il num di pacchetti da inviare"))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((targetIP, UDPport))
    
    for x in range(0, PIDnumber, 1):
        s.sendall(PIDmaker().encode("utf-8"))
        print(f"{x} pacchetti inviati")
        time.sleep(randomDelay())
    s.close()

if __name__ == "_main_":
    main()
    