import tkinter as tk
import Bull_and_cows
import time

def aktualizuj_cas():
    aktualni_cas = time.strftime("%H:%M:%S")# získání aktuálního času ve formátu HH:MM:SS
    Label.config(text=aktualni_cas)
    root.after(1000, aktualizuj_cas)# aktualizace každou sekundu


#vytvoříme základní okno 
root = tk.Tk()
root.title("bull & cows.py")

#nastavení velikosti okna
root.geometry("500x500")# šířka výška v px

#přidání labelu pro zobrazení čsu 
Label = tk.Label(root, text="time",font=("Arial",15)) # vytvoření labelu s prazdným textem 
Label.place(x=15, y=2)#umýstění labelu na presne dane mysto



#funkce pro začátek hry
def zacni_hru():
    button.config(text="hra začíná") #změna textu tlačítka
    Bull_and_cows.spustit_hru() # spustí logiku hry z importovaného souboru

# nastavení tlačítka
button = tk.Button(root, text="play",command=zacni_hru)
button.pack() # umístění tlačítka 

#funkce pro zavření aplikace
def zavri_aplikaci():
    root.destroy() #zavře hlavní okno a ukončí aplikaci

#přidání tlačítka pro zavření aplikace
button_zavrit = tk.Button(root, text= "zavři aplikaci",command=zavri_aplikaci)
button_zavrit.pack() #umístění tlačítka do okna 

#funkce pro spustění aktualizace času
aktualizuj_cas()

#spuštění aplikace
root.mainloop()