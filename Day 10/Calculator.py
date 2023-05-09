from Art import logo

def calculate(operation, num1, num2):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtraction(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    else:
        print("You must enter one of four operation (+)(-)(/)(*)")

def add(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    if num2 == 0:
        print(f"You can't divide number with zero")
    else:
        result = num1 / num2
        return result

def calculater():
    say_no = False
    print(logo)
    number1 = float(input("Enter the first number: "))
    while not say_no:
        operation = input("Enter the operation: ")
        number2 = float(input("Enter the next number: "))
        result = calculate(operation, number1, number2)

        if operation in ["+", "-", "*", "/"]:
            print(f"Result: {number1} {operation} {number2} = {result}")
        
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")

        if answer == "y":
            number1 = result
        elif answer == "n":
            calculater()

calculater()