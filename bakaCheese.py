import sys

sys.setrecursionlimit(1000000)

memo = {}


def bob(n):
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
    
    bob_n = bob(n-2) + bob(n-1)
    memo[n] = bob_n
    
    return bob_n


print(bob(1) == 0)
print(bob(2) == 1)
print(bob(3) == 1)
print(bob(4) == 2)


print(f'4000th number is: {bob(49999)}')
