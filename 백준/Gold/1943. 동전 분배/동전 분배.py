import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coins = []
    total = 0

    for _ in range(n):
        v, c = map(int, input().split())
        total += v * c

        k = 1
        while c > 0:
            take = min(k, c)
            coins.append(v * take)
            c -= take
            k <<= 1

    if total % 2:
        print(0)
        continue

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for coin in coins:
        for j in range(target, coin - 1, -1):
            if dp[j - coin]:
                dp[j] = True

    print(1 if dp[target] else 0)