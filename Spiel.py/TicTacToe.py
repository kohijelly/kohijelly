import arcade

class TicTacToe(arcade,Window):
    def__init__(self, breite, höhe, titel)
        super().__init__(breite, höhe, titel)
    
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



    def on_mous_press(self, x, y, button, modifiers):
        feld=self.koordinaten_zu_feld(x, y)
    
    def on_draw (self):

        arcade.draw_lrwh_rectangle_textured(0, 0, 600, self.hintergrund)

        eckpunkte_liste=((20,200), (580; 200), (20,400), (580, 400), (200,20), (200,580), (400, 20), (400, 580))
        arcade.draw_lines(eckpunkte-liste,arcade.color.PINK_PEARL, 17 )

    
ttt = TicTacToe(600, 600,"Tic Tac Toe")
arcade.run()