# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, "r") as e:
        File = e.read().replace("\n", "\t")
        filetxt = File.split('\t')
        i = 1
        while (i < (len(filetxt)-1)//8):
            j = 0
            templst = []
            while (j < 8):
                N = i * 8 + j
                if (filetxt[N].isdigit() and j > 4):
                    templst.append(float(filetxt[N]))
                else:
                    templst.append(filetxt[N])
                j += 1
            lst.append(tuple(templst))
            i += 1
    return
# b) Crie a função notaFinal aqui...
def notaFinal(lst):
    i = 0
    finalLst = []
    while (i < (len(lst) - 1)):
        j = 0
        templst = []
        while j < 6:
            if j == 5:
                x = (float(lst[i][j])+float(lst[i][j+1])+float(lst[i][j+2]))/3
                templst.append(x)
                j += 1
                continue
            templst.append(lst[i][j])
            j +=1
        finalLst.append(tuple(templst))
        i += 1
    return (finalLst)



# c) Crie a função printPauta aqui...
def printPauta(lst, destination):
    messageform = "{:>5} {:^50} {:>5.1f}\n"
    with open(destination, "w") as fname:  
        fname.write("{:29} {:27s} {:s}\n".format("Numero", "Nome", "Nota"))
        for i in lst:
            fname.write(messageform.format(i[0], i[1], i[5]))
    return

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    FinalGradeLst = notaFinal(lst)
    # ordenar a lista

    FinalGradeLst.sort(key=lambda x:x[5], reverse=True)
    
    # mostrar a pauta
    printPauta(FinalGradeLst, "pauta.txt")

# Call main function
if __name__ == "__main__":
    main()


