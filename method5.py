from inputs import *



def f4(x: int):
    return x >= 0 and x % 2 == 1

def index():
    print(inputTexts(4, 0))
    try:
        while not f4(int(input("Kérek egy egész számot: "))):
            print("Ez a szám nem pozitív és páratlan")
    except:
        print("HIBA: Ez nem egészszám.")


if __name__ == '__main__':
    index()