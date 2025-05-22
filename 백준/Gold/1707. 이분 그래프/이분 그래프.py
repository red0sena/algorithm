import sys
from collections import deque


k = int(sys.stdin.readline().rstrip())


def bfs(v, graph, color, i):
    q = deque([(i, 1)])
    color[i] = 1
    while q:
        u, now_color = q.popleft()
        for v in graph[u]:

            if color[v] == 0:
                next_color =  now_color * -1
                color[v] = next_color
                q.append((v, next_color))

            else:
                if color[v] == color[u]:
                    return False
    return True



for _ in range(k):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True
    for i in range(1, v + 1):
        if color[i] == 0:  # 미방문 정점에서 BFS 시작
            if not bfs(v, graph, color, i):
                result = False
                break

    if result:
        print("YES")
    else:
        print("NO")