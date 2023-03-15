
ende = ['Ende','ENDE','ende','End','end']
liste = []

while True:
    eingabe = input("Geben Sie einen Namen ein. Abschluss mit ENDE: ")
    if eingabe not in ende:
        liste.append(eingabe)
    else:
        break
liste.sort()
print(liste)