from collections import deque
import sys
input = sys.stdin.readline

def is_bipartite(v, graph, color, start):
    q = deque([start])
    color[start] = 1  # 시작 정점 색 1
    while q:
        u = q.popleft()
        for v in graph[u]:
            if color[v] == 0:  # 미방문 정점
                color[v] = -color[u]  # 반대 색 부여
                q.append(v)
            elif color[v] == color[u]:  # 색 충돌
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    
    # 간선 입력
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 모든 정점에 대해 BFS
    result = True
    for i in range(1, v + 1):
        if color[i] == 0:  # 미방문 정점에서 BFS 시작
            if not is_bipartite(v, graph, color, i):
                result = False
                break
    
    print("YES" if result else "NO")