""" Für die Lohnabzüge für eine Sozialversicherung sollen die folgenden Regeln gelten:
Der Beitrag ist erst auf Jahreslöhne ab 20'000.- zu entrichten
Der Beitrag wird vom Lohn nur bis zu einer Höhe von 120'000.- abgezogen.
Lohnanteile über dieser Summe sind beitragsfrei.
Für Löhne über 20'000 und bis zu 80'000.- gilt der Beitragssatz 10%
Für Lohnanteile über 80.000.- un bis zu 120.000 gilt der Beitragssatz 5%
"""
# Alle Variablen in diesem Programm werden zunächst inialisiert
beitrag_grenze1 = 80000
prozentsatz1 = 10.0
beitrag1 = 0
beitrag_grenze2 = 120000
prozentsatz2 = 5.0
beitrag2 = 0
beitrag_gesamt = 0

brutto_lohn = float(input("Bruttolohn: "))

# Es wird nur der Bruttolohn bis zur beitrag_grenze2 berechnet
if brutto_lohn > beitrag_grenze2 :
    brutto_lohn = beitrag_grenze2

# Nur die Löhne über 20000 sind beitragspflichtig
# bis beitrag_grenze1 gilt prozentsatz1
if brutto_lohn >= 20000 :
    beitrag1 = beitrag_grenze1 * prozentsatz1 / 100
# Lohnanteile über beitrag_grenze1 werden mit prozentsatz2 abgezogen
if brutto_lohn > beitrag_grenze1 :
    beitrag2 = (brutto_lohn - beitrag_grenze1) * prozentsatz2 / 100

beitrag_gesamt = beitrag1 + beitrag2
print( 'Abzug: ', beitrag_gesamt )