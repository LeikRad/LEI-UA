import time

def main():
    n = int(input("Tempo? "))
    countdown(n)

def countdown(n):
    assert n > 0
    while(n >= 0):
        print(n, "segundos restantes")
        n -= 1
        time.sleep(1)

if __name__ == "__main__":
    main()