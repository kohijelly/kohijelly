import arcade

class TicTacToe(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)
    
        self.spieler = "x"

        self.spielfeld = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
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
        if self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5]: 
            return True 
        if self.spielfeld[8] == self.spielfeld[7] == self.spielfeld[6]:
            return True
        if self.spielfeld[2] == self.spielfeld[4] == self.spielfeld[6]:
            return True 
        if self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8]:
            return True
        

    def on_mouse_press(self, x, y, button, modifiers):
       
        feld=self.koordinaten_zu_feld(x, y)

        if self.spielfeld[feld-1] == feld: 
            self.spielfeld[feld-1] = self.spieler

        aufhängepunkt = self.feld_zu_mittelpunkt(feld)

        if self.spieler == "x":
            spielstein = arcade.Sprite ("picklrricks.jpeg")
            self.spieler = "o"
        else:
            spielstein = arcade.Sprite ("morty.png")
            self.spieler = "x"

        spielstein.position = aufhängepunkt
        self.spielstein_liste.append(spielstein)
        
    def on_draw (self):

        arcade.draw_lrwh_rectangle_textured(0, 0, 600, 600, arcade.load_texture("hintergrund.jpeg"))

        eckpunkte_liste=((20,200), (580, 200), (20,400), (580, 400), (200,20), (200,580), (400, 20), (400, 580))
        arcade.draw_lines(eckpunkte_liste,arcade.color.UFO_GREEN, 17 )

        self.spielstein_liste.draw()

        if self.gewinnprüfung() == True:
            arcade.draw_lrtb_rectangle_filled(0,600, 600,0, arcade.color.WINE_DREGS)
            arcade.draw_text (("pickelRick" if self.spieler == "o" else "Morty") + "hat gewonnen!", 300, 300, arcade.color.WHITE, 20, font_name="Kenney Blocks", anchor_x="center")
        


ttt = TicTacToe(600, 600,"Tic Tac Toe")
arcade.run()