from inputs import *

def f1():
    i = 0
    szoveg= ""
    while(i<=150):
        szoveg+=f"{i}, "
        i+=2
    return szoveg.rstrip(", ")

def index():
    print(inputTexts(0, 0))
    print(f1())


if __name__ == '__main__':
    index()