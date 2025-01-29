n = int(input())

wine_list = []
for _ in range(n):
    wine_list.append(int(input()))

dp = [0] * n
if n == 1:
    print(wine_list[0])
elif n == 2:
    print(wine_list[0]+wine_list[1])
else:
    dp[0] = wine_list[0]
    dp[1] = wine_list[0] + wine_list[1]
    dp[2] = max(wine_list[2] + wine_list[1], wine_list[0]+wine_list[2], dp[1])
    for i in range(3, n):
        dp[i] = max( # 현재 최대 포도주는
            dp[i - 1],  # 현재 포도주를 마시지 않는다.
            dp[i - 3] + wine_list[i - 1] + wine_list[i], # 현재 포도주와 이전포도주를 마시고 전전 포도주는 마시지 않는다.
            dp[i - 2] + wine_list[i] # 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다.
        )
    print(dp[-1])

