# Codewars Challenge
# link: https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

def grow(arr):
    hasil = arr[0]
    for i in range(1, len(arr)):
        hasil *= arr[i]
    return hasil
    

print(grow([1, 2, 3, 4]))  # Output: 24