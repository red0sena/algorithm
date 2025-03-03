from collections import deque

def bfs(N, M, grid):
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 외부 공기 표시 (-1), 치즈(1), 내부 공기(0)
    def mark_air():
        visited = [[False] * M for _ in range(N)]
        q = deque([(0, 0)])  # 가장자리에서 시작 (외부 공기)
        grid[0][0] = -1
        visited[0][0] = True
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] != 1:
                    grid[nx][ny] = -1  # 외부 공기로 표시
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    time = 0
    while True:
        # 1. 외부 공기 영역 표시
        mark_air()
        
        # 2. 녹을 치즈 찾기
        melting = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    air_count = 0
                    for k in range(4):
                        ni, nj = i + dx[k], j + dy[k]
                        if grid[ni][nj] == -1:  # 외부 공기와 접촉
                            air_count += 1
                    if air_count >= 2:  # 2변 이상 공기와 접촉
                        melting.append((i, j))
        
        # 3. 치즈가 더 이상 녹지 않으면 종료
        if not melting:
            return time
        
        # 4. 치즈 녹이기
        for x, y in melting:
            grid[x][y] = 0  # 치즈 제거
        
        time += 1

# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(bfs(N, M, grid))