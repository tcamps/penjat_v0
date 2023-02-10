import time
import os

paraula = 'BARCELONA'
tipus = 'CIUTAT'

lletres_entrades = []

errors = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###### JOC DEL PENJAT ######")
    # Dibuixa pista
    print(f"{tipus} de {len(paraula)} lletres\n")

    # Dibuixa paraula i comprova si s'ha encertat
    encertada = True
    for lletra in paraula:
        if lletra in lletres_entrades:
            print(f"{lletra:3}", end=" ")
        else:
            print(f"{'__':3}", end=" ")
            encertada = False
    
    # Ha encertat. S'acaba el joc sortint del bucle
    if encertada:
        print("\nENHORABONA. HAS GUANYAT!!!!")
        time.sleep(2)
        break;

    # Mostra errors / Dibuixa penjat i controla el Game Over sortint del bucle
    #print(f"\nErrors: {errors}")
    if (errors >= 1):
        print("\n\n---------|")
    if (errors >= 2):
        print("         o")
    if (errors >= 3):
        print("        /|\\")
    if (errors >=4):
        print("        / \\")
        print("\nHAS PERDUT!!!")
        time.sleep(2)
        break;
 
    # Demana nova lletra
    lletra = input("\nIntrodueix una lletra: ").capitalize()
    if lletra not in lletres_entrades:
        lletres_entrades.append(lletra)
        if lletra not in paraula:
            errors += 1

