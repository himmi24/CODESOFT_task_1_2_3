## SIMPLE CALCULATOR ##

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Getting user input for numbers and operation choice
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation= input("Enter Operator (+ for Addition, - for Subtraction, * for Multiplication, / for Division: ")

# Performing calculation based on the operation choice
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation selected! Enter correct operation! "

# Display the result
print("Result: ",result)
