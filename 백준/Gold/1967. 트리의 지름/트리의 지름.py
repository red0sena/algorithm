from collections import defaultdict, deque
import sys

input = sys.stdin.readline
graph = defaultdict(list)
n = int(input())

for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append((start, 0))
    visited[start] = True
    farthest_node = start
    max_dist = 0
    while q:
        node, dist = q.popleft()
        if dist > max_dist:
            max_dist = dist
            farthest_node = node
        for next_node, weight in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, dist + weight))
    return farthest_node, max_dist

# 1번 노드에서 가장 먼 노드 A 찾기
A, _ = bfs(1)
# A에서 가장 먼 노드까지의 거리(=지름)
_, diameter = bfs(A)
print(diameter)