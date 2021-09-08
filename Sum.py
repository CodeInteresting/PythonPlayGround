def Sum(num):
    if num == 0:
        return 0
    return num + Sum(num - 1)


print(Sum(10))


def Sum2(num, agg):
    if num == 0:
        return agg
    return Sum2(num - 1, agg + num)


print(Sum2(10, 0))


# f(0) = 0
# f(1) = 1
# f(n) = f(n - 1) + f(n - 2)
def Fib(n):
    if n < 2:
        return n
    N_minus_one = 1  # f(1)
    N_minus_two = 0  # f(0)
    N = 0  # (f(2))

    for i in range(2, n + 1):
        N = N_minus_one + N_minus_two
        N_minus_two = N_minus_one
        N_minus_one = N
    return N


def Fib2(n):
    if n < 2:
        return n
    return Fib2(n - 1) + Fib2(n - 2)


def Fib3(n, cache):
    if n < 2:
        return n

    if n in cache:
        return cache[n]
    else:
        cache[n] = Fib3(n - 2, cache) + Fib3(n - 1, cache)
        return cache[n]


print(Fib(0))
print(Fib(1))
print(Fib(11))

print(Fib2(0))
print(Fib2(1))
print(Fib2(11))

print(Fib3(11, {}))
