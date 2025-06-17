# Codewars Challenge
# link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

def even_or_odd(number):
    hasil = ""
    if number % 2 == 0:
        hasil = "Even"
    else:
        hasil = "Odd"
    return hasil

print(even_or_odd(2))  # Output: "Even"
print(even_or_odd(3))  # Output: "Odd"