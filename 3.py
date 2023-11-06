def add(num1,num2):
    return num1 + num2 
def subtract(num1,num2):
    return num1 - num2 
def multiply(num1,num2):
    return num1 * num2 
def divide(num1,num2):
    return num1 / num2 

# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    result = add(first_number, second_number)
    print(f"Result: {result}")
elif operation == "subtract":
    result = subtract(first_number, second_number)
    print(f"Result: {result}")
elif operation == "multiply":
    result = multiply(first_number,second_number)
    print(f"Result: {result}")
elif operation == "divide":
    result = divide(first_number, second_number)
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")
