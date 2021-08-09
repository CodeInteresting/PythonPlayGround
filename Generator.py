def genNums(n):
    for i in range(n):
        yield i


counter = genNums(10)
value = next(counter)
value = next(counter)
print(value)
