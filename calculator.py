def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    if number_1 or number_2 == 0:
        return "Cannot divide by zero"
    else:
        return number_1 / number_2
    
x = int(input("What's x: "))
y = int(input("What's y: "))
operation = input("What operation do you want to perform? (Add, Subtract, Multiply or Divide)")

if operation == "Add":
    add(x, y)
elif operation == "Subtract":
    subtract(x, y)
elif operation == "Multiply":
    multiply(x, y)
else:
    divide(x, y)
