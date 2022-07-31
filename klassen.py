class Tier:
    def_init_(self, tierart, tierklasse, gewicht, körperhöhe, körperlänge, ernährungsweise, farbe, männlich, flugfähig, alter)
        self.tierart = tierart
        self.tierklasse = tierklasse
        self.gewicht = gewicht 
        self.körperhöhe = körperhöhe
        self.ernährungsweise = ernährungsweise
        self.farbe = farbe 
        self.männlich = männlich
        self.flugfähig = flugfähig
        self.alter = alter

    def_str_(self):
        return "Tier | Tierart" + self.tierart + "Gewicht: " + str(self.gewicht) + "kg, Alter: " + str(self.alter) + "Jahre"

    def geburtstag(self):
       self.alter = self.alter + 1

# Gewicht nimmt um 10% zu
    def füttern(self):
        self.gewicht = self.gewicht + self.gewicht/10
# Gewicht nimmt um 25% des beutetieres zu
    def fressen(self,beutetier):
        self.gewicht = self.gewicht + beutetier.gewicht/4

tier1 = Tier("Katze","Wirbeltier", 5, 25, 60, " Allesfreser", "grau", False, False, 2)
tier2 = Tier("Elefant", "Wirbeltier", 5000, 300, 500, "Pflanzenfresser", "grau", True, False, 9)
tier3 = Tier("Lachs", "Fisch", 2, 20, 45, "Fleischfresser, "blau-grau", False, False, 3)
tier4 = Tier("Taube", "Vogel", 1, 15, 25, "Allesfresser", "grau", True, True, 1)
tier5 = Tier("Schnabeltier", "Wirbeltier", 15, 35, 90, "Allesfresser", "braun", True, False, 5)

print(tier1.alter)
tier1.geburtstag()
print(tier1.alter)

print(tier4.gewicht)
tier4.füttern()
print(tier1.gewicht)

print(tier1.gewicht)
tier1.fressen(tier4)
print(tier1.gewicht)


class Zoo:
    def_init_(self, fläche, tierbestand, eintrittspreis, name, adresse, öffnungszeiten):
        self.fläche = fläche
        self.tierbestand = tierbestand
        self.eintrittspreis = eintrittspreis
        self.name = name 
        self.adresse = adresse
        self.öffnungszeit = öffnungszeit


    def_str_(self):
        return"Zoo | Name: " + self.name + ", Adresse: " + self.adresse + ", Eintrittspreis: " + str(self.eintrittspreis) + "€"

    def anzahl_tiere(self):
        anzahl = len(self.tiere):
        return anzahl

    def tier_aufnahmen(self, tier):
        self.tierbestand .append(tier)

zoo1 = Zoo("30 Hektar", [tier1, tier2, tier3, tier4, tier5], 20.0, "Wilhelma", "Wilhelma 13, 70376 stuttgart", "08:15 - 20:00 Uhr")

print (zoo1)
