t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    dp = [0] * (k+1)
    for _ in range(n):
        weight, value = map(int, input().split())
        for w in range(k, weight-1, -1):
            dp[w] = max(dp[w], dp[w-weight]+value)

    print(dp[k])

