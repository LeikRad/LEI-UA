# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    dic = {}
    for i in contacts:
        if partName.lower() in contacts[i].lower():
            dic[i] = contacts[i]
    return dic

def addContacts(dic, name, numb): 
    dic[numb] = name

def remContact(dic, numb):
    if numb not in dic:
        print("O número que deseja remover não está nos seus contactos.")
    else:
        dic.pop(numb)

def searchContacts(dic, numb):
    if numb in dic:
        name = dic.get(numb)
    else:
        name = numb
    return name

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""
    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }
    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            name = input("Nome do novo contacto? ")
            while True:
                numero = input("Número do novo contacto? ")
                if (len(numero) == 9):
                    break
                print("O número introduzido tem que ter 9 digitos. Introduza outra vez.")
            addContacts(contactos, name, numero) #     dic[numb] = name
        elif op == "R":
            while True:
                numero = input("Número do contacto que quer remover? ")
                if (len(numero) == 9):
                    break
                print("O número introduzido tem que ter 9 digitos. Introduza outra vez.")
            remContact(contactos, numero)
        elif op == "N":
            while True:
                numero = input("Número do contacto que quer procurar? ")
                if (len(numero) == 9):
                    break
                print("O número introduzido tem que ter 9 digitos. Introduza outra vez.")
            print(searchContacts(contactos, numero))
        elif op == "P":
            name = input("Nome do contacto que quer procurar? ")
            print(filterPartName(contactos, name))
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

