import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

n, m = map(int, sys.stdin.readline().split(' '))

maps = []

for i in range(n):    
	maps.append(list(map(int, input().split())))


visited = [[-1] * m for _ in range(n)]



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if visited[x][y] == -1:
        visited[x][y] = 0

        for direction in range(4):
            new_dx = x + dx[direction]
            new_dy = y + dy[direction]

            if 0 <= new_dx < n and 0 <= new_dy < m:    
                if maps[new_dx][new_dy] < maps[x][y]:
                    visited[x][y] += dfs(new_dx, new_dy)

    return visited[x][y]

                    




print(dfs(0, 0))