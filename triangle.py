from shape import Shape
import math

class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        

    def get_area(self):
        # נוסחת הרון לחישוב שטח משולש בעזרת הצלעות
        # helf_primeter
        s = 0.5 * (self._side1 + self._side2 + self._side3)
        return math.sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3))
    
    def get_primeter(self):
        return self._side1 + self._side2 + self._side3
    
    def __str__(self):
        return f'Triangle -> Side 1: {self._side1}, Side 2: {self._side2}, Side 3: {self._side3}'
    