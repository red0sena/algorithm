from collections import deque

def bfs(graph, start, n, m):
    # 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 방문 여부와 거리를 저장하는 배열
    visited = [[-1] * m for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    max_distance = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 지도 범위 내이고, 육지이며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                max_distance = max(max_distance, visited[nx][ny])
    
    return max_distance

def solve():
    # 입력
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    
    max_dist = 0
    # 모든 육지 지점에서 BFS 수행
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                max_dist = max(max_dist, bfs(graph, (i, j), n, m))
    
    return max_dist

print(solve())