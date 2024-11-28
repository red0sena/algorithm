import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
node_list = [[] for _ in range(n)]
visited = [False] * n
count = 0

for _ in range(m):
    node, edge = map(int, sys.stdin.readline().rstrip().split(' '))
    node_list[node-1].append(edge - 1)
    node_list[edge - 1].append(node - 1)


def dfs(node):
    global count
    if visited[node] == True:
        return
    count += 1
    visited[node] = True

    for next_node in node_list[node]:
        dfs(next_node)

dfs(0)
print(count-1)
