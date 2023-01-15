from rectangle import *


def test_rectangle_has_length_and_breath():
    rectangle = Rectangle(2.0, 3.0)
    assert rectangle.length != None
    assert rectangle.breadth != None

def test_get_perimeter_calculates_correct_perimeter():
    rectangle = Rectangle(2.0, 3.0)
    assert rectangle.get_perimeter() == 10.0

def test_get_area_calculates_correct_area():
    rectangle = Rectangle(2.0, 3.0)
    assert rectangle.get_area() == 6.0