def remove_exclamation_marks(s):
    hasil = ''
    for char in s:
        if char != '!':
            hasil += char
        else:
            continue
    return hasil

print(remove_exclamation_marks("Hello World!!!"))