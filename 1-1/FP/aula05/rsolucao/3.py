def main():
    FList = inputFloatList()
    print(FList)
    mini, maxi = minmax(FList)
    print(mini, maxi)
    v = (maxi + mini)/2
    print(v)
    InfVList = countLower(FList, v)
    print(InfVList)

def inputFloatList():
    TList = []
    while True:
        while True:
            usrInp = input("Número? ")
            if(usrInp.isnumeric() or usrInp == ""):
                break
        if(usrInp == ""):
            break
        TList.append(float(usrInp))
    return(TList)

def countLower(lst, v):
    TList = []
    for i in lst:
        if i < v:
            TList.append(i)
    return(len(TList))

def minmax(lst):
    #return(min(lst), max(lst))
    mx = lst[0] 
    mi = lst[0]
    for i in lst:
        if mx < i:
            mx = i
        if mi > i:
            mi = i
    return(mi, mx)
        

    

if __name__ == "__main__":
    main()
