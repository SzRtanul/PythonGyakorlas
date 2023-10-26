from inputs import *

def f6(x: float):
    return x % 3 == 0 or x**1/2 % 1 == 0


def index():
    print(inputTexts(5, 0))
    try:
        while not f6(float(input("Kérek egy egész számot: "))):
            print("Ez a szám nem is osztató 3-mal és nem is négyzetszám.")
    except:
        print("HIBA: Ez nem szám.")


if __name__ == '__main__':
    index()