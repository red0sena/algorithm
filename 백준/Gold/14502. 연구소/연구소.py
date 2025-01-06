from collections import deque
import copy

n, m = map(int, input().split(' '))
lab_map = [list(map(int, input().split(' '))) for _ in range(n)]
move = [(1,0), (0,1), (-1,0), (0,-1)]
ans = -1

def bfs():
    global ans
    tmp_map = copy.deepcopy(lab_map)
    q = deque()

    for i in range(n):
        for j in range(m):
            if tmp_map[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < m:
                if tmp_map[nx][ny] == 0:
                    tmp_map[nx][ny] = 2
                    q.append((nx, ny))
    count = 0

    for i in range(n):
        for j in range(m):
            if tmp_map[i][j]==0:
                count += 1

    ans = max(ans, count)

def make_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == 0:
                lab_map[i][j] = 1
                make_wall(count+1)
                lab_map[i][j] = 0


make_wall(0)
print(ans)