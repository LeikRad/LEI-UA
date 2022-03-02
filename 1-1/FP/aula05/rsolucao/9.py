def main():
    StringUsrInp = input("String Input? \n")
    IntUsrInp = int(input("Int Input? \n"))
    LstUsrInp = []
    print("Escreva um numero para a lista ou deixe vazio para acabar a sua lista")
    
    while True:
        usrInput = input("Numero? ")
        if (usrInput == ""):
            break
        LstUsrInp.append(float(usrInput))

    print(evenThenOdd(StringUsrInp))
    print(noDups(StringUsrInp))
    print(nFunction(IntUsrInp))
    print(maxLst(LstUsrInp))

def maxLst(Lst):
    i = 1
    mx = Lst[0]
    mxLocal = 0
    while(i < len(Lst)):
        if(mx < Lst[i]):
            mx = Lst[i]
            mxLocal = i
        i += 1
    return(mxLocal)            

def evenThenOdd(txt):
    i = 0
    j = 1
    eto = ""
    while(i < len(txt)):
        eto = eto + txt[i]
        i += 2
    while(j < len(txt)):
        eto = eto + txt[j]
        j +=2
    return(eto)

def noDups(txt):
    i = 1
    ND = txt[0]
    while(i < len(txt)):
        if(txt[i] == txt[i-1]):
            i +=1
            continue
        else:
            ND = ND + txt[i]
        i += 1
    return(ND)

def nFunction(n):
    lst = []
    i = 1

    while (i <= n):
        j = 1
        while (j <= i):
            lst.append(i)
            j += 1
        i += 1
    return(lst)


if __name__ == "__main__":
    main()