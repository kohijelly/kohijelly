
def gewinnprüfung(spielfeld, spieler):
    if (spielfeld[0] == spieler and spielfeld[1] == spieler and spielfeld[2] == spieler) or \
        (spielfeld[3] == spieler and spielfeld[4] == spieler and spielfeld[5] == spieler) or \
        (spielfeld[6] == spieler and spielfeld[7] == spieler and spielfeld[8] == spieler) or \
        (spielfeld[0] == spieler and spielfeld[3] == spieler and spielfeld[6] == spieler) or \
        (spielfeld[1] == spieler and spielfeld [4] == spieler and spielfeld[7] == spieler) or \
        (spielfeld[2] == spieler and spielfeld [5] == spieler and spielfeld[8] == spieler) or \
        (spielfeld[0] == spieler and spielfeld [4] == spieler and spielfeld[8] == spieler) or \
        (spielfeld[6] == spieler and spielfeld[4] == spieler and spielfeld[2] == spieler):
        return True
    else:
        return False   

def spielfeld_ausgeben(spielfeld):
    print(spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2])
    print("----------")
    print(spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5])
    print("----------")
    print(spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8])

def spieler_zug(spielfeld):
    gültige_eingabe = False
    while gültige_eingabe == False:
        feld = input("Spieler " +spieler+  ", auf welches Feld möchtest du setzen? ")
        if feld in spielfeld and feld != "x" and feld != "o":
            gültige_eingabe = True
        else:
            print(" Ungültige Eingabe, bitte nochmal!")
    return feld


def computer_zug(spielfeld):
    pass

# Begrüßung
print("Willkommen bei Tic Tac Toe!")

# Spielfeld anlegen
spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

spielfeld_ausgeben(spielfeld) 



spieler = "x"

for i in range(9):
   
    # Spieler 1 nach seinem Zug fragen
    feld = spieler_zug(spielfeld)


    # Zug durchführen 
    spielfeld[int(feld)-1] = spieler 

    spielfeld_ausgeben(spielfeld)

    # Prüfe, ob Spieler gewonnen hat
    if gewinnprüfung (spielfeld, spieler):
        print ("Glückwunsch " + spieler + ", du hast gewonnen!")        
        break

    if spieler == "x":
        spieler = "o"
    else:
        spieler = "x"



# wie nutzt Shein Informatik, um mit Mode erfolgreich zu sein, ohne sich mit Mode auszukennen
# decordin shein: The rise of china's newest retail decacorn 