from square import Square
from triangle import Triangle
from rightTriangle import Right_trinagle
from circle import Circle
from hexagon import Hexagon



def main():
    square1 = Square(3)
    square2 = Square(3)
    square3 = square1
    triangle1 = Triangle(6, 3, 7)
    right_triangle = Right_trinagle(3, 3)
    circle = Circle(6)
    hexagon = Hexagon(4)
    print(square1 == square2)
    print(square1.has_equal_area(square2))
    print(square1 - square3)
    print(square1 - triangle1)
    print(right_triangle)
    print(circle.has_equal_area(right_triangle))
    print(hexagon.has_equal_primeter(circle))


if __name__ == "__main__":
    main()    



