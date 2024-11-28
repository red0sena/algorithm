import sys
sys.setrecursionlimit(int(10e7))
n = int(sys.stdin.readline().rstrip())
dp = [-1] * n


def recursive(depth):
    if depth == n:
        return 1
    if depth > n:
        return 0
    if dp[depth] != -1:
        return dp[depth]

    a = recursive(depth+1)
    b = recursive(depth+2)
    dp[depth] = a+b
    return a+b


print(recursive(0) % 10007)
