from collections import deque

n = int(input())
input_list = [list(map(int, input())) for _ in range(n)]


move = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs():
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    q = deque([(0,0)])
    flag=False
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1:
            return visited[x][y]

        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if input_list[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


print(bfs())
