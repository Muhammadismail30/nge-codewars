def logical_calc(array, op):
    hasil = None
    if op == "AND":
        hasil = True
        for bool in array:
            hasil = hasil and bool
    elif op == "OR":
        hasil = False
        for bool in array:
            hasil = hasil or bool
    elif op == "XOR":
        hasil = False
        for bool in array:
            if hasil is False:
                hasil = bool
            else:
                hasil = hasil != bool
    return hasil