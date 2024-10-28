import random

#globální proměnne
pokus = 0
tajne_cislo = []

# Generování tajného čísla jako seznam čtyř jedinečných náhodných číslic    
def nahodne_cislo():    
    global pokus, tajne_cislo
    
    tajne_cislo = random.sample(range(1, 10), 4)# vybere 4 jedinečné číslice z 1-9
    pokus = 0 #inicializace počítadla pokusů
    print(f"(pro testovani:tajne cislo je {tajne_cislo})")

#Funkce pro získání vstupu od uživatele
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

while True:
    uzivatelovo_cislo = ziskej_uzivatelsky_vstup()
    pokus +=1 # zvyšuje počet pokusů při každém vstupu

    Bulls, cows = porovnej_cisla(tajne_cislo, uzivatelovo_cislo)
    print(f"Bulls:{Bulls},Cows:{cows}")

    if Bulls == 4:
        print(f"Gratulace.Uhadl-a jis správně čislo po {pokus} pokusech.")
        break
    
    

    
