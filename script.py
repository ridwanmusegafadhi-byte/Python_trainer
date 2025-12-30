def greet (name = "josef" ):
    return f"Hey {name}"


print(greet("25"))
print(greet())
print("---------------")

def multiply (num):
    return (num *
            num)

print(multiply(9))

print("----------")


def divider (a,b) : return a/b
print(divider(10,3))

print("----------------")
with open('example.py',"w") as file:
    content =file.write("Hello world")
    print(content)

    print("-------")
#read in file
with open('example.txt', "r" ) as file:
    content =file.read()
    print(content)
    print("-------------")
