def is_int(string: str) -> bool :
    """Prüft, ob ein String in einen int-Wert umgewandelt werden kann.
    Falls ja, gibt die Funktion True zurück"""
    try:
        zahl = int(string)
        return True
    except ValueError:
        return False


# Aufgabe 5
def read_int(prompt: str) -> int :
    """Fordert solange zur Eingabe einer ganzen Zahl auf, bis eine eingegeben wurde.
    Ist die Eingabe nicht in int umwandelbar, wird eine Fehlermeldung ausgegeben"""
    string = input(prompt)
    while is_int(string) == False :
        string = input(prompt)
    ausgabe = int(string)
    return ausgabe