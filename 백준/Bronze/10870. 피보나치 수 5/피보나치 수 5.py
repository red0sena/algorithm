import sys

n = int(sys.stdin.readline().rstrip())

memo = {0:0, 1:1}

def fibo_recursive(x):
    if x in memo:
        return memo[x]
    a = fibo_recursive(x - 1) + fibo_recursive(x - 2)
    memo[x] = a
    return a

print(fibo_recursive(n))