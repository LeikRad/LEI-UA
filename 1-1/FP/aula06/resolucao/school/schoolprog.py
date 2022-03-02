# Complete o programa!

# a)
"""def loadFile(fname, lst):
    with open(fname, "r") as e:
        File = e.read().replace("\n", "\t")
        filetxt = File.split('\t')
        i = 1
        while (i < (len(filetxt)-1)//8):
            j = 0
            templst = []
            while (j < 8):
                N = i * 8 + j
                if (j > 4):
                    templst.append(float(filetxt[N]))
                else:
                    templst.append(filetxt[N])
                j += 1
            lst.append(tuple(templst))
            i += 1
    return"""

def loadFile(fname, lst):
    try:
        with open(fname, "r") as e:
            line = e.readline()
            for line in e:
                tmplst = line.strip().split('\t')
                tmplst[0] = int(tmplst[0])
                tmplst[-1] = float(tmplst[-1])
                tmplst[-2] = float(tmplst[-2])
                tmplst[-3] = float(tmplst[-3])
                lst.append(tuple(tmplst))                    
    except:
        print("O ficheiro não existe.")
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    j = 0
    templst = []
    print(reg)
    while j < 6:
        if j == 5:
            x = ((reg[j])+(reg[j+1])+(reg[j+2]))/3
            templst.append(x)
            j += 1
            continue
        templst.append(reg[j])
        j +=1
    return (templst)



# c) Crie a função printPauta aqui...
def printPauta(lst):
    messageform = "{:>5} {:^50} {:>5.1f}"
    print("{:29} {:27s} {:s}".format("Numero", "Nome", "Nota"))
    for i in lst:
        print(messageform.format(i[0], i[1], i[5]))
    return

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)

    # ordenar a lista
    FinalGradeLst = []
    for i in lst:
        FinalGradeLst.append(notaFinal(i))
    print(FinalGradeLst)
    FinalGradeLst.sort()
    
    # mostrar a pauta
    printPauta(FinalGradeLst)


# Call main function
if __name__ == "__main__":
    main()


