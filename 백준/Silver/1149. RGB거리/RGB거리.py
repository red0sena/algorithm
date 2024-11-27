import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())

input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
dp = [[-1] * 3 for i in range(n)]

def recursive(x, y):
    if dp[x][y] != -1: # 이미 계산된 값이 있다면 그 값을 사용
        return dp[x][y]

    current = input_list[x][y]

    if x == n - 1:
        dp[x][y] = current
        return current

    min_price = float("inf")
    direction = 2 - y
    if direction == 2:
        min_price = min(min_price, recursive(x+1, y+1), recursive(x+1, y+2))
    if direction == 1:
        min_price = min(min_price, recursive(x+1, y-1), recursive(x+1, y+1))
    if direction == 0:
        min_price = min(min_price, recursive(x+1, y-1), recursive(x+1, y-2))
    dp[x][y] = current + min_price
    return dp[x][y]

print(min(recursive(0, 2), recursive(0, 1), recursive(0, 0)))

