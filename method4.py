from inputs import *

def f3(x: int):
    return len(str(x)) == 2 and x % 2

def index():
    print(inputTexts(3, 0))
    try:
        while not f3(int(input("Kérek egy egész számot: "))):
            print("Ez a szám nem kétjegyű és páratlan.")
    except:
        print("HIBA: Ez nem egészszám.")


if __name__ == '__main__':
    index()