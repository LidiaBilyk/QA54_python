with open("user.txt", "w", encoding="utf-8") as file:
    file.write("test \n" )
    file.write("passed\n")

#read() - whole file
print("read")
with open("user.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))
print()

#readlines()  returns list with element == line
print("readlines")
with open("user.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
    print(len(lines))
    for line in lines:
        print(line.strip())

print()

#for
print("for")
with open("user.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())