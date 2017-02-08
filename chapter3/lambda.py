l = lambda x : x * 2
print(l(10))

def func(l, arg):
    return l(arg)

print(func(lambda x : x * x, 5))
