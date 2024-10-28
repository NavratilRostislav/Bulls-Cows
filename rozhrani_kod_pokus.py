import tkinter as tk
#import Bull_and_cows
import random
import time

def spustit_aplikaci():
    root = tk.Tk()
    root.title("bull & cows")
    root.geometry("500x500")

#ukazatel realného času času 
    label_time = tk.Label(root, text="time",font=("Arial",15))
    label_time.place(x=15, y=2)

#label pro počitání pokusů
    label_pokus = tk.Label(root, text="počet pokusů: 0", font=("Arial",15))
    label_pokus.place(x=150,y=2)

#label text pro instrukce
    label_text = tk.Label(
        root,
        text=" "*6 + "Výtej ve hře Bull And cows.\n"
                      "Princip hry je následujci :\n" 
                      "Budeš hádat 4 místné číslo a musíš uhádnout číslo a umístění.",
        font=("Arial",10)
    )
    label_text.place(x=45, y=40)

    def aktualizuj_cas():
        aktualni_cas = time.strftime("%H:%M:%S")
        label_time.config(text=aktualni_cas)
        root.after(1000, aktualizuj_cas)

    def generovani_cisla():
        nahodne_cislo = random.sample(range(1, 10),4)
        print(f"(pro testovani:tajne cislo je {nahodne_cislo})") 

    button_vygeneruj_cislo = tk.Button(root, text="nahodné číslo",font=("Ariel",15))
    button_vygeneruj_cislo.place(x=30,y=100)    
            
    def zpracuj_vstup():
        uzivatelsky_vstup = entry_vstup.get()
        while True:
            if len(uzivatelsky_vstup) !=4 or not uzivatelsky_vstup.isdigit() or "0" in uzivatelsky_vstup:
                print("zadej čtyři číslice(0 není platná číslice).")
                continue
            uzivatelovo_cislo = [int(c)for c in uzivatelsky_vstup]
            return uzivatelovo_cislo    
    
    entry_vstup = tk.Entry(root,font=("Arial",15))
    entry_vstup.place(x=125,y=300)
        

    button_vstup = tk.Button(root, text="odeslat", command=zpracuj_vstup)
    button_vstup.place(x=200,y=350)

    def porovnej_cisla(nahodne_cislo, uzivatelovo_cislo):
        Bulls = 0
        cows = 0

        for i in range(4):
            if uzivatelovo_cislo [i] == nahodne_cislo[i]:
                Bulls+=1
            elif uzivatelovo_cislo [i] in nahodne_cislo:
                cows +=1
        
        return Bulls,cows

    def aktualizuj_pokus():
        aktualni_pocet = Bull_and_cows.pokus
        label_pokus.config(text=f"Počet pokusů: {aktualni_pocet}")
        root.after(1000, aktualizuj_pokus)
       
     
    

    def zavri_aplikaci():
        root.destroy()
            
    button_zavrit = tk.Button(root, text="zavrit aplikaci",bg="black", fg="white",command=zavri_aplikaci)
    button_zavrit.place(x=200,y=470)   
        
    aktualizuj_cas()
    root.mainloop()

if __name__=="__main__":
    spustit_aplikaci()