# Codewars Challenge
# link: https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    hasil = []
    for i in range(n):
        hasil.append(x * (i + 1))
    return hasil
    
print(count_by(2, 5))