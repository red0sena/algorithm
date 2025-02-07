from collections import deque

n = int(input())

input_list = [list(map(int, input())) for _ in range(n)]

visited = [[-1] * n for _ in range(n)]
move = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque([(0,0)])
visited[0][0] = 0
while q:
    x, y = q.popleft()
    if x == n-1 and y == n-1:
        print(visited[x][y])
        break
    for dx, dy in move:
        nx = dx + x
        ny = dy + y

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == -1:
                if input_list[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

