from collections import deque

n, m = map(int, input().split())
input_list = [list(input()) for _ in range(n)]
fire_visited = [[-1] * 1000 for _ in range(1000)]
jihoon_visited = [[-1] * 1000 for _ in range(1000)]
q = deque()
res = "IMPOSSIBLE"
move = [(1,0),(0,1),(-1,0),(0,-1)]
jihoon_loc = []
for i in range(n):
    for j in range(m):
        if input_list[i][j] == 'J':
            jihoon_loc.append((i,j,'J',1))
            jihoon_visited[i][j] = 1
        if input_list[i][j] == 'F':
            q.append((i, j, 'F', 0))
            fire_visited[i][j] = 1

q.extend(jihoon_loc)
while q:
    x, y, who, depth = q.popleft()
    for dx, dy in move:
        if who == 'J':
            nx = dx + x
            ny = dy + y
            if n <= nx or nx < 0 or m <= ny or ny < 0:
                print(depth)
                exit(0)
            else:
                if input_list[nx][ny] != '#' and fire_visited[nx][ny] == -1 and jihoon_visited[nx][ny] == -1:
                    q.append((nx,ny, 'J', depth+1))
                    jihoon_visited[nx][ny] = 1
        else:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and fire_visited[nx][ny] == -1 and input_list[nx][ny] != '#':
                q.append((nx,ny,'F', 0))
                fire_visited[nx][ny] = 1

print(res)