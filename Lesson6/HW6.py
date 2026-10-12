# 1. Напишите функцию:
# get_product(products, index)
# Функция должна возвращать товар из списка по переданному индексу.
# Если такого индекса нет, вернуть:
# Product index is out of range
# Примеры:
# products = ["coffee", "tea", "milk"]
# print(get_product(products, 0))
# # coffee
# print(get_product(products, 7))
# # Product index is out of range
# Обработайте IndexError.
print("Task1")
def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"

products = ["coffee", "tea", "milk"]

print(get_product(products, 0))
print(get_product(products, 7))
# coffee
# Product index is out of range
print()

# 2. Напишите функцию:
# get_settings_value(settings, key)
# Функция должна возвращать значение из словаря по ключу.
# Если ключ отсутствует, вернуть:
# Setting was not found
# Примеры:
# settings = {
# "language": "English",
# "theme": "dark"
# }
# print(get_settings_value(settings, "theme"))
# # dark
# print(get_settings_value(settings, "font"))
# # Setting was not found
# Обработайте KeyError.
print("Task2")
def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:  #IRL try/except is rarely used for dicts, instead, use the built-in dictionary func .get(key, default_value)
        return "Setting was not found"
    # return settings.get(key, "Setting was not found")

settings = {
"language": "English",
"theme": "dark"
}

print(get_settings_value(settings, "theme"))
print(get_settings_value(settings, "font"))
# dark
# Setting was not found

print()

# 3. Напишите функцию:
# calculate_total_price(price, quantity)
# Функция получает два значения, преобразует их в числа и возвращает результат умножения.
# Обработайте отдельно:
# ValueError, если значение невозможно преобразовать в число.
# TypeError, если передан неподходящий тип данных.
# Примеры:
# print(calculate_total_price("12.5", "4"))
# # 50.0
# print(calculate_total_price("coffee", "4"))
# # Value must be a number
# print(calculate_total_price(None, 4))
# # Invalid data type
# Не используйте один общий except Exception.
print("Task3")

def calculate_total_price(price, quantity):
    try:
        return float(price) * float(quantity)
    except TypeError:
        return "Invalid data type"
    except ValueError:
        return "Value must be a number"

print(calculate_total_price("12.5", "4"))
print(calculate_total_price("coffee", "4"))
print(calculate_total_price(None, 4))
# 50.0
# Value must be a number
# Invalid data type
print()

# 4. Напишите функцию:
# def read_temperature():
# Функция должна:
# Запросить у пользователя температуру с помощью input().
# Преобразовать значение в float.
# Если преобразование прошло успешно, вывести:
# Temperature was entered successfully
# Если пользователь ввёл неправильное значение, вывести:
# Invalid temperature
# Независимо от результата всегда вывести:
# Program finished
print("Task4")

def read_temperature():
    try:
        temperature = float(input("Enter a temperature: "))
        print("Temperature was entered successfully")
    except ValueError:    # TypeError is redundant - input() -> str, float(str) may cause ValueError but not TypeError
        print("Invalid temperature")
    finally:
        print("Program finished")

read_temperature()
print()

# 5. Напишите функцию:
# def validate_discount(discount):
# Требования:
# если скидка меньше 0, выбросить:
# ValueError("Discount cannot be negative")
# если скидка больше 100, выбросить:
# ValueError("Discount cannot be greater than 100")
print("Task5")

def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")

validate_discount(5)