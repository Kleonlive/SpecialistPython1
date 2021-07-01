# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 1
b = 122
cn = 0


def palindrome(number):
    return str(number) == str(number)[::-1]


for el in range(a,b):
    if palindrome(el):
        cn += 1

print(cn)
