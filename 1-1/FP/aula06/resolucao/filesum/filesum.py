from tkinter import filedialog
from tkinter.constants import X

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    name = input("File? ")                                  #A
    #name = filedialog.askopenfilename(title="Choose File") #B
    if not ".txt" in name:
        name = name + ".txt"

    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    File = open(filename, "r").read()
    lst = File.split()
    i = 0
    for x in lst:
        i = i + float(x)
    return(i)

if __name__ == "__main__":
    main()

