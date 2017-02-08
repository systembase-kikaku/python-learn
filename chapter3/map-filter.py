l = [2, 3, 4, 5]

print(list(map(lambda x : x * x, l)))
print(list(filter(lambda x : x % 2 == 0, l)))

def odd(x):
    return x % 2 == 0

print(list(filter(odd, l)))
