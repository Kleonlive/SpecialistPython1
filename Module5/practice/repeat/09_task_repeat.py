# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: [“ананас”, “кокос”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к” больше.
# Дано: [“ананас”, “яблоко”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к”и “а” больше.

test = ["ананас", "кокос", "Арбуз", "киви", "Клюква", "банан", "хурма"]


def check_max_f_letter_word(names):
    lower_f_letter = []
    count_letters = []
    letter = ""
    max_count = 0
    for name in names:
        lower_f_letter.append(name[0].lower())
    for f_letter in lower_f_letter:
        cnt = lower_f_letter.count(f_letter)
        count_letters.append([f_letter, cnt])
    for cur_letter in count_letters:
        if cur_letter[1] > max_count:
            max_count = cur_letter[1]
            letter = cur_letter[0]
    return letter


print(check_max_f_letter_word(test))
