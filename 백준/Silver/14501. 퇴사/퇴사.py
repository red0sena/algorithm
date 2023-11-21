N = int(input())
input_list = []
for _ in range(N):
    a, b = map(int, input().split())
    input_list.append((a,b))

dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i+input_list[i][0], N+1):
        if dp[j] < dp[i] + input_list[i][1]:
            dp[j] = dp[i] + input_list[i][1]

print(dp[-1])