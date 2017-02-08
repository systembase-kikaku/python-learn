def myfor(itr, cb):
    _itr = iter(itr)
    while True:
        try:
            v = next(_itr)
            cb(v)
        except StopIteration as e:
            break

nums = [1, 2, 4]

myfor(nums, lambda x: print(x))
