def ensure_question(s):
    hasil = ''
    if '?' in s[-1:]:
        hasil = s
    else:
        hasil = s + '?'
    return hasil

print(ensure_question("Does this work"))
print(ensure_question("Does this work?"))