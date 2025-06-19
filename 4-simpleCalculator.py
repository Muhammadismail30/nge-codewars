# Codewars Challenge
# link: https://www.codewars.com/kata/5302d846be2a9189af0001e4/train/python

def calculator(x:int, y:int, op):
    try:
        x = int(x)
        y = int(y)
    except (ValueError, TypeError):
        return "unknown value"
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            return "Error: Division by zero"
        return x / y
    else:
        return "unknown value"
    

print(calculator(6, 2, '+'))