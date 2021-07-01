# Напишите функцию находящую n-ое число Фибоначчи.

def fibo(n):
    num = 1
    buffer_num = 0
    prev_num = 0
    i = 1
    while i < (n - 1):
        buffer_num = num
        num = num + prev_num
        prev_num = buffer_num
        i += 1
    return num

print(fibo(20))
