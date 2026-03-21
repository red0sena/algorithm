def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M, S = map(int, input().split())

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# 방문 순서 정보: 한 줄에 주어짐
order = list(map(int, input().split()))

edges.sort()

parent = [i for i in range(N + 1)]
mst_weight = 0
edges_count = 0

for w, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        mst_weight += w
        edges_count += 1
        if edges_count == N - 1:
            break

print(mst_weight)