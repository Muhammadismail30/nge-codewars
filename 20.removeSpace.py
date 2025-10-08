def no_space(x):
    #your code here
    for space in x:
        if space == " ":
            x = x.replace(" ", "")
    return x