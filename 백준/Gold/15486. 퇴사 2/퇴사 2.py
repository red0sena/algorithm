import sys

n = int(sys.stdin.readline().rstrip())

input_list = []

for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    input_list.append((t,p))

dp = [0] * (n + 1)


for i in range(n):
    t, p = input_list[i]
    dp[i+1] = max(dp[i+1], dp[i])
    if i+t < n + 1:
        if dp[i+t] < dp[i] + p:
            dp[i+t] = dp[i] + p

print(dp[-1])
