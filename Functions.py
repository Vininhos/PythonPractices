# Defining a function
def add(arg1, arg2):
    total = arg1 + arg2
    return total


result = add(2, 3)
print(result)


def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)


adder(10, 30)


def sum(arg):
    x = 0
    for i in arg:
        x += i
    return x


result = sum([1, 2, 3])
print(result)


# Default Argument
def greetings(msg="Morning"):
    print(f"Good {msg}")
    print("Welcome to the function")


greetings("Evening")
greetings()
