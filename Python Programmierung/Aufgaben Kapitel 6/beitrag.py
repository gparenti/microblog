zahl = int(input("Zahl:"))
zins1 = 10
zins2 = 5

if zahl < 20000:
    print("Abzug: 0")
elif zahl >= 20000 and zahl <= 120000:
    if zahl > 20000 and zahl <= 80000:
        abzug = (zins1/100) * zahl
        print("Abzug:",abzug)
    elif zahl > 80000:
        abzug = (zins2/100) * zahl
        print("Abzug:",abzug)
else:
    print("Kein Abzug")