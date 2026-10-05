# #1. Написать функцию print_list_reverse(lst)
# Функция принимает список и выводит этот список в консоль в обратном порядке.
# Если lst равен None, пустой список, или если аргумент не является объектом типа list, функция должна вывести:
# Wrong list
# Пример:
# print_list_reverse([1, 2, 3, 4, 5])
# Вывод в консоль:
# [5, 4, 3, 2, 1]
# *************************************
print("Task1")
def print_list_reverse(lst):
    # print(type(lst))
    if lst is None or len(lst) == 0 or type(lst) != list:
        print("Wrong list")
    else:
        lst.reverse()
        print(lst)

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse("qrqr")
print_list_reverse([])
print_list_reverse(None)
print()
# 2. Написать функцию is_valid_point(point)
# Функция принимает кортеж и проверяет, является ли он корректной точкой на плоскости.
# Условия корректной точки:
#  • аргумент должен быть кортежем (tuple), а не списком или другим типом;
#  • кортеж состоит ровно из 2 элементов;
#  • оба элемента являются числами (int или float).
# Если кортеж соответствует всем условиям, функция возвращает True.
# Если аргумент не соответствует условиям, функция возвращает False.
# Если point равен None или является пустым кортежем, функция возвращает None.
# Примеры:
# is_valid_point((3, 5))      # True
# is_valid_point((3, "5"))    # False
# is_valid_point([3, 5])      # False
# is_valid_point((1, 2, 3))   # False
# is_valid_point(())          # None
# is_valid_point(None)        # None
# *************************************
print("Task2")
def is_valid_point(point):
    if point is None or not point:   #isEmpty() analogs => not point, len(point) == 0, point == ().
        return None
    elif type(point) != tuple or len(point) != 2 or not isinstance(point[0], (int, float)) or not isinstance(point[1], (int, float)):
        return False
    else:
        return True

print(is_valid_point((3, 5)),
      is_valid_point((3, "5")),
      is_valid_point([3, 5]),
      is_valid_point((1, 2, 3)),
      is_valid_point(()),
      is_valid_point(None), sep = "\n")
print()
# 3. Написать функцию print_sublist_reverse(lst, start, finish)
# Функция принимает список, стартовый индекс и финишный индекс.
# Нужно вывести в консоль список, в котором элементы от индекса start до индекса finish включительно расположены в обратном порядке, а остальные элементы остаются в обычном порядке.
# Пример:
# print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
# Исходный список:
# [10, 20, 30, 40, 50, 60]
# Часть списка от индекса 1 до индекса 3 включительно:
# [20, 30, 40]
# После реверса:
# [40, 30, 20]
# Вывод в консоль:
# [10, 40, 30, 20, 50, 60]
# Если lst равен None, пустой список, не является списком, если start / finish не являются целыми числами, если индексы start / finish выходят за пределы списка, или start > finish, функция должна вывести:
# Wrong args
# Пример:
# print_sublist_reverse([1, 2, 3], "0", 2)  # Wrong args (start не является целым числом)
# *************************************
print("Task3")
def print_sublist_reverse(lst, start, finish):
    if (lst is not lst
            or not isinstance(lst, list) #isinstance() catches both non-dicts and None, so "is None" chack is redundant
            # or not isinstance(start, int)  -> doesn't work with True False values! recognizes bool as int!!!
            # or not isinstance(finish, int)
            or type(start) is not int
            or type(finish) is not int
            or start not in range(0, len(lst))
            or finish not in range(0, len(lst))
            or start > finish):
        print ("Wrong args")
    else:
        sublist = lst[start:finish+1]
        sublist_reversed = sublist[::-1]
        print(lst[:start] + sublist_reversed + lst[finish+1:])
        # result = lst[:start]+lst[start:finish+1][::-1]+lst[finish+1:]
        # print(result)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
# [10, 40, 30, 20, 50, 60]
print_sublist_reverse([1, 2, 3], "0", 2)  # Wrong args (start не является целым числом)
print()
# 4. Advanced — Написать функцию get_students_by_grade(students)
# Функция принимает словарь, где ключ — имя студента, а значение — его оценка.
# Нужно вернуть новый словарь, где ключ — оценка, а значение — список имён студентов, получивших эту оценку.
# Пример:
# get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})
# Результат:
# {90: ["Alice", "Diana"], 85: ["Bob", "Charlie"]}
# Если students равен None, является пустым словарём или аргумент не является словарём, функция должна вернуть пустой словарь:
# {}
#
#
print("Task4")
def get_students_by_grade(students):
    if not isinstance(students, dict) or not students:  #isinstance() catches both non-dicts and None, so "is None" chack is redundant
        return {}
    else:
        result = {}
        for name, grade in students.items():
            # if grade not in result:
            #     result[grade] = []
            # result[grade].append(name)
            result.setdefault(grade, []).append(name)   #.setdefault() returns value by key. The .setdefault(key, default_value) method does two things in one: it looks up the key in the dictionary and, if it's not there, automatically creates it with the given value.
        return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
print(get_students_by_grade(None))
print(get_students_by_grade({}))
print(get_students_by_grade(["Alice", "Bob", "Charlie"]))
print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85, "Dave": 90, "Katherine": 90, "Elizabeth": 90, "Ian": 70, "Karoline": 70}))