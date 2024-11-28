import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

input_list = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()
q.append([1, 0, 0])
visited[0][0] = True

while q:
    distance, x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(distance)
        exit()

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if (0 <= next_x < n and 0 <= next_y < m) and (not visited[next_x][next_y]) and (input_list[next_x][next_y]==1):
            q.append([distance+1, next_x, next_y])
            visited[next_x][next_y] = True




