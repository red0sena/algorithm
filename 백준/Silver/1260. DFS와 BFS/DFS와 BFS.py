from collections import deque
import sys

input = sys.stdin.readline

# 입력 받기
N, M, V = map(int, input().split())

# 그래프를 dictionary로 초기화 (정점 번호: 인접 정점 리스트)
graph = {i: [] for i in range(1, N+1)}

# 간선 정보를 양방향으로 추가
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서가 작은 정점부터 탐색할 수 있도록 정렬
for key in graph:
    graph[key].sort()

# DFS 구현 (재귀 방식)
def dfs(v, visited, dfs_result):
    visited.add(v)
    dfs_result.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited, dfs_result)

dfs_result = []
visited_dfs = set()
dfs(V, visited_dfs, dfs_result)

# BFS 구현 (deque를 활용)
bfs_result = []
visited_bfs = [False] * (N + 1)
queue = deque([V])
visited_bfs[V] = True

while queue:
    current = queue.popleft()
    bfs_result.append(current)
    for neighbor in graph[current]:
        if not visited_bfs[neighbor]:
            visited_bfs[neighbor] = True
            queue.append(neighbor)

# 결과 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
