# 1.Напишите три функции
# 1.1 save_test_ids(test_ids) — принимает список ID тестов и сохраняет их в tests.txt. Каждый ID должен находиться на отдельной строке.
# 1.2 add_test_id(test_id) — добавляет один новый ID в конец существующего файла, не удаляя предыдущие записи.
# 1.3 load_test_ids(filename) — читает файл и возвращает список ID. Пустые строки нужно пропускать, пробелы по краям удалять.
# Пример исходного списка->["QA-1001", "QA-1002", "QA-1003"]
# После вызова add_test_id("QA-1004") функция load_test_ids("tests.txt") должна вернуть:
# ["QA-1001", "QA-1002", "QA-1003", "QA-1004"]
# Используйте: def, return, for, list, append(), with open(), режимы w, a, r, strip().
# Проверьте пустой список, повторное добавление записи и чтение файла с пустыми строками.
import csv
import json
from pprint import pprint

print("Task1")
def save_test_ids(test_ids):
    with open('tests.txt', 'w', encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")

def add_test_id(test_id):
    with open('tests.txt', 'a', encoding="utf-8") as file:
        file.write(test_id + "\n")

def load_test_ids(filename):
    result = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            if line.strip():
                result.append(line.strip())
    return result

save_test_ids(["QA-1001", "QA-1002", "QA-1003"])
add_test_id("QA-1004")
print(load_test_ids("tests.txt"))
print()
# ["QA-1001", "QA-1002", "QA-1003", "QA-1004"]

# 2.Создайте файл results.csv test_id,status,duration_ms
# QA-1001,PASSED,120
# QA-1002,FAILED,230
# QA-1003,PASSED,150
# Напишите функцию get_test_statistics(filename)
#
# Функция должна:
# 1.Прочитать данные из CSV.
# 2.Посчитать общее количество тестов.
# 3.Посчитать количество PASSED и FAILED.
# 4.Найти суммарное время выполнения тестов в миллисекундах.
# 5.Собрать в список ID всех проваленных тестов.
# 6.Вернуть словарь с результатом
# Ожидаемый резальт->
# {
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500,
#     "failed_ids": ["QA-1002"]
# }
# Используйте: csv.DictReader(), for, if, dict, list, int(), append(), return.
# Считайте, что в корректном входном файле статусы могут быть только PASSED и FAILED, а время — целое неотрицательное число.
# Дополнительно проверьте файл, содержащий только заголовки. Все счётчики должны быть равны нулю, список ошибок — пустой.
print("Task2")
with open("results.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id","status", "duration_ms"])
    writer.writerow(["QA-1001","PASSED", 120])
    writer.writerow(["QA-1002","FAILED", 230])
    writer.writerow(["QA-1003","PASSED", 150])

def get_test_statistics(filename):
    result = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "total_duration_ms": 0,
        "failed_ids": []
    }
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row:
                result["total"] += 1
                result["total_duration_ms"] += int(row["duration_ms"])
                if row["status"] == "PASSED":
                    result["passed"] += 1
                if row["status"] == "FAILED":
                    result["failed"] += 1
                    result["failed_ids"].append(row["test_id"])
    # return result
    return json.dumps(result, indent=4)

print(get_test_statistics("results.csv"))
# pprint(get_test_statistics("results.csv"),sort_dicts=False)  #pprint!!!

# {
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500,
#     "failed_ids": ["QA-1002"]
# }
print()

# 3. Напишите две функции:
# save_test_config(environment, base_url, timeout) — создаёт config.json и сохраняет параметры тестового окружения.
# load_test_config(filename) — читает JSON и возвращает словарь с настройками.
# Пример вызова
# save_test_config(
#     "staging",
#     "https://example.com",
#     30
# )
# Ожидаемый JSON {
#     "environment": "staging",
#     "base_url": "https://example.com",
#     "timeout": 30
# }
# —-----------
# 1.Для сохранения используйте json.dump().
# 2.Для чтения используйте json.load().
# 3.Сохраняйте данные с отступами для удобного чтения.
# 4.Проверьте, что после загрузки тип timeout остаётся int.
# 5.Проверьте, что повторное сохранение заменяет старую конфигурацию.
#
# Используйте: dict, json.dump(), json.load(), with open(), type(), assert.
print("Task3")
def save_test_config(environment, base_url, timeout):
    configdata_json = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(configdata_json, file, indent=4, ensure_ascii=False)

def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        config = json.load(file)
        return json.dumps(config, indent=4)

save_test_config(
    "staging",
    "https://example.com",
    30
)
print(load_test_config("config.json"))
print()
# 4.Advanced
# Вы работаете QA Engineer. После запуска автоматизированных тестов необходимо создать отчёт для команды.
# Напишите функцию build_run_report(project_name, csv_filename)
# Функция получает название проекта и путь к CSV-файлу в формате из Task 2.
# Она должна
# 1.   Прочитать все результаты тестирования.
# 2.   Посчитать total, passed, failed, total_duration_ms.
# 3.   Создать папку reports.
# 4.   Внутри неё создать папку с названием проекта.
# 5.   Создать файл summary.json с общей статистикой.
# 6.   Создать файл failed_tests.txt, в который записать ID всех тестов со статусом FAILED.
# 7.   Вернуть словарь с итоговой статистикой.
#
# Пример
# build_run_report("Shop", "results.csv")
# reports/
#     Shop/
#         summary.json
#         failed_tests.txt
# Содержимое summary.json:
# {
#     "project": "Shop",
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500
# }
# Содержимое failed_tests.txt QA-1002
# Если папки ещё нет, она должна создаваться автоматически.
# •    Если папка уже существует, программа должна работать без ошибки.
# •    Если проваленных тестов нет, failed_tests.txt должен существовать, но оставаться пустым.
# •    При повторном запуске файлы должны обновляться, а не дублировать старые результаты.
#
# Используйте: pathlib.Path, mkdir(parents=True, exist_ok=True), csv.DictReader(), json.dump(), with open(), циклы, условия, списки и словари.
