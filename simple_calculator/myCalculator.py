#Import logo
from turtle import clear
from calculatorLogo import logo

#Definition of operators
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Create main function
def calculator():
    print(logo)
    number1 = float(input("What is your first number?: "))
    for symbol in operations:
        print(symbol)
    isContinue = True

    #Looping till user choose not to continue
    while isContinue:
        operationSymbol = input("Pick an operation: ")
        number2 = float(input("What is your next number?: "))
        calcFunct = operations[operationSymbol]
        answer = calcFunct(number1, number2)
        print(f"{number1} {operationSymbol} {number2} = {answer}")

        #Select condition
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            number1 = answer
        else:
            isContinue = False
            clear()
            calculator()

#Calling the main function
calculator()
