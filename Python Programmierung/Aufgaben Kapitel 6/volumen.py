import math
pi = math.pi

form = input('Form: Kubus, Zylinder oder Kegelstumpf: ')

if form == 'Ku' or form == 'Kubus':
    l = float(input('Länge in cm: '))
    b = float(input('Breite in cm: '))
    h = float(input('Höhe in cm: '))
    Volumen = l * b * h / 1000

elif form == 'Zy' or form == 'Zylinder':
    durchmesser = float(input('Durchmesser in cm: '))
    h = float(input('Höhe in cm: '))
    Volumen = pi * pow((durchmesser/2),2) * h / 1000

elif form == 'Ke' or form == 'Kegel' or form == 'Kegelstumpf':
    doben = float(input('Durchmesser oben in cm: '))
    dunten = float(input('Durchmesser unten in cm: '))
    h = float(input('Höhe in cm: '))
    Volumen = h * (pi/12) * (pow(doben,2) + doben * dunten +pow(dunten,2)) / 1000

else :
    print("Üngültige Eingabe!")
if Volumen != 0 :
    print('Volumen:', Volumen, 'Liter')


#Blumenerde berechnen
sack20 = 0
sack10 = 0
sack5 = 0
gesamtkosten = 0

if Volumen >= 20:
    sack20 += 1 
    Volumen -= 20

if Volumen >= 10 and Volumen < 20:
    sack10 += 1
    Volumen -= 10

if Volumen > 5 and Volumen <= 10 :
    Volumen -= 10
    sack10 += 1 

if Volumen <= 5:
        sack5 += 1 

print(sack5, "x 5 L Sack kosten:", sack5 * 5)
print(sack10, "x 10 L Sack kosten:", sack10 * 8)
print(sack20, "x 20 L Sack kosten:", sack20 * 14)

print ("Gesamtkosten = ", sack5 * 5 + sack10 * 8 + sack20 * 14)