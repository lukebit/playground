from re import S


def add_five(x):
    y = x + 5
    return y


def deduct_five(f):
    g = f - 5
    return g


def power_10(x):
    r = x ** 10
    return r

# print(power_10(30))


def sum_up_to(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(sum_up_to(1000000000000000000000000000000000))
