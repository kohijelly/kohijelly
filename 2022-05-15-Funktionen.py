from urllib.parse import ParseResultBytes


def funktion1():
    print("Hallo!")
funktion1()

def funktion2(wort):
    print(wort)
funktion2("Hi!")
funktion2("Ciao!")

def funktion3(zahl):
    print(zahl * 2)
funktion3(5)

# Gibt "Positiv" aus, falls zahl größer 0 ist, und "Negativ", falls zahl kleiner 0 ist. Bei 0 tut sie nichts.
def funktion4(zahl):
    if zahl > 0:
        print("Positiv")
    if zahl < 0:
        print("Negativ")
funktion4(-1)
funktion4(0)
funktion4(1)

# Gibt "A" aus, falls wort mit dem Buchstaben A beginnt, ansonsten "Nicht A"
def funktion5(wort):
    if wort[0] == "A":
        print("A")
    else:
        print("Nicht A")
funktion5("Auto")
funktion5("Baum")

# Gibt die größere der beiden Zahlen aus (irgendeine, fall sie gleich groß sind)
def größere(zahl1, zahl2):
    if zahl1 > zahl2:
        print(zahl1)
    else:
        print(zahl2)

# Gibt die größte der drei Zahlen aus (irgendeine, fall alle gleich groß sind)
def größte(zahl1, zahl2, zahl3):
    if zahl1 >= zahl2 and zahl1 >= zahl3:
        print(zahl1)
    elif zahl2 >= zahl3 and zahl2 >= zahl1:
        print(zahl2)
    else:
        print(zahl3)
größte(2, 2, 1)

def summe(zahl1, zahl2):
    summe = zahl1 + zahl2
    print(summe)
summe(3, 5)

