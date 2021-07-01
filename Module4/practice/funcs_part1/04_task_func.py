# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками
import math


def distance(p1, p2):
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))


def can_triangle(p1, p2, p3):
    # TODO: your code here
    if distance(p1, p2)+distance(p1, p3) > distance(p2, p3) or distance(p1, p3)+distance(p2, p3) > distance(p1, p2) or distance(p2, p3)+distance(p1, p2) > distance(p1, p3):
        return True
    return False
    pass


# Пример вызова функции
if can_triangle((10, 12), (14, 18), (12, 12)):
    print("Yes")
else:
    print("No")

# Не забудьте протестировать вашу функцию
