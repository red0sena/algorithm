import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split(' '))
node_list = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    node, edge = map(int, sys.stdin.readline().rstrip().split(' '))
    node_list[node-1].append(edge-1)
    node_list[edge - 1].append(node - 1)

for i in range(n):
    node_list[i] = sorted(node_list[i])

## DFS ##
def dfs(node):
    if visited[node] == True:
        return
    visited[node] = True

    print(node+1, end=' ')
    for next_node in node_list[node]:
        dfs(next_node)

dfs(v-1)
print()
## BFS ##
visited = [False] * n

q = deque()
q.append(v-1)
visited[v-1] = True

while q:
    node = q.popleft()
    print(node+1, end=' ')

    for next_node in node_list[node]:
        if visited[next_node]:
            continue
        q.append(next_node)
        visited[next_node] = True