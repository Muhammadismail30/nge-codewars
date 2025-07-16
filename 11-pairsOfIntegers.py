def generate_pairs(n):
    hasil = []
    for i in range(n + 1):
        for j in range(i, n + 1):
            hasil.append([i, j])
    return hasil

print(generate_pairs(2)) # output  [  [0, 0], [0, 1], [0, 2],  [1, 1], [1, 2],  [2, 2]  ]