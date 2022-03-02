def main():
    PF = 20
    PC = 24.95
    IMP = 0.23
    SPA = 0.20

    Lucro = 500 * (((PC - SPA) / (1 + IMP)) - PF)
    Impostos = ((PC-SPA) * IMP) * 500
    Taxas = Impostos + (SPA * 500) #Pergunta não clarifica o que quer

    print("Lucro: ", Lucro, "\nImpostos: ", Impostos, "\nTaxa: ", Taxas)

if __name__ == "__main__":
    main()