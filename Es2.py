import tkinter as tk

def Risultato():

    ST = float(enST.get())

    if(float(enST.get())<5000):
        if(int(enAS.get())>=30):
            ST = ST-(ST*4/100)
        elif(int(enAS.get())>=10):
            ST = ST-(ST*8/100)
        else:
            ST = ST-(ST*12/100)       
    else:
        laR ["text"] = f"Totale dell'importo {ST}" 

    laR ["text"] = f"Totale dell'importo {ST}"                 
            

main = tk.Tk()
main.geometry("250x180")
main.resizable(False, False)
main.title("Es 1")

laST = tk.Label(main, text="Inserisci lo stipendio")
laST.pack()

enST = tk.Entry(main)
enST.pack()

laAS = tk.Label(main, text="Inserisci l'anzianità di servizio")
laAS.pack()

enAS = tk.Entry(main)
enAS.pack()

laR = tk.Label(main, text="")
laR.pack()

button = tk.Button(main, text="Invia", command=Risultato)
button.pack()


main.mainloop()