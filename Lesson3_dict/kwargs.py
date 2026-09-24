

def print_config(**kwargs):
    print(type(kwargs), kwargs)

print_config(browser="safari", headless="True", timeout=10)

def create_user3(**data):
    return data

user = create_user3(name="Jessy", role="student")
print(user)


def for_example(a, b=15,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

for_example(2,3,4,5,name="Jessy")
