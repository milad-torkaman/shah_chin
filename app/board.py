from app.Pieces import King, Queen, Rook, Bishop, Knight, Pawn
from app.utils.color import Color

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
        ]
        # add pawn 8 column (in row 7)
        self.team_black.extend( [Pawn(color=Color.BLACK, postion= (x, 1)) for x in range(8)])

        self.team_white = [
            Rook   ( color=Color.WHITE, postion=(7, 0) ),
            Knight ( color=Color.WHITE, postion=(6, 0) ),
            Bishop ( color=Color.WHITE, postion=(5, 0) ),
            King   ( color=Color.WHITE, postion=(4, 0) ),
            Queen  ( color=Color.WHITE, postion=(3, 0) ),
            Bishop ( color=Color.WHITE, postion=(2, 0) ),
            Knight ( color=Color.WHITE, postion=(1, 0) ),
            Rook   ( color=Color.WHITE, postion=(0, 0) ),
        ]
        # add pawn 8 column (in row 7)
        self.team_white.extend( [Pawn(color=Color.WHITE, postion= (x, 1)) for x in range(8)])

    def get_piece_by_position(self, x:int, y:int):
        target_postion = (x, y)
        for piece in self.team_white:
            if piece.postion == target_postion:
                return piece

        for piece in self.team_black:
            if (7 - piece.postion[0], 7 - piece.postion[1]) == target_postion:
                return piece
        return None

    def show(self, postion:Color = Color.WHITE):
        my_range = [8] if Color.WHITE else [7, -1, -1]
        res = '\n'
        for y in range(*my_range):
            line = ''
            for x in range(*my_range):
                piece = self.get_piece_by_position(x, y)
                line += f" {piece.symbol} " if piece else ' ■ '
            res += line.rjust(40, ' ')
            res += '\n'
        return res

    def __str__(self):
        return self.show()



    