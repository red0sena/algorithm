import sys


N = int(sys.stdin.readline())
kn_list = []
for _ in range(N):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    kn_list.append((k, n))
for tuple in kn_list:
    k, n = tuple[0], tuple[1]
    k = k+1 
    first_floor = [1*i for i in range(1, n+1)]
    dp = [first_floor]
    for i in range(k):
        floor = [0 for i in range(n)]
        floor[0] = 1
        dp.append(floor)
    for i in range(1, k+1):
        for j in range(0, n):
            if j == 0:
                continue
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    

    print(dp[k-1][n-1])
