import arcade

class TicTacToe(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)
    
        self.spieler = 1

    
        self.spielstein_liste = arcade.SpriteList ()

    def koordinaten_zu_feld(self, x, y):
        if x < 200 and y > 400:
            return 1 
        if x < 400 and y > 400:
            return 2
        if x < 600 and y > 400:
            return 3
        if x < 200 and 200 < y < 400:
            return 4
        if 200 < x < 400 and 200 < y < 400:
            return 5 
        if x > 400 and 200 < y < 400:
            return 6
        if x < 200 and y < 200:
            return 7
        if 200 < x < 400 and y < 200:
            return 8 
        if x > 400 and y < 200:
            return 9

    def feld_zu_mittelpunkt(self, feld):
        zeile = (feld-1)//3
        spalte =(feld-1)%3
        x = 100 + spalte * 200
        y = 500 - zeile * 200
        return (x, y)
    
    def gewinnprüfung(self):
        if self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2]:
            return True
        if self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2]: 
        

    def on_mous_press(self, x, y, button, modifiers):
        feld=self.koordinaten_zu_feld(x, y)

        if self.spielfeld[feld-1] == feld: 
            self.spielfeld[feld-1] = self.spieler

        aufhängepunkt = self.feld_zu_mittelpunkt(feld)

        if self.spieler == 1:
            spielstein = arcade.Sprite ("rick.png")
            self.spieler = 2
        else:
            spielstein = arcade.Sprite("morty.png")
            self.spieler = 1

        spielstein.position = aufhängepunkt
        self.spielstein_liste.append(spielstein)
    
    def on_draw (self):

        arcade.draw_lrwh_rectangle_textured(0, 0, 600, 600, arcade.load_texture("hintergrund.jpeg"))

        eckpunkte_liste=((20,200), (580, 200), (20,400), (580, 400), (200,20), (200,580), (400, 20), (400, 580))
        arcade.draw_lines(eckpunkte_liste,arcade.color.UFO_GREEN, 17 )

        self.spielstein_liste.draw

    
ttt = TicTacToe(600, 600,"Tic Tac Toe")
arcade.run()