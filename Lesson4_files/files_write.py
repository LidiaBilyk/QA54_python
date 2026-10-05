#with => try/catch/finally
with open("test.txt", "w", encoding = "utf-8" ) as file:
    file.write("Hello, world!")
    file.write("test")


with open("test.txt", "w", encoding = "utf-8" ) as file:
    file.write("bla-bla-bla")



#r - read (if file already exists, w - write (creates and rewrites), "a" - append (add text to the existing), rb, wd pdf, screenshot

def log_res(test_name, status):
    with open("test1.txt", "a", encoding = "utf-8") as file:
        file.write(f"{test_name}: {status}\n")

log_res("test1", "success")
log_res("test2", "failed")
log_res("test3", "failed")


