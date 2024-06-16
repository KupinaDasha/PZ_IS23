# Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
# унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
# вычисления площади и периметра.

import math


class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Круг")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":

    circle = Circle("Красный", 5)

    area = circle.area()
    perimeter = circle.perimeter()

    print(f"Площадь: {area:.2f}")
    print(f"Периметр: {perimeter:.2f}")
