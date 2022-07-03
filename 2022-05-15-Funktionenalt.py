from contextlib import nullcontext
import random


def funktion1():
    print("hallo!")
funktion1()

def funktion2(wort):
    print(wort)
funktion2("hi")
funktion2("ciao!")

def funktion3(zahl):
    print(zahl * 2)
funktion3(5)

#Gibt Positiv aus, falls zahl groesser 0 ist, und Negativ, falls zahl kleiner 0 ist. bei  0 tut sie nichts.
def funktion4(zahl):
    zahl = random.randint(-10,10)
    if zahl < 0:
        print("Negativ")
    if zahl > 0:
        print("Positiv")

#Gibt A aus, falls wort mit dem Buchstaben A beginnt, annsomsten nicht A.
def funktion5(wort):
    if wort[0] == "A":
        print("A")
    else:
        print("Nicht A")
funktion5("Auto")
funktion5("Baum")

def groessere(zahl1,zahl2):
    
    if zahl1 > zahl2 :
        print(zahl1)
    else:
        print(zahl2)

def groesste (zahl1,zahl2,zahl3):
    if zahl1 >= zahl2 and zahl1 >= zahl3:
        print(zahl1)
    elif zahl2 >= zahl1 and zahl2 >= zahl3:
        print(zahl2)
    else:
        print(zahl3)

def summe2 (zahl1, zahl2):
    summe = zahl1 + zahl2 
    return summe
ergebnis = summe2(3, 5)
print(ergebnis)

def summe3(zahl1, zahl2, zahl3):
    zwischenergebnis = summe2(zahl1, zahl2)
    endergebnis = summe2 (zahl3, zwischenergebnis)

    return ergebnis
ergebnis = summe3(1, 2, 3)
print(ergebnis )

def mal (zahl1, zahl2):
    zwischenergebnis = 0 
    for i in range(zahl1):
        zwischenergebnis = summe2(zwischenergebnis, zahl2)
    
    return zwischenergebnis
ergebnis = mal (2, 3)
print (ergebnis)

def erster(wort):
     
   ergebnis = wort[0] 
   return ergebnis
ergebnis = erster("schiff")
print(ergebnis)

def laenge(wort):
    ergebnis = len(wort)
    return ergebnis
ergebnis = laenge("schiff")
print(ergebnis)



def letzter(wort):
    letzte_position = laenge(wort) - 1
    ergebnis = wort[letzte_position]
    return ergebnis
ergebnis = letzter("schiff")
print(ergebnis)

def erster_und_letzter(wort):
    e = erster(wort)
    l = letzter(wort)
    return e + l
ergebnis = erster("schiff")
print (ergebnis)



def quadrat(zahl):
    zwischenergebnis = mal(zahl, zahl)
    return zwischenergebnis
ergebnis = quadrat(5)
print (ergebnis)



def erster_gleich_erster(wort1, wort2):
    if wort1[0] == wort2[0]:
        return True
    else:
        return False
ergebnis = erster_gleich_erster("schiff", "seilbahn")
print(ergebnis) #True
ergebnis = erster_gleich_erster("schiff", "eisenbahn")

def letzter_gleich_letzter(wort1, wort2):
    wortlaenge1 = len(wort1)
    wortlaenge2 = len(wort2)
    if wort1[wortlaenge1 - 1] == wort2[wortlaenge2 - 1]:
        return True
    else:
        return False
ergebnis = letzter_gleich_letzter("statue", "zaehne")
print(ergebnis)#True
ergebnis = letzter_gleich_letzter("wolke", "wald")
print(ergebnis)#False

def letzter_gleich_erster(wort1, wort2):
    wortlaenge1 = len (wort1)
    if wort1[wortlaenge1-1] == wort2[0]:
        return True 
    else:
        return False       
ergebnis = letzter_gleich_erster("spanien", "neandertaler")
print(ergebnis)#True
ergebnis = letzter_gleich_erster("atlantis", "abend")
print(ergebnis)#False

def erster_gleich_letzter(wort1, wort2):
    wortlaenge2 = len(wort2)
    if wort1[0] == wort2[wortlaenge2-1]:
        return True 
    else:
        return False       
ergebnis = letzter_gleich_erster("frankreich", "dorf")
print(ergebnis)#True
ergebnis = letzter_gleich_erster("kirche", "stadt")
print(ergebnis)#False

def oder(wort1, wort2):
    wortlaenge1 = len(wort1)
    wortlaenge2 = len(wort2)
    if wort1[0] == wort2[wortlaenge2-1] or wort1[wortlaenge1-1] == wort2[0]:
        return True 
    else:
        return False 
ergebnis = oder ("london", "klasse")
print(ergebnis)#False
ergebnis = oder("hochhaus", "steinmauer")
print(ergebnis)#False
ergebnis = oder("flasche", "torf")
print(ergebnis)#True

def stelle_gleich_stelle(wort1, wort2, stelle):
    if wort1[stelle] == wort2[stelle]:
        return True
    else:
        return False
ergebnis = stelle_gleich_stelle("lorbeeren", "serbien", 3)
print(ergebnis)#True
ergebnis = stelle_gleich_stelle("aegaeis", "nilpferd", 1)
print(ergebnis)#flasche

def kommt_vor(wort, buchstabe):
    wortlaenge = len(wort)
    
    #if buchstabe in wort:
    #   return True
    #else:
    #   return False    
    for i in range(wortlaenge):
        if wort[i] == buchstabe: 
            return True
        
    return False
ergebnis = kommt_vor("freiburg", "g")
print(ergebnis) 
ergebnis = kommt_vor("fensterscheibe", "e")
print(ergebnis) 

def anzahl_buchstaben(wort, buchstaben):
    pass
ergebnis = anzahl_buchstaben("ananas","a")
print(ergebnis)#3
ergebnis = kommt_vor("essen","e")
print(ergebnis)#2

def buchstabe_gleich(wort1, wort2):
    pass
ergebnis = buchstabe_gleich("birnbaum", "barnabas")
print(ergebnis)#3

def palindrom(wort):
    #wortlaenge = len(wort)
    #zaehler = 0
    #for i in range(int(wortlaenge/2-1)):
    #    if wort[zaehler] != wort[wortlaenge - zaehler -1]:
    #        return False
    #    else:
    #        zaehler = zaehler + 1
    #return True
    reverse = wort[::-1]
    if reverse.lower() == wort.lower():
        return True
    else:
        return False
ergebnis = palindrom("rentner")
print(ergebnis)#True
ergebnis = palindrom("Lagerregal")
print(ergebnis)#True
ergebnis = palindrom("lager")
print(ergebnis)#False