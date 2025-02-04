import sys
sys.setrecursionlimit(int(10e8))
n = int(sys.stdin.readline().rstrip())
input_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]
move = [(0,1),(1,0),(-1,0),(0,-1)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    bamboo_list = []
    for dx, dy in move:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < n and 0 <= ny < n:
            if input_list[nx][ny] > input_list[x][y]:
               bamboo_list.append(dfs(nx, ny))
    if not bamboo_list:
        dp[x][y] = 1
        return 1
    bamboo_max = max(bamboo_list)
    dp[x][y] = bamboo_max + 1
    return bamboo_max + 1

max_res = -1
for i in range(n):
    for j in range(n):
        max_res = max(max_res, dfs(i, j))

print(max_res)