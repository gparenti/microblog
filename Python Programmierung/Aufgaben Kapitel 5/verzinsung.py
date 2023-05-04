Kanfang = float(input("Anfangsbetrag eintippen: "))
Z = float(input("Zinssatz in % eintippen: "))
Jahre = float(input("Anzahl Jahre : "))
Kende=Kanfang * (pow((1+Z/100),Jahre))

print("Kapital nach {} Jahren: {}".format(Jahre,Kende))