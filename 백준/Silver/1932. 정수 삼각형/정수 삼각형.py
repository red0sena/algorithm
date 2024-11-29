import sys

n = int(sys.stdin.readline().rstrip())
input_tree = []
for _ in range(n):
    input_tree.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
dp = []

for line in input_tree:
    dp.append([-1] * len(line))


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]


    if x!=n-1:
        dp[x][y] = max(dfs(x+1, y) + input_tree[x][y], dfs(x+1, y+1) + input_tree[x][y])
        return dp[x][y]
    return input_tree[x][y]

print(dfs(0, 0))
