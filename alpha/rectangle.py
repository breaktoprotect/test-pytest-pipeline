
class Rectangle:
    def __init__(self, length:float, breadth:float) -> None:
        self.length = length
        self.breadth = breadth 

    def get_perimeter(self) -> float:
        return self.length * 2 + self.breadth * 2

    def get_area(self) -> float:
        return self.length * self.breadth

    def get_length(self) -> float:
        return self.length

    def get_breadth(self) -> float:
        return self.breadth

    def set_length(self, length) -> bool:
        self.length = length
        return True

    def set_breadth(self, breadth) -> bool:
        self.breadth = breadth
        return True