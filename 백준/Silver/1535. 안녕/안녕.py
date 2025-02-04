import sys



n = int(sys.stdin.readline().rstrip())

L = list(map(int, sys.stdin.readline().rstrip().split()))
J = list(map(int, sys.stdin.readline().rstrip().split()))

LJ_list = list(tuple(zip(L, J)))



k = 100
dp = [0] * (k + 1)
for L, J in LJ_list:
    for w in range(k-1, L-1, -1):
        dp[w] = max(dp[w], dp[w-L] + J)

print(dp[k-1])
