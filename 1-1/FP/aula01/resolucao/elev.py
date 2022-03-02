def main():
    Pisos = 4
    MoradoresPorPiso = 1
    MoradoresTotais = MoradoresPorPiso * Pisos
    AlturaDePisos = 3
    Vel = 1 #m/s

    DistanciaTotal = 365 * (AlturaDePisos * (2 * MoradoresTotais))
    HorasDeFuncionamento = (365 * ((AlturaDePisos * (2 * MoradoresTotais)) / Vel)) / 3600

    print("Distância total percorrida num ano: ", DistanciaTotal, "\nHoras de funcionamento num ano: ", HorasDeFuncionamento) 



if __name__ == "__main__":
    main()