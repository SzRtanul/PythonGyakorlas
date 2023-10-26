def inputTexts(x: int, y: int):
    return [
        ["1. Írjuk ki 0-tól 150-ig a páros számokat!"],
        ["2. Számold meg 10 bekért szám esetében a 3-mal osztható számokat!"],
        ["3. Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*"],
        ["4. Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*"],
        ["5. Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*"],
        ["6. Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*"],
        ["7. Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk! "],
        ["8. Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*"],
        ["9. Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*"],
        ["10. Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!"],
        ["11. A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!"]
    ][x][y]
