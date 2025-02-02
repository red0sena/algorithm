import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
input_list = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0]
this_sum = 0
for i in range(n):
    this_sum += input_list[i]
    dp.append(this_sum)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(dp[j] - dp[i-1])