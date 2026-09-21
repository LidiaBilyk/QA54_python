# HOMEWORK
# Loops + List Methods
# Practice: for / while, indexes, and basic list methods
# Use only the topics we have already covered. Try to solve the tasks with loops and list methods. Do not use list comprehensions, sort()/sorted(), max(), min(), or other shortcuts unless the task says otherwise.
#
# Mandatory
#
# Task 1. Shopping cart
# Write a function clean_cart(cart). The list contains product names. Remove all occurrences of the string "sold out" and return the updated list.
# print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
# # ["milk", "bread", "coffee"]
# Hint: Be careful when removing elements while iterating through a list.
#

print("Task1")
def clean_cart(cart):
    while "sold out" in cart:
        cart.remove("sold out")
    return cart

print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
# ["milk", "bread", "coffee"]
print()

# Task 2. Temperature report
# Write a function temperature_report(temperatures). Return a NEW list containing only temperatures greater than 25.
# print(temperature_report([21, 28, 19, 31, 25, 27]))
# # [28, 31, 27]
# Hint: Create an empty result list and add suitable values with append().
#
print("Task2")
def temperature_report(temperatures):
    new_list = []
    for temp in temperatures:
        if temp > 25: new_list.append(temp)
    return new_list

print(temperature_report([21, 28, 19, 31, 25, 27]))
# [28, 31, 27]
print()

# Task 3. Fix negative balances
# Write a function fix_balances(balances). Replace every negative value in the SAME list with 0. Return the list.
# print(fix_balances([120, -30, 50, -5, 0, 200]))
# # [120, 0, 50, 0, 0, 200]
# Hint: Here you need indexes because you are changing list elements.
#
print("Task3")
def fix_balances(balances):
    for i in range(len(balances)):
       if balances[i] < 0: balances[i] = 0
    return balances

print(fix_balances([120, -30, 50, -5, 0, 200]))
# [120, 0, 50, 0, 0, 200]
print()

# Task 4. Remove duplicates without set
# Write a function unique_items(items). Return a new list containing each value only once, preserving the original order. Do not use set().
# print(unique_items(["red", "blue", "red", "green", "blue"]))
# # ["red", "blue", "green"]
# Hint: Before append(), check whether the value is already in the result list.
#
print("Task4")
def unique_items(items):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(unique_items(["red", "blue", "red", "green", "blue"]))
# ["red", "blue", "green"]
print()


# Advanced
# ADVANCED · Task 5. Longest word
# Write a function longest_word(words). Find and return the longest word in the list. If several words have the same maximum length, return the first one. Do not use max().
# print(longest_word(["cat", "elephant", "python", "coffee"]))
# # "elephant"
# Hint: Keep the best word found so far and compare len().

print("Task5")
def longest_word(words):
    longest_candidate = ""
    for word in words:
        if len(word) > len(longest_candidate):
            longest_candidate = word
    return longest_candidate

print(longest_word(["cat", "elephant", "python", "coffee"]))
# "elephant"
print(longest_word(["cat", "elephant", "python", "coffee", "password"]))
# "elephant"