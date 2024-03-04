prozent = 8
ende = "o"

while True:
    if ende == "x":  # wenn die x-Taste gedrückt wird, beenden Sie die Schleife
        break
    kapital = int(input("Geben Sie das Startkapital ein: "))
    jahre = int(input("Geben Sie die Laufzeit in Jahren ein: "))
    endkapital = kapital * (1 + prozent / 100) ** jahre
    endkapital = round(endkapital, 2)
    print("Endkapital:", endkapital)
    for i in range(1, jahre + 1):
        print("Jahr", i, ":", round(kapital * (1 + prozent / 100) ** i))
    ende = input("Beenden? (x)")
