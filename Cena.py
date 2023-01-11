P1 = int(input("Inserisci l'età della prima persona: "))
P2 = int(input("Inserisci l'età della seconda persona: "))
P3 = int(input("Inserisci l'età della terza persona: "))

PDISC = 100
PVEG = 10
PBS = 10 
PPI = 10

if(P1>=18):
    CP1 = 30
    CP1 = CP1 + PDISC
elif(P1 >= 6 and P1 <=17):
    CP1 = 20
else:
    CP1 = 10
    CP1 = CP1 + PBS
    QP = input("La prima persona vuole usufruire di giochi pirotecnici? (SI/NO)")
    if(QP == "SI"):
        CP1 = CP1 + PPI 

if(P2>=18):
    CP2 = 30
    CP2 = CP2 + PDISC
elif(P2 >= 6 and P2 <=17):
    CP2 = 20
else:
    CP2 = 10
    CP2 = CP2 + PBS
    QP = input("La seconda persona vuole usufruire di giochi pirotecnici? (SI/NO)")
    if(QP == "SI"):
        CP2 = CP2 + PPI

if(P3>=18):
    CP3 = 30
    CP3 = CP3 + PDISC
elif(P3 >= 6 and P3 <=17):
    CP3 = 20
else:
    CP3 = 10
    CP3 = CP3 + PBS
    QP = input("La terza persona vuole usufruire di giochi pirotecnici? (SI/NO)")
    if(QP == "SI"):
        CP3 = CP3 + PPI

TOT = CP1 + CP2 + CP3

QC = input("Qualcuno vuole lo champagne? (SI/NO)")
if(QC == "SI" or QC == "Si" or QC == "si" or QC == "sI"):
    if(P1 >= 18 and P2 >= 18 and P3 >= 18):
        
        NCHAM = int(input("Inserisci il numero di bicchieri: "))

        while NCHAM >3:
            NCHAM = int(input("Inserisci il numero di bicchieri: "))
        else:
            PCHAM = float(input("Inserisci il prezzo dello champagne: €"))
            TOT = TOT + (NCHAM*PCHAM)

QV = input("Qualcuno è vegano? (SI/NO)")
if(QV == "SI" or QV == "Si" or QV == "si" or QV == "sI"):

    NVEG = int(input("Inserisci il numero di persone vegane: "))

    while NVEG >3:
        NVEG = int(input("Il numero della persona non può essere più di 3"))
    else:
        TOT = TOT + (PVEG*NVEG)

print("Totale dell'importo: €", TOT)
