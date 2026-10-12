#only performs calculator
def calculator(a: float, b: float, operator: str):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    raise ValueError("Invalid operator")


#parsing converts string into num

def parse(a_str: str, b_str, operator: str):
    a = float(a_str) # value error
    b = float(b_str) # value error
    return calculator(a, b, operator)

#dialog
def run():
    try:
        a = input("Enter a number: ")
        b = input("Enter another number: ")
        operator = input("Enter Action operator (+, -, *, /): ")
        result = parse(a, b, operator)
        print(f"Result: {result}")

    except ValueError as e:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print(f"Cannot divide by zero")
run()

