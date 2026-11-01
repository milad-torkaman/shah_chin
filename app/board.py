from app.Pieces import King, Queen, Rook, Bishop, Knight, Pawn
from app.utils import Color

class Board:
    def __init__(self):
        """ Inisial Board
        """
        self.team_black = [
            Rook   ( color=Color.BLACK, postion=(7, 0) ),
            Knight ( color=Color.BLACK, postion=(6, 0) ),
            Bishop ( color=Color.BLACK, postion=(5, 0) ),
            King   ( color=Color.BLACK, postion=(4, 0) ),
            Queen  ( color=Color.BLACK, postion=(3, 0) ),
            Bishop ( color=Color.BLACK, postion=(2, 0) ),
            Knight ( color=Color.BLACK, postion=(1, 0) ),
            Rook   ( color=Color.BLACK, postion=(0, 0) ),
        ].extend( [Pawn(color=Color.BLACK, postion= (x, 1)) for x in range(8)])
        self.team_white = [
            Rook   ( color=Color.WHITE, postion=(7, 0) ),
            Knight ( color=Color.WHITE, postion=(6, 0) ),
            Bishop ( color=Color.WHITE, postion=(5, 0) ),
            King   ( color=Color.WHITE, postion=(4, 0) ),
            Queen  ( color=Color.WHITE, postion=(3, 0) ),
            Bishop ( color=Color.WHITE, postion=(2, 0) ),
            Knight ( color=Color.WHITE, postion=(1, 0) ),
            Rook   ( color=Color.WHITE, postion=(0, 0) ),
        ].extend( [Pawn(color=Color.BLACK, postion= (x, 1)) for x in range(8)])

    def show(self):
        pass

    def __str__(self):
        return self.show()


if __name__ == "__main__":
    pass

    

    