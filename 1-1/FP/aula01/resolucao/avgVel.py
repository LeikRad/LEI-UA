def main():
    v1 = float(input("Average Speed V1? "))
    v2 = float(input("Average Speed V2? "))
    v3 = (2*v1*v2)/(v1+v2)
    answertext = "The average speed of the whole trip is {}"
    print(answertext.format(v3))

if __name__ == "__main__":
    main()

