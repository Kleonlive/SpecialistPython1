# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here

my_list = []

while first_number < second_number:
    first_number += 1
    if first_number % 3 == 0:
        my_list.append(first_number)

print(my_list)
