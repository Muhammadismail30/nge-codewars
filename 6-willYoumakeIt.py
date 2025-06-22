# Codewars Challenge
# link: https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
def zero_fuel(distance_to_pump, mpg, fuel_left):
    hasil = None
    if (distance_to_pump / mpg <= fuel_left):
        hasil = True
    else:
        hasil = False
    return hasil

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))