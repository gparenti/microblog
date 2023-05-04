lohninput = float(input("lohninput:"))

zins10 = 10
zins5 = 5

grenze1 = 20000
grenze2 = 80000
grenze3 = 120000

if lohninput < grenze1:
    print("Abzug: 0 - Lohn unter 20'000")

if lohninput >= grenze1 and lohninput <= grenze2:
        abzug1 = (lohninput/100) * zins10
        print("Abzug:",abzug1)

elif lohninput > grenze3:
    lohninput = grenze3

if lohninput > grenze2:
    lohninputneu = lohninput - 80000
    abzug1 = (grenze2/100) * zins10
    print("Abzug1:",abzug1)

    abzug2 = (zins5/100) * lohninputneu
    print("Abzug2:",abzug2)

    output = abzug1 + abzug2
    print("Abzug:",output)