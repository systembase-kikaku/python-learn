value = 100

def printValue():
    print(value)
    value = 30

def changeValue():
    global value
    value = 20

printValue()
changeValue()
print(value)
