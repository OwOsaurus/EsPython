
M = 0
loopExecuted = False

VC = float(input("Enter Caffè Venduto: "))
VT = float(input("Enter Tè Venduto: "))


while True:


    TV = VC+VT
    
    if VC>5000:
        PC = VC*0.1
    else:
        PC = VC*0.05

    if VT>10000:
        PT = VT*0.16
    else:
        PT = VT*0.04

    if TV>20000:
        PTV = TV*0.12
    else:
        PTV = 0

    TP = PC + PT + PTV
    M += 1

    loopExecuted = True
    
    VC = 0
    VT = 0

    if loopExecuted == True:
        print("Il totale per il mese", M, "è:",TP)
        VC = float(input("Enter Caffè Venduto: "))
        VT = float(input("Enter Tè Venduto: "))

        if VC > 0 and VT > 0:
            continue
        break
    



