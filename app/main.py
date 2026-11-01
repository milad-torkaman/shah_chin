from enum import Enum

class Borad:
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

    def show(self):
        pass

    def __str__(self):
        return self.show()

class Color(Enum):
    BLACK = "Black"
    WHITE = "White"

class Piece:
    def __init__(self,
                 *,
                 color: Color,
                 postion = (0, 0),
                ):
        self.color = color
        self.postion = postion

    def set_postion(self, x, y):
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.postion = (x, y)
            return True, self.postion
        else:
            return False, self.postion

    def __str__(self):
        return self.symbol

class King(Piece):
    def __init__(self,
                 *,
                 color: Color,
                 postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )
        self.point = -1

        self.actions = self.attacks = (
            (-1, 1, 1), (0, 1, 1), (1, 1, 1),
            (-1, 0, 1), (1, 0, 1),
            (-1, -1, 1), (0, -1, 1), (1, -1, 1)
        )

    @property
    def symbol(self):
        return '♚' if self.color == Color.BLACK else '♔'

class Queen(Piece):
    def __init__(self,
                *,
                color: Color,
                postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )
        self.point = 9

        self.actions = self.attacks = (
            (-1, 1, -1), (0, 1, -1), (1, 1, -1),
            (-1, 0, -1), (1, 0, -1),
            (-1, -1, -1), (0, -1, -1), (1, -1, -1)
        )

    @property
    def symbol(self):
        return '♛' if self.color == Color.BLACK else '♕'

class Bishop(Piece):
    def __init__(self,
                *,
                color: Color,
                postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )
        self.point = 3

        self.actions = self.attacks = (
            (-1, 1, -1), (1, 1, -1),
            (-1, -1, -1), (1, -1, -1)
        )

    @property
    def symbol(self):
        return '♝' if self.color == Color.BLACK else '♗'

class Rook(Piece):
    def __init__(self,
                *,
                color: Color,
                postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )
        self.point = 5

        self.actions = self.attacks = [
            (0, 1, -1),
            (-1, 0, -1), (1, 0, -1),
            (0, -1, -1)
        ]

    @property
    def symbol(self):
        return '♜' if self.color == Color.BLACK else '♖'

class Knight(Piece):
    def __init__(self,
                *,
                color: Color,
                postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )
        self.point = 3

        self.actions = self.attacks = [
            (2, -1, 1), (2, 1, 1),
            (-2, -1, 1), (-2, 1, 1),
            (-1, 2, 1), (1, 2, 1),
            (-1, -2, 1), (1, -2, 1)
        ]

    @property
    def symbol(self):
        return '♞' if self.color == Color.BLACK else '♘'

class Pawn(Piece):
    def __init__(self,
                *,
                color: Color,
                postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )
        self.point = 1
        
    @property
    def actions(self):
        res = [
            (0, 1, 1)
        ]

        if self.postion[1] == 1:
            res.append( (0, 2, 1) )

        return tuple(res)

    @property
    def attacks(self):
        return (
        (-1, 1, 1), (1, 1, 1)
    )

    @property
    def symbol(self):
        return '♟' if self.color == Color.BLACK else '♙'

if __name__ == "__main__":
    pass
    pawn = Pawn(color=Color.BLACK, postion=(0, 2))
    print(str(pawn))
    

    