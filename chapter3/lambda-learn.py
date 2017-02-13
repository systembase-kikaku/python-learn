x2 = lambda x : x * 2
xy = lambda x,y : x * y
tri = lambda a,b : a * b / 2


print(x2(3))
print(xy(3,10))
print(tri(13, 15))


def calc_5_3(func):
    return func(5,3)

result = calc_5_3(lambda a,b: a * b)
print(result)
result = calc_5_3(lambda a,b: a + b)
print(result)
