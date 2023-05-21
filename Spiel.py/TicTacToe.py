import arcade

class TicTacToe(arcade,Window):
    def__init__(self, breite, höhe, titel)
        super()._init_(breite, höhe, titel)
    
    def on_draw (self):

        arcade.draw_lrwh_rectangle_textured(0, 0, 600, self.hintergrund)

        eckpunkte_liste=((20,200), (580; 200), (20,400), (580, 400), (200,20), (200,580), (400, 20), (400, 580))
        arcade.draw_lines(eckpunkte-liste,arcade.color.PINK_PEARL, 17 )

    
ttt = TicTacToe(600, 600,"Tic Tac Toe")
arcade.run()