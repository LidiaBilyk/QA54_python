def greet(name):
    return f"Hello, {name}!"

result =greet("Lidia")
print(result)

def create_user(name, role = "user"):
    return {"name":name, "role":role}

print(create_user("Lidia"))
print(create_user("Lidia", "Admin"))

print()

def calc_discount(price, discount = 20):
    return price - (price * discount)/100

print(calc_discount(2000))
print(calc_discount(2000, 25))

def foo(a = 2,b = 3):
    return a+b
print(foo(5))


def add_tests(name, results = None):
    if results is None:
        results = []
        results.append(name)
        return results

print(add_tests("test_registration"))
print(add_tests("test_login"))


def create_user2(username, email,role):
    return f"{username} ({email}) - {role}"

print(create_user2("Lidia", "test@gm.com", "teamLead"))
print(create_user2(role ="admin", username= "Jessy", email = "test2@gm.com"))



