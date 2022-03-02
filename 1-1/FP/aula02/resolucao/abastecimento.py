def main():
    abastecimento()

def abastecimento():
    litros = float(input("O número de litros é: "))
    preco = float
    if (litros > 40.0):
        preco = litros * 1.40 * 0.9
    else:
        preco = litros * 1.40
    print("{:.2f}".format(preco), "Euros")

if __name__ == "__main__":
    main()
