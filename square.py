from shape import Shape

class Square(Shape):

    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side
    
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
        return f"Square -> Side: {self._side}"
    
    def __add__(self, other: Shape):
        return Square(self._side + other._side)
    
    def __repr__(self):
        return f"Square({self._side})"