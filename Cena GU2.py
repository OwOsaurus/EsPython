import tkinter as tk

def Total():

    PDISC = 100
    PVEG = 10
    PBS = 10 
    PPI = 10

    #Prima persona
    if(int(enP1.get())>=18):
        CP1 = 30
        CP1 = CP1 + PDISC
    elif(int(enP1.get()) >= 6 and int(enP1.get()) <=17):
        CP1 = 20
    else:
        CP1 = 10
        CP1 = CP1 + PBS
        laQP1.pack()
        enQP1.pack()
        if enQP1.get() == "SI":

            CP1 = CP1 + PPI

        elif enQP1.get() == "Si":

            CP1 = CP1 + PPI
    
        elif enQP1.get() == "si":

            CP1 = CP1 + PPI

        elif enQP1.get() == "sI":

            CP1 = CP1 + PPI
        
        else:

            CP1 += 0

    #Seconda persona
    if(int(enP2.get())>=18):
        CP2 = 30
        CP2 = CP2 + PDISC
    elif(int(enP2.get()) >= 6 and int(enP2.get()) <=17):
        CP2 = 20
    else:
        CP2 = 10
        CP2 = CP2 + PBS
        laQP2.pack()
        enQP2.pack()
        if enQP2.get() == "SI":

            CP2 = CP2 + PPI

        elif enQP2.get() == "Si":

            CP2 = CP2 + PPI
    
        elif enQP2.get() == "si":

            CP2 = CP2 + PPI

        elif enQP2.get() == "sI":

            CP2 = CP2 + PPI
        
        else:

            CP2 += 0

    #Terza persona
    if(int(enP3.get())>=18):
        CP3 = 30
        CP3 = CP3 + PDISC
    elif(int(enP3.get()) >= 6 and int(enP3.get()) <=17):
        CP3 = 20
    else:
        CP3 = 10
        CP3 = CP3 + PBS
        laQP3.pack()
        enQP3.pack()
        if enQP3.get() == "SI":

            CP3 = CP3 + PPI

        elif enQP3.get() == "Si":

            CP3 = CP3 + PPI
    
        elif enQP3.get() == "si":

            CP3 = CP3 + PPI

        elif enQP2.get() == "sI":

            CP3 = CP3 + PPI
        
        else:

            CP3 += 0


    #Totale
    TOT = CP1 + CP2 + CP3

    #Champagne

    if enQC.get() == "SI":

            NCHAM = int(enNCHAM.get())

            while NCHAM >3:
                NCHAM = int(enNCHAM.get())
            else:
                PCHAM = float(enPCHAM.get())
                TOT = TOT + (NCHAM*PCHAM)

    elif enQC.get() == "Si":

            NCHAM = int(enNCHAM.get())

            while NCHAM >3:
                NCHAM = int(enNCHAM.get())
            else:
                PCHAM = float(enPCHAM.get())
                TOT = TOT + (NCHAM*PCHAM)
    
    elif enQC.get() == "si":

            NCHAM = int(enNCHAM.get())

            while NCHAM >3:
                NCHAM = int(enNCHAM.get())
            else:
                PCHAM = float(enPCHAM.get())
                TOT = TOT + (NCHAM*PCHAM)
    
    elif enQC.get() == "sI":

            NCHAM = int(enNCHAM.get())

            while NCHAM >3:
                NCHAM = int(enNCHAM.get())
            else:
                PCHAM = float(enPCHAM.get())
                TOT = TOT + (NCHAM*PCHAM)

    else:

        TOT += 0

    #Vegan
    if enQV.get() == "SI":

            NVEG = int(enNVEG.get())

            while NVEG >3:
                NVEG = int(enNVEG.get())
                print("Il numero della persona non può essere più di 3")
            else:
                TOT = TOT + (PVEG*NVEG)

    elif enQV.get() == "Si":

            NVEG = int(enNVEG.get())

            while NVEG >3:
                NVEG = int(enNVEG.get())
                print("Il numero della persona non può essere più di 3")
            else:
                TOT = TOT + (PVEG*NVEG)
    
    elif enQV.get() == "si":

            NVEG = int(enNVEG.get())

            while NVEG >3:
                NVEG = int(enNVEG.get())
                print("Il numero della persona non può essere più di 3")
            else:
                TOT = TOT + (PVEG*NVEG)
    
    elif enQV.get() == "sI":

            NVEG = int(enNVEG.get())

            while NVEG >3:
                NVEG = int(enNVEG.get())
                print("Il numero della persona non può essere più di 3")
            else:
                TOT = TOT + (PVEG*NVEG)
    
    else:

        TOT += 0


    #Importo finale
    laTOT ["text"] = f"Totale dell'importo {TOT}"

    #Piro P1
    if enQP1.get() == "SI":

        CP1 = CP1 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    elif enQP1.get() == "Si":

        CP1 = CP1 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"
    elif enQP1.get() == "si":

        CP1 = CP1 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    elif enQP1.get() == "sI":

        CP1 = CP1 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"       
    else:

        CP1 += 0
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    #Piro P2
    if enQP2.get() == "SI":

        CP2 = CP2 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    elif enQP2.get() == "Si":

        CP2 = CP2 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"   
    elif enQP2.get() == "si":

        CP2 = CP2 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"
    elif enQP2.get() == "sI":

        CP2 = CP2 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"        
    else:

        CP2 += 0
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    #Piro P3
    if enQP3.get() == "SI":

        CP3 = CP3 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    elif enQP3.get() == "Si":

        CP3 = CP3 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    elif enQP3.get() == "si":

        CP3 = CP3 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"

    elif enQP2.get() == "sI":

        CP3 = CP3 + PPI
        laTOT ["text"] = f"Totale dell'importo {TOT}"
                
    else:

        CP3 += 0
        laTOT ["text"] = f"Totale dell'importo {TOT}"


