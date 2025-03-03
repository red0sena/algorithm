from collections import deque
n, m = map(int, input().split())

input_list = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if input_list[i][j] == 1:
            q.append((i, j))

move = [(0,1),(1,0),(0,-1),(-1,0)]
melt_cheez = []
not_melt_cheez = []
res = 0

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    q = deque([(x, y)])
    while q:
        x, y = q.pop()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if input_list[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
            else:
                return 1
    return 0

while True:
    if not q:
        break
    x, y = q.popleft()
    count = 0
    for dx, dy in move:
        nx = dx + x
        ny = dy + y
        if input_list[nx][ny] == 0:
            count += bfs(nx,ny)
            if count >= 2:
                melt_cheez.append((x,y))
                break
    if count < 2:
        not_melt_cheez.append((x,y))
    if not q and melt_cheez:
        for mx, my in melt_cheez:
            input_list[mx][my] = 0
        res += 1
        q.extend(not_melt_cheez)
        not_melt_cheez = []
        melt_cheez = []

print(res)

