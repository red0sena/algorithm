from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 방향 벡터 (동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def count_sea(x, y):
    """주변 바다(0인 칸)의 개수를 반환"""
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
            count += 1
    return count

def melt_iceberg():
    """빙산을 녹이고, 녹은 후 빙산이 남아있는지 확인"""
    new_grid = [row[:] for row in grid]
    has_ice = False
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                new_grid[i][j] = max(0, grid[i][j] - count_sea(i, j))
                if new_grid[i][j] > 0:
                    has_ice = True
    for i in range(N):
        grid[i] = new_grid[i][:]
    return has_ice

def bfs(x, y, visited):
    """BFS로 연결된 빙산 덩어리 탐색"""
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_icebergs():
    """빙산 덩어리 개수 세기"""
    visited = [[False] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

# 메인 로직
year = 0
while True:
    # 빙산이 모두 녹았는지 확인
    if not melt_iceberg():
        print(0)
        break
    year += 1
    # 빙산 덩어리 개수 확인
    iceberg_count = count_icebergs()
    if iceberg_count >= 2:
        print(year)
        break