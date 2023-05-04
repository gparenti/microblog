Kanfang = float(input("Anfangsbetrag eintippen: "))
Z = float(input("Zinssatz in % eintippen: "))
Jahre = float(input("Anzahl Jahre : "))
Jahreverlauf = 1

while Jahreverlauf <= Jahre:
    Kende=Kanfang * (pow((1+Z/100),Jahreverlauf))
    print("Kapital nach {} Jahr: {}".format(Jahreverlauf,Kende))
    Jahreverlauf += 1