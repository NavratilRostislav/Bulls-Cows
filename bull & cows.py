#import keyboard nejdřív naistalovat a pročíst si příkazy
import random
print("Výtej ve hře Bull And cows.princip hry je následujci : budeš hádat 4 místné číslo a musíš uhádnout číslo a umístění.")
#promněné pro čísla 
cislo1 = random.randint(1, 9)
cislo2 = random.randint(1, 9)
cislo3 = random.randint(1, 9)
cislo4 = random.randint(1, 9)
tajne_cislo = [cislo1, cislo2, cislo3, cislo4]

print(tajne_cislo)

#funkce pro tajne číslo
def ziskej_uzivatelsky_vstup():
    while True: #smyčka, dokud nedostaneme správný vstup 
        vstup = input("zadej 4-mýstné číslo: ")
    
        if len(vstup) != 4 or not vstup.isdigit() or "0" in vstup:
            print("zadej čtyři číslice(0 není platná číslice).")
            continue #Znovu vyžádat vstup
                #převede seznam na celá čísla
        uzivatelovo_cislo = [int(c) for c in vstup]
        return uzivatelovo_cislo

#porovnávání tajneho čísla s uživatelovým číslem 
def porovnej_cisla(tajne_cislo, uzivatelovo_cislo):
    
    Bulls = 0
    cows = 0
    
    #porovnej číslice
    for i in range(4):
        if uzivatelovo_cislo [i] == tajne_cislo[i]:
            Bulls +=1
        elif uzivatelovo_cislo [i] in tajne_cislo:
            cows += 1

    return Bulls, cows
#hlavní smyčka hry
pokus = 0 #inicializace počitadla pokusů

while True:
    uzivatelovo_cislo = ziskej_uzivatelsky_vstup()
    pokus +=1 # zvyšuje počet pokusů při každém vstupu

    Bulls, cows = porovnej_cisla(tajne_cislo, uzivatelovo_cislo)
    print(f"Bulls:{Bulls},Cows:{cows}")

    if Bulls == 4:
        print(f"Gratulace.Uhadl-a jis správně čislo po {pokus} pokusech.")
        break
