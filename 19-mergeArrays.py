def merge_arrays(first, second): 
    hasil = []
    first.sort()
    second.sort()
    for i in first:
        if i not in hasil:
            hasil.append(i)
    for j in second:
        if j not in hasil:
            hasil.append(j)
    hasil.sort()
    return hasil