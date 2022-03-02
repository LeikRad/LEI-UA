import datetime

def main():
    nome = input("Como te chamas? ")
    ano1 = int(input("Em que ano nasceste? ")) #ano1 é o ano de nascença
    ano2 = datetime.datetime.now().year #ano2 é este ano
    anos = ano2 - ano1 + 1
    print(nome+ ", em "+ str(ano2) + " farás "+ str(anos)+ " anos.")


if __name__ == "__main__":
    main()
