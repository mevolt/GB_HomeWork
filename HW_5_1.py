def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


odd_to_10 = odd_nums(10)
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))

