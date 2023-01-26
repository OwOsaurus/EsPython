import tkinter as tk

def Risultato():

    if(int(enE.get())>=21):
            laR ["text"] = f"Si può guidare le auto di tutti i tipi"
    elif(int(enE.get())>=18):
            laR ["text"] = f"Si può guidare l'auto fino a 150 Km/h"
    elif(int(enE.get())>=16):
            laR ["text"] = f"Si può guidare la moto fino a 125cc"
    elif(int(enE.get())>=14):
            laR ["text"] = f"Si può guidare il motorino da 50cc"
    else:
            laR ["text"] = f"Non si può guidare"        

main = tk.Tk()
main.geometry("250x110")
main.resizable(False, False)
main.title("Es 1")

laE = tk.Label(main, text="Inserisci l'età")
laE.pack()

enE = tk.Entry(main)
enE.pack()

laR = tk.Label(main, text="")
laR.pack()

button = tk.Button(main, text="Invia", command=Risultato)
button.pack()


main.mainloop()