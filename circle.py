
from shape import Shape
import math

class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    def get_area(self):
        return math.pi * self._radius**2
    
    def get_primeter(self):
        return math.pi * self._radius * 2
    
    def __str__(self):
        return f"Circle -> Radius: {self._radius}"