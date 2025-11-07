def position(letter):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alfabet)):
        if letter == alfabet[i]:
            return i + 1
    pass

print(position("a"))