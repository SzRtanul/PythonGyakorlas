from inputs import *

def f1(x: int):
    return x % 3 == 0

def index():
    print(inputTexts(1, 0))
    array = []
    i = 0
    while i < 10:
        try:
            array.append(int(input(f"Kérem a(z) {i+1}/10 számot: ")))
            i += 1
        except:
            print("HIBA: Ez nem egészszám.")
    i=0
    ossz = 0
    while(i< len(array)):
        if f1(array[i]):
            ossz+=1
        i += 1
    print(f"A 3-mal osztható számok száma: {ossz}")




if __name__ == '__main__':
    index()