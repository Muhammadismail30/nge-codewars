# Codewars Challenge
# link: https://www.codewars.com/kata/56a4addbfd4a55694100001f

def validate_hello(greetings):
    #your code here
    greetings = greetings.lower()
    hello = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    hasil = None

    for word in hello:
        if word not in greetings:
            hasil = False
        else:
            hasil = True
            break
    return hasil

print(validate_hello("ahoj, cześć, hallo, salut, hola, ciao, hello"))
print(validate_hello("anjay"))