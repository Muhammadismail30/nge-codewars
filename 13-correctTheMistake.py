def correct(s):
    hasil = ""
    for i in s:
        if i == "0":
            hasil += "O"
        elif i == "1":
            hasil += "I"
        elif i == "5":
            hasil += "S"
        else:
            hasil += i
    return hasil
