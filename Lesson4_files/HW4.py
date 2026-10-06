# #1. Save a book list
# Напишите функцию save_books(books).
# Функция принимает список строк и создаёт файл books.txt, в который сохраняет названия книг.
# Каждая книга должна быть записана с новой строки.
# Пример:
# books = [
#  	"Harry Potter",
#  	"The Hobbit",
#  	"1984",
#  	"The Little Prince"
#  ]
#
#  save_books(books)
# После выполнения программы файл books.txt должен выглядеть так:
# Harry Potter
#  The Hobbit
#  1984
#  The Little Prince
# Используйте:
# ·       with open(...)
# ·       режим "w"
# ·       цикл for
import csv
import json
import os
from pathlib import Path

print("Task1")
def save_books(books):
    with open("books.csv", "w", encoding="utf-8") as file:
        for e in books:
            file.write(e+"\n")

books = [
    "Harry Potter",
    "The Hobbit",
    "1984",
    "The Little Prince"
 ]
save_books(books)
# Harry Potter
#  The Hobbit
#  1984
#  The Little Prince
print()

# 2. Read data from a CSV file
# Создайте файл products.csv со следующим содержимым:
# product,price
#  Coffee,25
#  Tea,18
#  Chocolate,12
# Напишите функцию:
# read_products(filename)
# Функция должна прочитать данные из файла и вывести информацию в следующем формате:
# Product: Coffee (25)
#  Product: Tea (18)
#  Product: Chocolate (12)
# Используйте:
# csv.DictReader()
print("Task2")

with open("products.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["product","price"])
    writer.writerow(["Coffee","25"])
    writer.writerow(["Tea","18"])
    writer.writerow(["Chocolate","12"])


def read_products(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Product: {row["product"]} ({row["price"]})")

read_products("products.csv")

# Product: Coffee (25)
#  Product: Tea (18)
#  Product: Chocolate (12)
print()

# 3. Save user information to a JSON file
# Напишите функцию:
# save_user(username, email, country)
# Функция должна создать файл user.json и сохранить в него информацию о пользователе.
# Пример вызова:
# save_user("anna21", "anna@example.com", "Israel")
# Ожидаемое содержимое файла user.json:
# {
#  	"username": "anna21",
#  	"email": "anna@example.com",
#  	"country": "Israel"
#  }
# Используйте:
# ·       словарь dict
# ·       json.dump()
print("Task3")

def save_user(username, email, country):
    field_names = "username", "email", "country"
    field_values = username, email, country
    json_data = {name:value for name, value in zip(field_names, field_values)}
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, skipkeys=True)

save_user("anna21", "anna@example.com", "Israel")
# {
#  	"username": "anna21",
#  	"email": "anna@example.com",
#  	"country": "Israel"
#  }
print()

# 4. Advanced ★
# Напишите функцию:
# create_logs_folder()
# Функция должна:
# 1.     Создать папку logs.
# 2.     Создать внутри неё файл app.txt.
# 3.     Записать в файл строку:
# Application started successfully!
# Используйте:
# ·       pathlib.Path
# ·       mkdir()
# ·       with open(...)
print("Task4")
def create_logs_folder():
    # parents=True - for intermediate directories. The flag tells pathlib to create the whole chain in one operation (Path('path/to/dir').mkdir(parents=True, exist_ok=True))
    # exist_ok=True - Without it, mkdir on a path that's already a directory raises FileExistsError. The flag makes the call idempotent.
    #The file-in-the-way trap: exist_ok=True only suppresses the error when a DIRECTORY already exists at the target path.
    # If a regular file sits there, FileExistsError still fires. This is correct behavior;
    # mkdir can't replace a file with a directory, and silencing this case would mask real bugs.
    Path("logs").mkdir(parents=True, exist_ok=True)
    with open("logs/app.txt", "w", encoding="utf-8") as file:  # if (directory is local(in the script area)): use relative path, else: absolute path
        file.write("Application started successfully!")

create_logs_folder()

# General Requirements
# ·       Используйте encoding='utf-8' при работе с текстовыми файлами.
# ·       Проверьте работу каждой функции на примерах из задания.
# ·       Используйте названия функций, указанные в задании.
# ·       Код должен быть читаемым и аккуратно оформленным.
# ·       После выполнения программы проверьте содержимое созданных файлов.
#
# #