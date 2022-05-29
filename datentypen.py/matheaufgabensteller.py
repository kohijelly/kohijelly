import random 
import time

# Willkommenheißung
rundenzahl = input("Willkommen zum Matheaufgabensteller. wie viele Runden willst du spielen?: ")
runde = 0
punkte = 0

while runde < int(rundenzahl):

    runde = runde + 1

    rechenzeichen = random.choice(["+", "-", "*", "/"])

    if rechenzeichen == "+":
        zahl = random.randint(0, 100)
        zahl1 = random.randint(0, 100 - zahl)
    if rechenzeichen == "-":
        zahl = random.randint(0, 100)
        zahl1 = random.randint(0, zahl)
    if rechenzeichen == "*":
        zahl = random.randint(0, 10)
        zahl1 = random.randint(0, 10)
    if rechenzeichen == "/":
        zahl = random.randint(0, 10)
        zahl1 = random.randint(0, 10)
        rechnung = zahl * zahl1
        zahl = rechnung

    # Was ist das Ergebnis dieser Aufgabe?
    startzeit = time.time()
    ergebnis_str = input(str(zahl) + " " + rechenzeichen + " " + str(zahl1) + " = ")
    endzeit = time.time()

    ergebnis = int(ergebnis_str)

    rechenzeit = round(endzeit - startzeit, 1)

    richtig = False

    # Ergebnis prüfen
    if rechenzeichen == "+":
        if ergebnis == zahl + zahl1:
            print ("richtig :), du hast " + str(rechenzeit) + " sec. gebraucht!")
            richtig = True
        else:
            print("Falsch :( , prüfe mit einem Taschenrechner nach!")
    if rechenzeichen == "-":
        if ergebnis == zahl - zahl1:
            print ("richtig :), du hast " + str(rechenzeit) + " sec. gebraucht!")
            richtig = True
        else:
            print ("Falsch :( , prüfe mit einem Taschenrechner nach!")
        
    if rechenzeichen == "*":
        if ergebnis == zahl * zahl1:
            print ("richtig :), du hast " + str(rechenzeit) + " sec. gebraucht!")
            richtig = True
        else:
            print("Falsch :( , prüfe mit einem Taschenrechner nach!")
    if rechenzeichen == "/":
        if ergebnis == zahl / zahl1:
            print ("richtig :), du hast " + str(rechenzeit) + " sec. gebraucht!")
            richtig = True
        else:
            print("Falsch :( , prüfe mit einem Taschenrechner nach!")

    if richtig == True:
        if rechenzeit < 1: 
            print("+5P")
            punkte = punkte + 5
        elif rechenzeit < 3:
            print("+4P")
            punkte = punkte +4
        elif rechenzeit < 5:
            print("+3P")
            punkte = punkte + 3
        elif rechenzeit < 10:
            print("+2P")
            punkte = punkte + 2
        else:
            print("+1P")
            punkte = punkte +1


print("Du hast " + str(punkte) + "P erreicht!")