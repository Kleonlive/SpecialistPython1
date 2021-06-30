# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

my_list = []

list_sum = 0

for el in my_list:
    if el > 0:
        list_sum = list_sum + el

print(list_sum)
