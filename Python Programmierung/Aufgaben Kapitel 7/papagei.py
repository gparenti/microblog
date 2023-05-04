eingabe = None

while True:
    eingabe = input("Erhäl mir was: ")
    print(eingabe)
    if eingabe == 'Ende' or eingabe == 'Schluss':
        print("War schön mit Dir zu reden!")
        break