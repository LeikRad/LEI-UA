def main():
    usrinput = int(input("Tempo em segundos? "))

    s = usrinput % 60
    m = (usrinput // 60) % 60
    h = usrinput // 3600
    
    print("{:02d}:{:02d}:{:02d}".format(h, m, s))

if __name__ == "__main__":
    main()