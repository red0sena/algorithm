import sys

def solve_2560():
    a, b, d, N = map(int, sys.stdin.readline().split())
    # dp[i]: i일에 태어난 짚신벌레 수
    dp = [0] * (N + 1)
    dp[0] = 1
    current_adults = 0
    
    for i in range(1, N + 1):
        # i일에 성체가 된 벌레 추가 (i-a일에 태어난 애들)
        if i >= a:
            current_adults = (current_adults + dp[i-a]) % 1000
        # i일에 더 이상 번식 못하게 된 벌레 제외 (i-b일에 태어난 애들)
        if i >= b:
            current_adults = (current_adults - dp[i-b] + 1000) % 1000
        
        dp[i] = current_adults
        
    # N일에 살아있는 벌레 = 최근 d일 동안 태어난 벌레들의 합
    ans = sum(dp[max(0, N-d+1):]) % 1000
    print(ans)

solve_2560()