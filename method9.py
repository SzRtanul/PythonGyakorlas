from inputs import *

def f8(x):
    return len(x) == 4 and x.islower()

def index():
    print(inputTexts(8, 0))
    try:
        x = ""
        while not f8(x):
            x = input("Kérek egy 4 karakterhosszú kisbetűs szöveget: ")
        print(f"Siker!")
    except:
        print("HIBA: Ez nem egészszám.")

if __name__ == '__main__':
    index()