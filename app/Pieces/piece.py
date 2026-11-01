from app.utils.color import Color

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