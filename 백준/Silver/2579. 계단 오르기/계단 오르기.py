import sys
sys.setrecursionlimit(int(10e7))
n = int(sys.stdin.readline().rstrip())

stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline().rstrip()))
dp = [-1] * n
if n == 1:
    print(stairs[-1])
elif n == 2:
    print(stairs[0] + stairs[1])
elif n == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[-1])

