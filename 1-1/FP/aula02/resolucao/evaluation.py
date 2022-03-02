import math 
ATP1 = float(input("Valor de ATP1? "))
ATP2 = float(input("Valor de ATP2? "))
APA = float(input("Valor de APA? "))
APF = float(input("Valor de APF? "))
CTP = (ATP1+ATP2)/2
CP = (APA+APF)/2

NF = 0.36 * CTP + 0.64 * CP

if(ATP1 > 20 or ATP2 > 20 or APA > 20 or APA > 20):
    print("Nota de componente > 20 impossivel")
    exit(1)


if (CTP < 6.5 or CP < 6.5):
    print("Nota Final: Código 66")
else:
    if(NF < 10):
        ATPR = float(input("Valor de ATPR? "))
        APR = float(input("Valor de ATR? "))

        if(ATPR > 20 or APR > 20):
            print("Nota de componente > 20 impossivel")
            exit(1)

        NR = 0.36 * max(CTP, ATPR) + 0.64 * max(CP, APR, 0.25 * APA + 0.75 * APR)

        if(ATPR < 6.5 or APR < 6.5):
            exit(1)
        else:
            print("Nota Final:", NR)
    else:
        print("Nota Final:", NF)