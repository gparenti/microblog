zahl = 0
limit = 20


zaehlen_bis = int(input("Zählen bis:"))
while zahl < zaehlen_bis:   
    if zahl == limit:
        print("Beim Limit",limit, "ist Schluss")
        break
    print(zahl)
    zahl += 1
    
else:
    print("Limit", limit, "wurde nicht erreicht")