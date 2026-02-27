import sys
from collections import deque
from itertools import permutations

def bfs(start_pos, target_pos, grid, h, w):
    q = deque([start_pos])
    visited = [[-1] * w for _ in range(h)]
    visited[start_pos[0]][start_pos[1]] = 0
    while q:
        r, c = q.popleft()
        if (r, c) == target_pos: return visited[r][c]
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] != 'x' and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    return -1

def solve_4991():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0: break
        grid = [list(sys.stdin.readline().strip()) for _ in range(h)]
        
        starts = []
        dirty = []
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 'o': starts = (r, c)
                elif grid[r][c] == '*': dirty.append((r, c))
        
        points = [starts] + dirty
        n = len(points)
        dist_matrix = [[0]*n for _ in range(n)]
        
        possible = True
        for i in range(n):
            for j in range(i+1, n):
                d = bfs(points[i], points[j], grid, h, w)
                if d == -1:
                    possible = False; break
                dist_matrix[i][j] = dist_matrix[j][i] = d
            if not possible: break
            
        if not possible:
            print(-1); continue
            
        res = float('inf')
        # 로봇(0번)을 제외한 나머지 지점들의 순열
        for p in permutations(range(1, n)):
            current_dist = dist_matrix[0][p[0]]
            for i in range(len(p)-1):
                current_dist += dist_matrix[p[i]][p[i+1]]
            res = min(res, current_dist)
        print(res)

solve_4991()