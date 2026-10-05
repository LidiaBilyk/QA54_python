import csv

with open("user_scv.csv", "w", encoding="utf-8",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "email", "role"])
    writer.writerow(["Lidia", "q@g.com", "admin"])
    writer.writerow(["Hermes", "w@g.com", "master"])
    writer.writerow(["Zephyr", "e@g.com", "baton"])

with open("user_scv.csv") as file:
    reader = csv.reader(file)
    print(type(reader))
    for row in reader:
        print(row)

#email = row[1]
with open("user_scv.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["name"], "-", row["role"])


