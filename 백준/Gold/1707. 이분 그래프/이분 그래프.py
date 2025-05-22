from collections import deque

def is_bipartite(v, graph, color, start):
    q = deque([(start, 1)])  # (정점, 색상)
    color[start] = 1  # 시작 정점에 색 1 부여
    while q:
        u, now_color = q.popleft()
        for v in graph[u]:
            if color[v] == 0:  # 방문하지 않은 정점
                next_color = -now_color  # 반대 색상 부여
                color[v] = next_color
                q.append((v, next_color))
            elif color[v] == now_color:  # 인접 정점과 색이 같으면 이분 그래프 아님
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)  # 0: 미방문, 1: 색1, -1: 색2
    
    # 간선 입력
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 모든 정점에 대해 BFS 수행
    is_bipartite_graph = True
    for i in range(1, v + 1):
        if color[i] == 0:  # 아직 방문하지 않은 정점에서 BFS 시작
            if not is_bipartite(v, graph, color, i):
                is_bipartite_graph = False
                break
    
    print("YES" if is_bipartite_graph else "NO")