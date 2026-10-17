# Регулярные выражения
# 1. Положительное число меньше 300
# Напишите функцию:
# def is_positive_less_than_300(value):
# Функция должна возвращать True, если строка содержит целое положительное число от 1 до 299.
# Подходят:
# 1
# 15
# 99
# 100
# 299
# Не подходят:
# 0
# 300
# -5
# 3.14
# Abc
import re

print("Task1")

def is_positive_less_than_300(value):
    return bool(re.fullmatch(r"[1-9]|[1-9]\d|[12]\d{2}",value))

print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("99"))
print(is_positive_less_than_300("100"))
print(is_positive_less_than_300("299"))
print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))
print(is_positive_less_than_300("3.14"))
print(is_positive_less_than_300("Abc"))
print()

#  2. Число от 1 до 255
# Напишите функцию: def is_number_from_1_to_255(value):
# Функция должна проверять целое число от 1 до 255 включительно.
# Подходят:
# 1
# 25
# 100
# 255
# Не подходят:
# 0
# 256
# 025
# -1
# 2.5
print("Task2")

def is_number_from_1_to_255(value):
    return bool(re.fullmatch(r"[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]",value))

print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("25"))
print(is_number_from_1_to_255("100"))
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("0"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("2.5"))
print()

# 3. Израильский мобильный номер
# Напишите функцию: def is_israel_mobile(phone):
# Допустимы номера:
# 0541234567
# 054-1234567
# +97254-123-4567
# 058-12-34-567
# Не подходят:
# 54-1234567
# 054--12-4567
# +972054-123-4567
# 97254-123-4567
print("Task3")

def is_israel_mobile(phone):
    return bool(re.fullmatch(r"(0|\+972)5\d(-?\d){7}", phone))
    # (?:) - non-capturing group. By adding ?: to the beginning of the brackets - (?:...) we disable the capturing of the data,
    # the engine uses the brackets only for logic and does not store the result in memory. This prevents memory leaks.
    # return bool(re.fullmatch(r"(?:0|\+972)5\d(?:-?\d){7}",phone))

print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))
print(is_israel_mobile("54-1234567"))
print(is_israel_mobile("054--12-4567"))
print(is_israel_mobile("+972054-123-4567"))
print(is_israel_mobile("97254-123-4567"))

print()

# 4. Проверка времени Напишите функцию: def is_valid_time(time):
# Формат времени: HH:MM (24 часа).
# Подходят:
# 00:00
# 09:30
# 14:45
# 23:59
# Не подходят:
# 24:00
# 12:60
# 8:30
# 123:45
# 12-30
print("Task4")

def is_valid_time(time):
    return bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d",time))

print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))
print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))
print()

# 5. Проверка автомобильного номера Израиля
# Напишите функцию:
# def is_israel_car_number(number):
# Поддержите два формата:
# 12-345-67
# 123-45-678
# Подходят:
# 12-345-67
# 99-999-99
# 123-45-678
# 456-78-901
# Не подходят:
# 12345678
# 12:345:67
# 1-234-56
# 1234-56-78
print("Task5")
def is_israel_car_number(number):
    return bool(re.fullmatch(r"\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3}",number))

print(is_israel_car_number("12-345-67"))
print(is_israel_car_number("99-999-99"))
print(is_israel_car_number("123-45-678"))
print(is_israel_car_number("456-78-901"))
print(is_israel_car_number("12345678"))
print(is_israel_car_number("12:345:67"))
print(is_israel_car_number("1-234-56"))
print(is_israel_car_number("1234-56-78"))


