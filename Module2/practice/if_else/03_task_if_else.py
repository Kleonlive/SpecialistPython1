# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here

side_a = float(input("Введите сторону стороны a:"))
side_b = float(input("Введите сторону стороны b:"))
side_c = float(input("Введите сторону стороны c:"))

if side_a == side_b or side_a == side_c or side_b == side_c:
    print("YES")
else:
    print("NO")