#Tabella
main = tk.Tk()
main.geometry("400x500")
main.resizable(height=True, width=True)
main.title("Cena 2023")

#Età della prima persona
laP1 = tk.Label(main, text="Inserisci l'età della prima persona")
laP1.pack()
enP1 = tk.Entry(main)
enP1.pack()

#Età della seconda persona
laP2 = tk.Label(main, text="Inserisci l'età della seconda persona")
laP2.pack()
enP2 = tk.Entry(main)
enP2.pack()

#Età della terza persona
laP3 = tk.Label(main, text="Inserisci l'età della terza persona")
laP3.pack()
enP3 = tk.Entry(main)
enP3.pack()

#Giochi pirotecnici P1
laQP1 = tk.Label(main, text="La prima persona vuole usufruire di giochi pirotecnici? (SI/NO)")
enQP1 = tk.Entry(main)

#Giochi pirotecnici P2
laQP2 = tk.Label(main, text="La seconda persona vuole usufruire di giochi pirotecnici? (SI/NO)")
enQP2 = tk.Entry(main)

#Giochi pirotecnici P3
laQP3 = tk.Label(main, text="La terza persona vuole usufruire di giochi pirotecnici? (SI/NO)")
enQP3 = tk.Entry(main)

#Champagne
laQC = tk.Label(main, text="Qualcuno vuole lo champagne? (SI/NO)")
laQC.pack()
enQC = tk.Entry(main)
enQC.pack()

#Champagne = numero del bicchiere
laNCHAM = tk.Label(main, text="Inserisci il numero di bicchieri: ")
laNCHAM.pack()
enNCHAM = tk.Entry(main)
enNCHAM.pack()

#Champagne = prezzo
laPCHAM = tk.Label(main, text="Inserisci il prezzo dello champagne (€)")
laPCHAM.pack()
enPCHAM = tk.Entry(main)
enPCHAM.pack()

#Vegan
laQV = tk.Label(main, text="Qualcuno è vegano? (SI/NO)")
laQV.pack()
enQV = tk.Entry(main)
enQV.pack()

#Vegan = numero
laNVEG = tk.Label(main, text="Inserisci il numero di persone vegane: ")
laNVEG.pack()
enNVEG = tk.Entry(main)
enNVEG.pack()

#Pulsante per calcolare il totale
button = tk.Button(main, text="Calcola totale", command=Total)
button.pack()

#TOT
laTOT = tk.Label(main, text="")
laTOT.pack()


main.mainloop()