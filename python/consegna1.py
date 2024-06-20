from math import pi

dizionarioforme = {1:"Quadrato", 2:"Cerchio", 3:"Rettangolo"}
listaUtente = [1,2,3]

while len(listaUtente) > 0:
    print("Le figure geometriche a scelta sono:\n")
    for i in dizionarioforme.keys ():
        if (i in listaUtente):
            print(f"{i}. {dizionarioforme[i]}")

    sceltaUtente = int (input ("\n"))

    if (sceltaUtente == 1):
        lato = float (input("\nInserisci il valore del lato del quadrato\n"))
        print("Il perimetro del quadrato è: ", lato * 4)
        print("L'area del quadrato è: ", lato ** lato)
    elif (sceltaUtente == 2):
        raggio = float (input("\nInserisci il valore del raggio del cerchio\n"))
        print("Il perimetro del cerchio è: ", raggio * 2 * pi)
        print("L'area del cerchio è: ", pi * (lato ** lato))
    elif (sceltaUtente == 3):
        base = float (input("\nInserisci il valore della base del rettangolo\n"))
        altezza = float (input("Inserisci il valore dell'altezza del rettangolo\n"))
        print("Il perimetro del rettangolo è: ", base * 2 + altezza * 2)
        print("L'area del rettangolo è: ", base * altezza)
    else:
        print ("Scelta non valida! Adios")
    listaUtente.remove (sceltaUtente)