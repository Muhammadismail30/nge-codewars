# Codewars Challenge
# link: https://www.codewars.com/kata/5302d846be2a9189af0001e4/train/python

def say_hello(name, city, state):
    name = " ".join(name)
    return f"Hello, {name}! Welcome to {city}, {state}!"

print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))