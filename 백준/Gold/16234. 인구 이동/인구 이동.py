from collections import deque
N, L, R = map(int, input().split())

input_list = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * N for _ in range(N)]


def bfs(sx,sy):
    global visited
    q = deque([(sx,sy)])
    visited[sx][sy] = 1
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    xy_list = []
    sum_val = 0
    while q:
        x, y = q.popleft()
        xy_list.append((x,y))
        sum_val += input_list[x][y]
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    diff = abs(input_list[x][y] - input_list[nx][ny])
                    if diff >= L and diff <= R:
                        visited[nx][ny] = 1
                        q.append((nx,ny))

    len_xy = len(xy_list)
    update_val = sum_val // len_xy
    if len(xy_list) == 1:
        return True
    else:
        for x, y in xy_list:
            input_list[x][y] = update_val
        return False

res = 0

while True:
    visited = [[-1] * N for _ in range(N)]
    flag = True

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                 if not bfs(i,j):
                     flag = False

    if flag:
        break
    res += 1

print(res)
