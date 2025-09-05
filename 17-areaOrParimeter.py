def area_or_perimeter(l , w):
    hasil = 0
    if l == w:
        hasil = l * w
    else:
        hasil = 2 * (l + w)
    return hasil

print(area_or_perimeter(3, 3))
print(area_or_perimeter(6, 10))