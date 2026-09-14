s = "cat"
s = s.upper()
print(s)

s1 = 'Hello'
s2 = "Hello"
s3 = """Line one  
Line two""" # """ allow to format a string
print(s1)
print(s2)
print(s3)

print(s1, s2, s3, sep = "\n")


#len()
s = "Helo my group!"
print(len(s))
print(s[0])
print(s[4])

print(s[-1])

#print(s[100])

#len() 1 2 3 4 5 6
s1 = "P y t h o n"
#ind   0 1 2 3 4 5  -> index of last element = len()-1 or -1


#slicing -> my_string[start:end:step]
text = "automation"
print(text[2:6])
print(text[:4]) #from start to ind 4 exclusive
print(text[4:]) #from ind inclusive to end
print(text[:])
print(text[::2]) #every 2 symbol
print(text[::-1]) #reverse
print(text[5:100]) #till the end, no error



#format
name = "Mariia"
last_name = "Ivanova"
age = 25
print(name + " " + last_name + "-" + str(age))
print(f"Hi my name is {name} and my last name is {last_name} and I'm {age}")


#upper()/lower()
raw = "      Automation QA      "
print(raw.upper())
print(raw.lower())

#strip()

print(raw.strip())
print(raw.strip().upper())


#split()/join()
cvs_line = "Login:Cart,Checkout,Mama,Papa"
parts = cvs_line.split(",")
print(parts)
print(" - ".join(parts))


#replace()
msg = "Test failed: element not found"
print(msg.replace("failed","passed"))


#find() and index()
# find() -> -1 if substring is not found, but index() -> error

s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
# print(s.index("xyz"))



#count()
print(s.count("na"))



