from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_primeter(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
    
    def __sub__(self, other):
        if isinstance(other, Shape):
            return self.get_area() - other.get_area()
        return NotImplemented

    def has_equal_area(self, other):
        return isinstance(other, Shape) and self.get_area() == other.get_area()
    
    def has_equal_primeter(self, other):
        return isinstance(other, Shape) and self.get_primeter() == other.get_primeter()
    
    
    
    

    
  
    

    