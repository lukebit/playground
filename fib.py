import sys

sys.setrecursionlimit(1000000)

memo = {}


def fib(n):
    if n == 1:
        memo[1] = 0
        return 0 
    elif n == 2:
        memo[2] = 1
        return 1
    elif n == 3:
        return 1

    if memo.get(n) is not None:
        return memo[n]
    
    bob_n = fib(n-2) + fib(n-1)
    memo[n] = bob_n
    
    return bob_n


print(fib(1) == 0)
print(fib(2) == 1)
print(fib(3) == 1)
print(fib(4) == 2)

print(f'500th number is: {fib(500)}')
