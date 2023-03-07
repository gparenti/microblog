eingabe= int(input("Zahl: "))
zahl = 1
zaehler = 1

while zaehler <= eingabe:
    zahl = zahl * zaehler
    zaehler +=1

print(eingabe,"! =",zahl)