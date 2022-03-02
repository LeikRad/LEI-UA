def main():
    text_answer = "{} ºC = {} ºF"
    usr_input = input("Temperature in Celsius? ")
    temp_C = float(usr_input)
    temp_F = 1.8 * temp_C + 32
    print(text_answer.format(temp_C, temp_F))

if __name__ == "__main__":
    main()

