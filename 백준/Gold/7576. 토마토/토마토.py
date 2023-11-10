import sys 
from collections import deque

m, n = map(int, sys.stdin.readline().split(' '))

maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split(' '))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


queue = deque()
next_tomato_location = []
days = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            queue.append((i, j))


while queue:
    while queue:
        y, x = queue.popleft()
        # for 문으로 현재 위치에서 상하좌우 다 찔러봄
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 현재위치에서 상하좌우 좌표가 갈수 있는지 확인
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0:
                maps[ny][nx] = 1
                next_tomato_location.append((ny, nx))
    queue = deque(next_tomato_location)
    next_tomato_location = []
    if queue:
        days += 1

flag = True
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            print(-1)
            flag = False
            break
    if not flag:
        break
if flag:
    print(days)   

