

def lunghezze_parole(n):
    z = []
    for parola in n:
        z.append(len(parola))
    return z

parola = ["cyberpunk", "gatto", "comodino", "acqua", "alcool"]
lunghezze = lunghezze_parole(parola)
print ("\n", parola ,"\n")
print(lunghezze)
