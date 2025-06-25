from shape import Shape

class Square(Shape):

    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._length
    
    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side must be positive.")
        self._side = value

    def get_area(self):
        return self._side * self._side
    
    def get_primeter(self):
        return self._side * 4
    
    def __str__(self):
        return f"Squqre -> Side: {self._length}"