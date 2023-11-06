import calculator

num1 = float(input('Enter your first number:'))
num2 = float(input('Enter your second number:'))
operator = input('What operation are you running (add, subtract, multiply or divide):')

while operator not in ('add', 'subtract', 'multiply', 'divide'):
    print('Invalid operator input!')
    operator = input('What operation are you running (add, subtract, multiply or divide):')

if operator == "add":
    result = calculator.add (num1,num2)
elif operator == "subtract":
    result = calculator.subtract (num1,num2)
elif operator == "multiply":
    result = calculator.multiply (num1,num2)
elif operator == "divide":
    result = calculator.divide (num1,num2)

print(f'Result: {result}')