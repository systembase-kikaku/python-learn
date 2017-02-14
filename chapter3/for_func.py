def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration as e:
            break
        except Exception as e:
            raise

nums = [1,2,3]
for_func(nums, lambda i : print(i))
