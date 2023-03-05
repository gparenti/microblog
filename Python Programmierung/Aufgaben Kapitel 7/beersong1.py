print("Der Kühlschrank ist leer")
bierflaschen = int(input("Wie viele Flaschen Bier kaufen? "))
vorrat = 0

while bierflaschen > vorrat:
    if bierflaschen == 1:
        print(bierflaschen, "Flasche Bier im Kühlschrank")
        print(bierflaschen, "Flasche Bier")
        print("Nimm eine raus")
        print("Trink sie aus")
        print("Der Kühlschrank ist leer")
        break

    else:
        print(bierflaschen, "Flaschen Bier im Kühlschrank")
        print(bierflaschen, "Flaschen Bier")
        print("Nimm eine raus")
        print("Trink sie aus")
        bierflaschen -= 1

else:
    print("Die Eingabe muss grösser 0 sein")
