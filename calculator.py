def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if x == 0 or y == 0:
        return "Cannot divide by zero"
    else:
        return x / y


x = int(input("What's x: "))
y = int(input("What's y: "))
operation = input(
    "What operation do you want to perform? (Add, Subtract, Multiply or Divide) "
)

if operation == "add":
    print(add(x, y))
elif operation == "subtract":
    print(subtract(x, y))
elif operation == "multiply":
    print(multiply(x, y))
elif operation == "divide":
    print(divide(x, y))
