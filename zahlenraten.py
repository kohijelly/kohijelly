import random

# Spieler nach seinem Namen fragen und diesen in einer Variablen speichern
name = input("Bitte Namen eingeben: ")


# Spieler begrüßen
print("Hallo " + name + ", herzlich willkommen beim Zahlenraten!")

# Eine zufällige Zahl auswählen und in einer Variablen speichern

zahl = random.randint(1,10)

gefunden = False 
versuch = 0 

while gefunden == False:
    # versuchzähler erhöhen
    versuch = versuch + 1 


    # Spieler nach seiner Zahl fragen und diese in einer Variable speichern
    eingabe_str = input("Versuch" + str(versuch) + " Wie lautet deine Zahl?: ") 
    eingabe = int(eingabe_str)


    #Prüfe, ob die Eingabe gleich der Zahl ist und das Ergebnis ausgeben
    if eingabe == zahl:
        print("Du hast die Zahl gefunden!")
        gefunden = True
    if eingabe < zahl:
        print ("Zu klein!")
    if eingabe > zahl:
        print("Zu groß!")    

