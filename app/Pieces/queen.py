from .piece import Piece
from app.utils.color import Color

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

