import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
    
    total_water = 0
    
    # 높이 2부터 9까지 물을 한 층씩 채운다고 가정
    for h in range(2, 10):
        visited = [[False] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                # 현재 높이 h보다 낮고 방문하지 않은 칸 발견
                if grid[i][j] < h and not visited[i][j]:
                    total_water += bfs(i, j, h, n, m, grid, visited)
                    
    print(total_water)

def bfs(si, sj, h, n, m, grid, visited):
    q = deque([(si, sj)])
    visited[si][sj] = True
    
    cells = [(si, sj)]
    is_leaking = False
    
    while q:
        r, c = q.popleft()
        
        # 4방향 탐색
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            # 경계를 벗어난다면 이 영역은 물이 고일 수 없음 (밖으로 샘)
            if not (0 <= nr < n and 0 <= nc < m):
                is_leaking = True
                continue
                
            if grid[nr][nc] < h and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))
                cells.append((nr, nc))
                
    if is_leaking:
        return 0
    else:
        # 고인 물의 양 계산: 영역 내 모든 칸에 물을 1층 쌓음
        for r, c in cells:
            grid[r][c] += 1
        return len(cells)

solve()