import socket as so

target = input("Inserici l'ip da scansionare: ")
portrange = input("inserici un range di porte da scansire (es 0-200): ")

lowport = 0
highport = 200

if portrange.find("-") == 1:
    lowport = int(portrange.split("-")[0])
    highport = int(portrange.split("-")[1])

print(f"Verranno scansite le porte da {lowport} a {highport}")
closePort = []
for port in range(lowport, highport+1):
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0): print("*** Porta {port} Aperta ***")
    else: closePort.append(port)
    s.close()
print("Porte chiuse: ", closePort)