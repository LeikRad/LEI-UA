def main():
    answer = "Chega ás {} horas e {} minutos."
    horaInicial = 6
    minInicial = 52
    ritmo1 = 10 # mins por km
    ritmo2 = 6 # mins por km

    TempoDeDemora = (1 * ritmo1) + (3 * ritmo2) + (4 * ritmo1) #mins
    minFinal = minInicial + TempoDeDemora

    horaFinal = horaInicial

    while(minFinal >= 60):
        horaFinal = horaFinal + 1
        minFinal = minFinal - 60

    print(answer.format(horaFinal, minFinal))


if __name__ == "__main__":
    main()