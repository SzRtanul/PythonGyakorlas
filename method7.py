from inputs import *

def f7(x: int, y: int, z: int):
    return max(x, y, z) * -1 + x + y + z > 0

def index():
    print(inputTexts(6, 0))
    try:
        while not f7(int(input("Kérem az 1/3 számot: ")), int(input("Kérem a 2/3 számot: ")), int(input("Kérem a 3/3 számot: "))):
            print("Ebből a 3 oldalból nem szerkeszthető háromszög.")
    except:
        print("HIBA: Ez nem egészszám.")


if __name__ == '__main__':
    index()