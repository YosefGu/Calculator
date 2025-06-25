from shape import Shape

class Rectangle(Shape):
     
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError('Length must be positive.')
        self._length = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Width must be positive.')
        self._width = value

    def get_area(self):
        return self._length * self._width
    
    def get_primeter(self):
        return (self._length + self._width) * 2
    
    def __str__(self):
        return f"Rectangle -> Length: {self._length}, Width: {self._width}"