# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def sec_to_time(sec):
    c_sec = sec % 60
    c_min = (sec // 60) % 60
    c_hour = (sec // 60) // 60
    c_time = f"{c_hour:0>2}:{c_min:0>2}:{c_sec:0>2}"
    return c_time

print(sec_to_time(29143))
