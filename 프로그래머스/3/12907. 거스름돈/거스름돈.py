def solution(n, money):
    # dp[i]는 i원을 만드는 경우의 수를 저장
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 경우는 1가지
    
    # 돈의 종류를 하나씩 사용하면서 dp 배열 채우기
    for coin in money:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[n]
