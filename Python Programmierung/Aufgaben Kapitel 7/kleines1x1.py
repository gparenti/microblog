eingabe = int(input("Geben Sie die Zahl ein: "))
zaehler = 1

if eingabe > 0:
    while True:
        print(zaehler, "x", eingabe, "=",zaehler * eingabe)
        zaehler += 1
        if zaehler == 11:
            break
else:
    print("Geben Sie eine Zahl grösser 0 ein")