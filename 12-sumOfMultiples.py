def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(i for i in range(n, m, n))

print(sum_mul(2, 9)) # output 20