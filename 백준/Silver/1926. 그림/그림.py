from collections import deque

n, m = map(int, input().split(" "))


input_list = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
move = [(0,1),(0,-1),(1,0),(-1,0)]

painting_num = 0
max_painting_size = 0

for i in range(n):
    for j in range(m):
        if input_list[i][j] == 1 and visited[i][j] == -1:
            q = deque([(i, j)])
            visited[i][j] = 1
            painting_num += 1
            now_painting_size = 1

            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx = dx + x
                    ny = dy + y
                    if 0 <= nx < n and 0 <= ny < m:
                        if visited[nx][ny] == -1 and input_list[nx][ny] == 1:
                            now_painting_size += 1
                            q.append((nx, ny))
                            visited[nx][ny] = 1


            if max_painting_size < now_painting_size:
                max_painting_size = now_painting_size


print(painting_num)
print(max_painting_size)


