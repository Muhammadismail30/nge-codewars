# Codewars Challenge
# link: https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python

def remove_exclamation_marks(s):
    hasil = ''
    for char in s:
        if char != '!':
            hasil += char
        else:
            continue
    return hasil

print(remove_exclamation_marks("Hello World!!!"))