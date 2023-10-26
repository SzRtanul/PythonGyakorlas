from inputs import *

def f8(x):
    return len(x) == 3

def index():
    print(inputTexts(7, 0))
    try:
        x = ""
        while not f8(x):
            x = input("Kérek egy 3 betűs szöveget: ")
        print(f"A szöveg nagy betűkkel: {x.upper()}")
    except:
        print("HIBA: Ez nem egészszám.")

if __name__ == '__main__':
    index()