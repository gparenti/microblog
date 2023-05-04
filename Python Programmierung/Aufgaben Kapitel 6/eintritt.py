normalpreis = 20
alter = float(input("Geben Sie ihr Alter an:"))

if alter <= 6 :
    print("Kinder bis 6 Jahren bezahlen keinen Eintritt")
if alter > 6 and alter <= 17 :
    normalpreis = normalpreis * 0.5
    print("Jugendliche bezahlen nur den halben Eintritt. Preis =",normalpreis)
if alter > 17 and alter < 65:
    print("Erwachsene bezahlen den vollen Eintritt. Preis:",normalpreis)
if alter >= 65:
    normalpreis = normalpreis * 0.75
    print("Retner bezahlen nur 75% des Eintritts", normalpreis)


normalpreis = 20
alter = float(input("Geben Sie ihr Alter an:"))

if alter <= 6 :
    ermässigung = 0
if alter > 6 and alter <= 17 :
    ermässigung = 0.5
if alter > 17 and alter < 65:
    ermässigung = 0
    if alter > 17 and alter < 41:
        antwort = input("Sind Sie Student? (J/N)")
        if antwort == 'J' or antwort 'j':
            student = True
            ermässigung2 = 0.25
if alter >= 65:
    ermässigung = 0.75
if (student == True):
    print ("Ihr Preis inkl. zusätzliche Rabatt:",normalpreis*ermässigung2)
else:
    print("Ihr Preis:", normalpreis * ermässigung)


normalpreis = 20
alter = float(input("Geben Sie ihr Alter an:"))

if alter <= 6 :
    ermässigung = 0
elif alter > 6 and alter <= 17 :
    ermässigung = 0.5
elif alter > 17 and alter < 65:
    ermässigung = 0
else:
    ermässigung = 0.75

print("Ihr Preis:", normalpreis * ermässigung)
