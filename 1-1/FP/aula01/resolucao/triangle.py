import math;

def main():
    catetoA = int(input("Primeiro Cateto? "))
    catetoB = int(input("Segundo Cateto? "))

    hipotenusa = hipotenuse(catetoA, catetoB)
    angulo = angle(catetoA, hipotenusa)

    print("Hipotenusa: ", hipotenusa, "\nAngulo em graus:", angulo)

def hipotenuse(catetoA, catetoB):
    hipotenusa = math.sqrt((catetoA ** 2) + (catetoB ** 2))
    return hipotenusa

def angle(catetoA, hipotenusa):
    angulo = math.degrees(math.acos(catetoA / hipotenusa))
    return angulo


if __name__ == "__main__":
    main()