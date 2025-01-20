from collections import deque

def solution(m, n, puddles):
    data = [[1] * m for _ in range(n)]
    path = [[0] * m for _ in range(n)]
    path[0][0] = 1
    for p in puddles:
        data[p[1]-1][p[0]-1] = 0

    q = deque()
    q.append((0,0))
    dxdy = (1, 0), (-1, 0), (0, 1), (0, -1)
    while q:
        y, x = q.popleft()
        for dy, dx in dxdy:
            if x+dx<0 or x+dx>=m or y+dy<0 or y+dy>=n:
                continue
            if data[y+dy][x+dx] == 1:
                data[y+dy][x+dx] += data[y][x]
                q.append((y+dy, x+dx))
        path[y][x] += path[y-1][x]
        path[y][x] += path[y][x-1]
        path[y][x] %= 1000000007

    return path[-1][-1]