from .piece import Piece

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
