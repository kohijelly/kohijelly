# Spielfeld anlegen
spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Spielfeld ausgeben 
print(spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2])
print("----------")
print(spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5])
print("----------")
print(spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8])
  
runde = 0

spieler = "x"

while runde < 9:

    runde = runde +1

    # Spieler ein Feld wählen lassen
    feld = input("Welches Feld möchtest du wählen? ")
    while spielfeld[int(feld) - 1] != feld:
        feld = input("Ungültige Eingabe, bitte noch einma: ")
    spielfeld[int(feld) - 1] = spieler
  
    

    # Spielfeld ausgeben 
    print(spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2])
    print("----------")
    print(spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5])
    print("----------")
    print(spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8])

    # Prüfen, ob der Spieler gewonnen hat
    if (spielfeld[0] == spieler and spielfeld[1] == spieler and spielfeld[2] == spieler) or \
        (spielfeld[3] == spieler and spielfeld[4] == spieler and spielfeld[5] == spieler) or \
        (spielfeld[6] == spieler and spielfeld[7] == spieler and spielfeld[8] == spieler) or \
        (spielfeld[0] == spieler and spielfeld[3] == spieler and spielfeld[6] == spieler) or \
        (spielfeld[1] == spieler and spielfeld [4] == spieler and spielfeld[7] == spieler) or \
        (spielfeld[2] == spieler and spielfeld [5] == spieler and spielfeld[8] == spieler) or \
        (spielfeld[0] == spieler and spielfeld [4] == spieler and spielfeld[8] == spieler) or \
        (spielfeld[6] == spieler and spielfeld[4] == spieler and spielfeld[2] == spieler):
            print("Glückwunsch" + spieler + ", du hast gewonnen!")
            break
    if spieler == "x":
        spieler = "o"
    else: 
        spieler = "x"

