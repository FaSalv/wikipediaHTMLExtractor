def removeN(string):
    pop = string[-2:]
    if pop == "\n":
        newString = string[:-2]
    elif pop == "\n ":
        newString = string[:-2]
    else:
        newString = string
    return newString
