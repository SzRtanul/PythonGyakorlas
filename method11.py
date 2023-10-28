from inputs import *
import method10

def index():
    print(inputTexts(10, 0))
    arr = []
    x = 1
    i = 0
    while (x != 0):
        try:
            x = float(input(f"Kérem a(z) {i + 1}. számot, ami 0-tól eltér: "))
            if x > 0:
                arr.append(x)
            elif x == 0:
                pass
            else:
                print("Csak pozitív szám elfogadott: ")
            i += 0
        except:
            print("HIBA: Ez nem szám!")
    print(f"A számok átlaga: {method10.f10(arr)}")


if __name__ == '__main__':
    index()