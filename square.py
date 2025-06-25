from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, _side):
        super().__init__(_side, _side)

    @property
    def side(self):
        return self._length
    
    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side must be positive.")
        self._length = value
        self._width = value

    
    def __str__(self):
        return f"Squqre -> Side: {self._length}"