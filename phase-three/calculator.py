def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calcuator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    while True:
        operation = input("Enter an operation (+, -, *, / and q for quit): ")
        if operation == "q":
            break
        try:
            x = float(input("Enter a number: "))
            y = float(input("Enter another number: "))
            if operation in operations:
                print(operations[operation](x, y))
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid input")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        

if __name__ == "__main__":
    calcuator()