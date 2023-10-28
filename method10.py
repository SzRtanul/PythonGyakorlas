from inputs import *

def f10(arr: []):
    atl = 0
    i = 0
    while (i < len(arr)):
        atl += arr[i]
        i += 1
    return atl / i

def index():
    print(inputTexts(9, 0))
    arr = []
    x = 1
    i = 0
    while(x != 0):
        try:
            x = float(input(f"Kérem a(z) {i+1}. számot, ami 0-tól eltér: "))
            if x != 0:
                arr.append(x)
            i += 0
        except:
            print("HIBA: Ez nem szám!")
    print(f"A számok átlaga: {f10(arr)}")


if __name__ == '__main__':
    index()
