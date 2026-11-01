from .piece import Piece

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