from enum import Enum


class Borad:
    def __init__(self):
        

    def show(self):
        board = self.board
        req = ''

        for row in board:
            for column in row:
                req += f"{column}"
            req += '\n'
        return req

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


class King(Piece):
    def __init__(self,
                 *,
                 color: Color,
                 postion = (0, 0)):
        super().__init__(
            color = color,
            postion=postion
        )

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
        self.double_move = True
        
    @property
    def actions(self):
        res = [
            (0, 1, 1)
        ]

        if self.double_move:
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
    

    