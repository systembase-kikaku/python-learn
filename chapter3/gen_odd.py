def odd(s, e):
    i = s
    while i < e:
        if i % 2 == 1:
            yield i
        i += 1

for i in odd(2, 30):
    print(i)
