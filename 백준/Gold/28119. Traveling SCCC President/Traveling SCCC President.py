import sys

# 유니온-파인드: 부모 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 유니온-파인드: 두 집합 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve():
    # 입력 속도 향상
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    
    # 간선 정보 입력 (u, v, w)
    edges = []
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((w, u, v))
    
    # 방문 순서 정보 (이 문제에서는 MST 구성이 핵심이라 직접적으로 쓰이지 않음)
    # 하지만 입력 형식은 맞춰야 하므로 스킵
    for _ in range(N):
        idx += 1
        
    # 1. 비용 기준 오름차순 정렬
    edges.sort()
    
    parent = [i for i in range(N + 1)]
    mst_weight = 0
    edges_count = 0
    
    # 2. 크루스칼 알고리즘 수행
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_weight += w
            edges_count += 1
            if edges_count == N - 1:
                break
                
    print(mst_weight)

if __name__ == "__main__":
    solve()
    