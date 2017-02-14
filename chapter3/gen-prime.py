def genPrime(maxnum):
    num = 1
    while num <= maxnum:
        num += 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime == True:
            yield num

it = genPrime(50)

for i in it:
    print(i)
