import sys 
from collections import deque


N = int(sys.stdin.readline())

r1, c1, r2, c2 = map(int, sys.stdin.readline().split(' '))

maps = [[0]*N for _ in range(N)]
visited_maps = [[0]*N for _ in range(N)]
visited_maps[r1][c1] = 1
dx = [-2,-2, 0, 0, 2, 2] 
dy = [-1, 1, -2, 2, -1, 1] 
n  = N
m = N

queue = deque()
queue.append((r1, c1))

while queue:
    x, y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and  visited_maps[nx][ny] == 0:
            maps[nx][ny] = maps[x][y] + 1
            visited_maps[nx][ny] = 1
            queue.append((nx, ny))

if maps[r2][c2] != 0:
    print(maps[r2][c2])
else:
    print(-1)