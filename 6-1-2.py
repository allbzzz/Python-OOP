"""
Попробуйте создать свой первый dataclass

Это будет простой класс Point, который должен хранить два целых атрибута x и y .

На основании класса Point создайте

 точку с координатами (5, 7) и сохраните ее в  переменную point1
точку с координатами (-10, 12) и сохраните ее в  переменную point2
Выведите сперва point1 потом на отдельной строке point2

"""


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point1 = Point(5, 7)
point2 = Point(-10, 12)
print(point1)
print(point2)
