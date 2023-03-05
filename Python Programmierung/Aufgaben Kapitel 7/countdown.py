zahl = int(input("Geben Sie ein, wo der countdown beginnen soll: "))

if zahl > 0:
    while zahl > 0:
        print(zahl)
        zahl -=1
    print("Am Endi vo de Schleife gibi das us!")
else:
    print("Falscher Input! Zahl muss grösser 0 sein")