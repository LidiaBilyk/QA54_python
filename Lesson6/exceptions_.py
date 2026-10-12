# with open("user.json", "r", encoding="utf-8") as file:
#     print(file.read())

# print("Hello world")
# result = 10/0
# print(result)
# print("Bye world")

# def div_int(a, b):
#     return a/b
# print("start program")
# result = div_int(10, 0)
# print(result)

#try/except
# print("Hello world!")
# try:
#     result = 10/1
#     print(result)
# except Exception as e:
#     print("An error occurred: ", e)
# print("Bye")


# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print("Result:", result)
# except ValueError:
#     print("Error Please enter a valid number")
# except ZeroDivisionError:
#     print("Error: cannot divide by zero")



def is_number(text):
    try:
        float(text)
        return True
    except (TypeError,ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("qwe"))
print(is_number(None))


try:
    value = int("39")
except ValueError as e:
    print("An error occurred: ", e)
else:
    print("An error occurred: ", value)
finally:
    print("End of try")
