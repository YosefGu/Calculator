import math
from triangle import Triangle

class Right_trinagle(Triangle):

    def __init__(self, side1, side2):
        _side3 = math.sqrt(side1**2 + side2**2)
        super().__init__(side1, side2, _side3)

    def __str__(self):
        return f"Right Triangle -> Side 1: {self._side1}, Side 2: {self._side2}, Hypotenuse: {self._side3}"
    
    def __repr__(self):
        return f'Right Triengle({self._side1}, {self._side2})'