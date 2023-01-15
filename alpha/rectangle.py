
class Rectangle:
    def __init__(self, length:float, breadth:float) -> None:
        self.length = length
        self.breadth = breadth 

    def get_perimeter(self) -> float:
        return self.length * 2 + self.breadth * 2

    def get_area(self) -> float:
        return self.length * self.breadth