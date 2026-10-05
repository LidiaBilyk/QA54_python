def login(username, password):
    print(username, password)

data = ["admin", "897654"]
login(data[0], data[1])
login(*data)
user = {
    "username": "admin",
    "password": "897654"
}
login(**user)

# user = {
#     "username": "admin",
#     "password": "897654",
#     "email": "1@test.com"  #TypeError: login() got an unexpected keyword argument 'email'
# }
# login(**user)