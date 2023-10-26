from inputs import *


def f2(x: int):
    return x % 10


def index():
    print(inputTexts(2, 0))
    try:
        while f2(int(input("Kérek egy egész számot: "))):
            print("Ez a szám nem osztató 10-zel.")
    except:
        print("HIBA: Ez nem egészszám.")


if __name__ == '__main__':
    index()