def summe2(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe
ergebnis = summe2(3, 5)
print(ergebnis)

# Kein + verwenden!
def summe3(zahl1, zahl2, zahl3):
    zwischenergebnis = summe2(zahl1, zahl2)
    endergebnis = summe2(zahl3, zwischenergebnis)
    return endergebnis
ergebnis = summe3(1, 2, 3)
print(ergebnis) # 6
ergebnis = summe3(2, 3, 4)
print(ergebnis) # 9

# Kein + oder * verwenden!
def mal(zahl1, zahl2):
    zwischenergebnis = 0
    for i in range(zahl1):
        zwischenergebnis = summe2(zwischenergebnis, zahl2)
    return zwischenergebnis
ergebnis = mal(2, 3) # 2 + 2 + 2 / 3 + 3
print(ergebnis) # 6

# Gibt den ersten Buchstaben von wort zurück
def erster(wort):
    ergebnis = wort[0]
    return ergebnis
ergebnis = erster("schiff")
print(ergebnis) # s

# Gibt die Länge von wort zurück
def länge(wort):
    ergebnis = len(wort)
    return ergebnis
ergebnis = länge("schiff")
print(ergebnis) # 6

# Gibt den letzten Buchstaben von wort zurück
def letzter(wort):
    letzte_position = länge(wort) - 1
    ergebnis = wort[letzte_position]
    return ergebnis
ergebnis = letzter("schiff")
print(ergebnis) # f

# Gibt den ersten gefolgt vom letzten Buchstaben von wort zurück (keine [] verwenden!)
def erster_und_letzter(wort):
    e = erster(wort)
    l = letzter(wort)
    return e + l
ergebnis = erster("schiff")
print(ergebnis) # sf

# Gibt das Quadrat von zahl zurück (kein * oder ** verwenden!)
def quadrat(zahl):
    zwischenergebnis = mal(zahl, zahl)
    return zwischenergebnis
ergebnis = quadrat(5)
print(ergebnis) # 25

# Gibt True zurück, falls der erste Buchstabe von wort1 gleich dem ersten Buchstaben von wort2 ist
def erster_gleich_erster(wort1, wort2):
    if wort1[0] == wort2[0]:
        return True
    else:
        return False
ergebnis = erster_gleich_erster("schiff", "seilbahn")
print(ergebnis) # True
ergebnis = erster_gleich_erster("schiff", "eisenbahn")
print(ergebnis) # False

# Gibt die Quadratwurzel von zahl zurück (abgerundet auf die nächste ganze Zahl)
def quadratwurzel(zahl):
    pass
ergebnis = quadratwurzel(25)
print(ergebnis) # 5

#TODO Auf 29. Mai: Cassie E-Mail auf dem Handy

# Gibt True zurück, falls der letzte Buchstabe von wort1 gleich dem letzten Buchstaben von wort2 ist
def letzter_gleich_letzter(wort1, wort2):
    wortlänge1 = len(wort1)
    wortlänge2 = len(wort2)
    if wort1[wortlänge1 - 1] == wort2[wortlänge2 - 1]:
        return True
    else:
        return False
ergebnis = letzter_gleich_letzter("statue", "zähne")
print(ergebnis) # True
ergebnis = letzter_gleich_letzter("wald", "wolke")
print(ergebnis) # False

# Gibt True zurück, falls der erste Buchstabe von wort1 gleich dem letzten Buchstaben von wort2 ist
def erster_gleich_letzter(wort1, wort2):
    wortlänge2 = len(wort2)
    if wort1[0] == wort2[wortlänge2 - 1]:
        return True
    else:
        return False
ergebnis = erster_gleich_letzter("frankfreich", "dorf")
print(ergebnis) # True
ergebnis = erster_gleich_letzter("kirche", "stadt")
print(ergebnis) # False

# Gibt True zurück, falls der letzte Buchstabe von wort1 gleich dem ersten Buchstaben von wort2 ist
def letzter_gleich_erster(wort1, wort2):
    pass
ergebnis = letzter_gleich_erster("spanien", "neandertaler")
print(ergebnis) # True
ergebnis = letzter_gleich_erster("atlantis", "abend")
print(ergebnis) # False

# Gibt True zurück, falls der erste Buchstabe von wort1 gleich dem letzten Buchstaben von wort2
# oder der letzte Buchstabe von wort1 gleich dem ersten Buchstaben von wort2 ist, ansonsten False
def oder(wort1, wort2):
    wortlänge2 = len(wort2)
    wortlänge1 = len(wort1)
    if wort1[0] == wort2[wortlänge2 - 1]:
        return True
    elif wort1[wortlänge1 - 1] == wort2[0]:
        return True
    else:
        return False
ergebnis = oder("london", "klasse")
print(ergebnis) # False
ergebnis = oder("hochhaus", "steinmauer")
print(ergebnis) # True
ergebnis = oder("flasche", "torf")
print(ergebnis) # True

# Gibt True zurück, falls wort1 und wort2 an der Stelle stelle den gleichen Buchstaben haben, ansonsten False
def stelle_gleich_stelle(wort1, wort2, stelle):
    if wort1[stelle] == wort2[stelle]:
        return True
    else:
        return False
ergebnis = stelle_gleich_stelle("lorbeeren", "serbien", 3)
print(ergebnis) # True
ergebnis = stelle_gleich_stelle("ägäis", "nilpferd", 1)
print(ergebnis) # False

# Gibt True zurück, falls in wort der Buchstabe buchstabe vorkommt, ansonsten False
# TODO Hausaufgabe auswendig lernen bis 10. juli 
def kommt_vor(wort, buchstabe):
    wortlänge = len(wort)
    for i in range(wortlänge):
        if wort[i] == buchstabe:
            return True
    return False
ergebnis = kommt_vor("freiburg", "g")
print(ergebnis) # True
ergebnis = kommt_vor("fensterscheibe", "e")
print(ergebnis) # True

# Gibt True zurück, falls in wort der Buchstabe buchstabe1 oder der Buchstabe buchstabe2 vorkommt, ansonsten False
def kommt_vor_2(wort, buchstabe1, buchstabe2):
    wortlänge = len(wort)
    for i in range(wortlänge):
        if wort[i] == buchstabe1 or wort[i] == buchstabe2:
            return True
    return False
ergebnis = kommt_vor_2("zentrum", "y", "z")
print(ergebnis) # True
ergebnis = kommt_vor_2("boje", "r", "i")
print(ergebnis) # False

# Gibt 1 zurück, falls in wort der Buchstabe buchstabe1 vorkommt und der Buchstabe buchstabe2 nicht
# Gibt 2 zurück, falls in wort der Buchstabe buchstabe2 vorkommt und der Buchstabe buchstabe1 nicht
# Gibt 3 zurück, falls in wort sowohl der Buchstabe buchstabe1 vorkommt als auch der Buchstabe buchstabe2
# Gibt 0 zurück, falls in wort weder der Buchstabe buchstabe1 vorkommt nocht der Buchstabe buchstabe2
def kommt_vor_3(wort, buchstabe1, buchstabe2):
    wortlänge = len(wort)
    buchstabe_kommt_vor = kommt_vor(wort, buchstabe1)
    buchstabe_kommt_vor1 = kommt_vor(wort, buchstabe2)
    if buchstabe_kommt_vor == True and buchstabe_kommt_vor1 == False:
        return 1
    if buchstabe_kommt_vor == False and buchstabe_kommt_vor1 == True:
        return 2
    if buchstabe_kommt_vor == True and buchstabe_kommt_vor1 == True:
        return 3
    if buchstabe_kommt_vor == False and buchstabe_kommt_vor1 == False:
        return 0
ergebnis = kommt_vor_3("gebirge", "e", "s")
print(ergebnis) # 1
ergebnis = kommt_vor_3("erhebung", "j", "h")
print(ergebnis) # 2
ergebnis = kommt_vor_3("tisch", "c", "s")
print(ergebnis) # 3
ergebnis = kommt_vor_3("nintendo", "u", "d")
print(ergebnis) # 0

#Gib die erste stelle zurück an der in wort der Buchstabe steht und -1, falls er garnicht vorkommt
def stelle(wort,buchstabe):
    wortlänge = len(wort)
    for i in range (wortlänge):  
        if wort[i] == buchstabe:
            return i
    return -1 

ergebnis = stelle( "microsoft", "r")
print(ergebnis) #3
ergebnis = stelle("python","z" )
print(ergebnis) #-1

# Gibt zurück, wie oft in wort der Buchstabe buchstabe vorkommt
def anzahl_buchstabe(wort, buchstabe):
    
    wortlänge = len(wort)
    zähler = 0
    for i in range(wortlänge):
        if wort [i] == buchstabe:
            zähler = zähler + 1
    return zähler
    
ergebnis = anzahl_buchstabe("ananas", "a")
print(ergebnis) # 3
ergebnis = anzahl_buchstabe("essen", "e")
print(ergebnis) # 2

# Gibt zurück, wie oft in wort1 und wort2 die gleichen Buchstaben an der gleichen Stelle stehen
def buchstaben_gleich(wort1, wort2):
    wortlänge = len(wort1)
    zähler = 0
    for i in range(wortlänge):
        if wort1[i] == wort2[i]:
            zähler = zähler + 1
    return zähler 
ergebnis = buchstaben_gleich("birnbaum", "barnabas")
print(ergebnis) # 3

def stelle_letzte(wort, buchstabe):
    wortlänge = len(wort)
    zähler = 0
    for i in range(wortlänge):
        if wort[i] == buchstabe:
            zähler = wortlänge - zähler - 2
            return zähler 
    return -1
ergebnis = stelle_letzte("eichelhäher", "e")
print (ergebnis) #9
ergebnis = stelle_letzte("fabrik", "e")
print (ergebnis) #-1

#Frag den Benutzer nach fünf Buchstaben und gibt das daraus zusammengesetzte Wort zurück.
def fünf_buchstaben():
    buchstabe1 = input("erster Buchstabe: ")
    buchstabe2 = input("zweiter Buchstabe: ")
    buchstabe3 = input("dritter Buchstabe: ")
    buchstabe4 = input("vierterBuchstabe: ")
    buchstabe5 = input("fünfter Buchstabe: ")
    
ergebnis = fünf_buchstaben()
print(ergebnis)

# Gibt True zurück, falls wort ein Palindrom ist, ansonsten False
def palindrom(wort):
    wortlaenge = len(wort)
    zaehler = 0
    for i in range(int(wortlaenge/2-1)):
        if wort[zaehler] != wort[wortlaenge - zaehler -1]:
            return False
        else:
            zaehler = zaehler + 1
    return True
ergebnis = palindrom("rentner")
print(ergebnis) # True
ergebnis = palindrom("lager")
print(ergebnis) # False