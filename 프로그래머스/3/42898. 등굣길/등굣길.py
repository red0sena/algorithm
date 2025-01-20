from collections import deque
def solution(m, n, puddles):
    map_list = [[1] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    for puddle in puddles:
        map_list[puddle[1] - 1][puddle[0] - 1] = 0
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = deque([(0,0)])

    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y  + dy
            if 0 <= nx < n and 0 <= ny < m:
                if map_list[nx][ny] == 1:
                    map_list[nx][ny] = -1
                    q.append((nx,ny))
        visited[x][y] += visited[x-1][y]
        visited[x][y] += visited[x][y-1]
        visited[x][y] %= 1000000007

    return visited[-1][-1]