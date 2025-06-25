import math
from shape import Shape

class Hexagon(Shape):

    def __init__(self, side):
        self._side = side

    def get_area(self):
        return 0.5 * (3 * math.sqrt(3) * self._side**2)
    
    def get_primeter(self):
        return self._side * 6
    
    def __str__(self):
        return f'Hexagon -> Side: {self._side}'
