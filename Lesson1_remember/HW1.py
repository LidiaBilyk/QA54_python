# #HOMEWORK — STRING METHODS REFRESH
#
# Python Review • Strings

# Task 1. Clean a Name #
# Write a function clean_name(name). #
# Remove spaces from the beginning and end of the string. #
# Return the name in title case.
#
# Example: #
# print(clean_name("   anna smith   "))
# # Anna Smith
#
# print(clean_name("DAVID COHEN"))
# # David Cohen
#
# Hint: Think about strip() and title().

print("Task 1")
def clean_name(name):
    return name.strip("_/!@#$%^&*(:;)+?-=., ").title()

print(clean_name("   anna smith   "))
# Anna Smith

print(clean_name("DAVID COHEN"))
# David Cohen

print(clean_name("    @# /.SyLvaNas WiNdRunNeR +^+$+"))
# Sylvanas Windrunner

#spaces are preserved in the middle of the string
print(clean_name(" .. .,@ ^  VariAn    wRynN  %^$*"))
# Varian    Wrynn

print()

# Task 2. Normalize an Email
#
# Write a function normalize_email(email).#
# Remove spaces from the beginning and end.#
# Convert all letters to lowercase.#
# Return the cleaned email.
#
# Example:#
# print(normalize_email("  Anna.Smith@Example.COM  "))
# # anna.smith@example.com
#
# Hint: Use strip() and lower().

print("Task 2")

def normalize_email(email):
    return email.strip("_/!#$%^&*(?):;+-=, ").lower()

print(normalize_email("  Anna.Smith@Example.COM  "))
# anna.smith@example.com

print(normalize_email(" $& ^& _MyEmAil@ExaMple.COM *((( "))
# myemail@example.com

print(normalize_email("  %%+ +123any.email@EMAIL.CoM &: **?? "))
# 123any.email@email.com

print()


# Task 3. Check a File Name
#
# Write a function is_python_file(filename).#
# Return True if the file name ends with .py.#
# The check must work for .py, .PY, .Py, etc.
#
# Example:#
# print(is_python_file("lesson.py"))
# # True
#
# print(is_python_file("HOMEWORK.PY"))
# # True
#
# print(is_python_file("notes.txt"))
# # False
#
# Hint: Normalize the case first, then use endswith().
#

print("Task 3")
def is_python_file(filename):
    return filename.lower().endswith(".py")

print(is_python_file("lesson.py"))
# True

print(is_python_file("HOMEWORK.PY"))
# True

print(is_python_file("notes.txt"))
# False

print(is_python_file("test123.tPy"))
# False

print(is_python_file("^&%^e34t.Py"))
# True

print()

# Task 4. Replace Words
#
# Write a function fix_message(message).#
# Replace every occurrence of the word "bad" with "good".#
# Return the new string.#
# Remember: strings are immutable, so the original string itself is not changed.
#
# Example:#
# message = "bad weather, bad mood"#
# result = fix_message(message)
#
# print(result)
# # good weather, good mood
#
# print(message)
# # bad weather, bad mood
#
# Hint: Use replace().

print("Task 4")

def fix_message(message):
    return message.strip("_/@!#$%^&*(?):;+-=,. ").replace("bad", "good", -1)

message = "bad weather, bad mood"#
result = fix_message(message)

print(result)
# good weather, good mood

print(message)
# bad weather, bad mood

message = "  ...  bad time, good time  ...:) "
result = fix_message(message)

print(result)
# good time, good time

print(message)
#  ...  bad time, good time  ...:)

#shouldn't replace due to capitals
message = "The Good, the Bad and the Ugly"
result = fix_message(message)

print(result)
# The Good, the Bad and the Ugly

print(message)
# The Good, the Bad and the Ugly


print()

# Task 5. Count a Letter
#
# Write a function count_letter(text, letter).#
# Count how many times letter appears in text.#
# The check must be case-insensitive.
#
# Example:#
# print(count_letter("Programming", "g"))
# # 2
#
# print(count_letter("Mississippi", "I"))
# # 4
#
# Hint: Convert both values to the same case and use count().

print("Task 5")

def count_letter(text, letter):
    return text.lower().count(letter.lower())


print(count_letter("Programming", "g"))
# 2

print(count_letter("Mississippi", "I"))
# 4

print(count_letter("*****stars", "**"))
# 2

print(count_letter("10x", "10"))
# 1

print()

# Task 6. Create a Short Login
#
# Write a function create_login(first_name, last_name).#
# Remove unnecessary spaces from both names.#
# Convert both names to lowercase.#
# Create a login in the format: first_name.last_name#
# Return the result.
#
# Example:#
# print(create_login("  Anna ", " SMITH  "))
# # anna.smith
#
# Hint: You can combine several string methods in one task.

print("Task 6")

def create_login(first_name, last_name):
    return f"{first_name.strip().lower()}.{last_name.strip().lower()}"


print(create_login("  Anna ", " SMITH  "))
# anna.smith

# "'" will be present in the lastname
print(create_login("    MoNKey    ", "   D'LuFFy    "))
# monkey.d'luffy

#the numbers will remain unchanged
print(create_login("  Mar1lyN  ", "MaNs0n     "))
# mar1lyn.mans0n


print()

# ⭐ Bonus 1. Split Full Name
#
# Write a function split_name(full_name). Assume the string contains exactly a first name and a last name separated by spaces.
#
# print(split_name("  Anna   Smith  "))
# # ["Anna", "Smith"]
#
# Hint: strip() first, then split().
#

print ("Bonus 1")

def split_name(full_name):
    return full_name.strip().split(maxsplit=1)

print(split_name("  Anna   Smith  "))
# ["Anna", "Smith"]

#symbols and spaces will be present in the lastname since maxsplit=1
print(split_name("      Name1                Last_   _Name        "))
# ['Name1', 'Last_   _Name']

print(split_name("    J0hn        D0e      "))
# ['J0hn', 'D0e']

print()

# ⭐ Bonus 2. Simple Password Check
#
# Write a function check_password(password). Return True only if all conditions are met:#
# the password has at least 8 characters;#
# it contains no spaces;#
# it is not made only of letters;
#
# print(check_password("python123"))
# # True
#
# print(check_password("python"))
# # False
#
# print(check_password("python 123"))
# # False
#
# Hint: Remember len(), isspace()/the in operator, and isalpha().
#

print("Bonus 2")

def check_password(password):
    return  password is not None and not password.isspace() and " " not in password  and not password.isalpha() and len(password) >= 8


print(check_password("python123"))
# True

print(check_password("python"))
# False

print(check_password("python 123"))
# False

print(check_password(None))
# False

print(check_password("     (=^..^=)       "))
# False

# Before submitting
#
# All functions return a result with return.
#
# Add at least 2 of your own calls for each function.
#
# Try different letter cases and strings with extra spaces.
#
# Be ready to explain which string method you used and why.
# #