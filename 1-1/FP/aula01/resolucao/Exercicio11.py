from math import ceil

nome = input("Qual é o teu nome? ")
nome2 = input("Qual é o teu apelido? ")
salário = float(input("Quanto recebes de salário? "))
subsídio = float(input("Quanto recebes de subsídio? "))

salárioTotal = 12 * salário
subsídioTotal = 12 * subsídio
dinheiroTotal = salárioTotal + subsídio

message = """A/O {} {} recebe:
    {:.2f} euros de salário ao fim de 1 ano
    {:.2f} euros de subsídio de alimentação ao fim de 1 ano
    {:.2f} no total ao fim de 1 ano."""

print(message.format(nome, nome2, ceil(salárioTotal * 100) / 100, ceil(subsídioTotal * 100)/100, ceil(dinheiroTotal * 100)/100))