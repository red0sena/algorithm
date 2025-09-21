import sys

# Union-Find를 위한 find 함수 (경로 압축 적용)
def find_parent(parent, x):
    """
    노드 x의 루트 노드를 찾습니다. 경로 압축을 통해 효율성을 높입니다.
    """
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union-Find를 위한 union 함수
def union_parent(parent, a, b):
    """
    두 노드 a와 b가 속한 집합을 합칩니다.
    """
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 빠른 입력을 위한 설정
input = sys.stdin.readline

while True:
    # m: 집의 수, n: 길의 수
    m, n = map(int, input().split())

    # 입력의 마지막 줄인 '0 0'을 만나면 종료
    if m == 0 and n == 0:
        break

    # 간선 정보를 저장할 리스트와 총 비용을 저장할 변수
    edges = []
    total_cost = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))  # 비용(z)을 기준으로 정렬하기 위해 맨 앞에 추가
        total_cost += z

    # 간선을 비용 순으로 오름차순 정렬
    edges.sort()

    # 각 노드의 부모를 자기 자신으로 초기화 (Union-Find 초기 설정)
    parent = [i for i in range(m)]
    
    # 최소 신장 트리의 비용
    mst_cost = 0

    # 정렬된 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge
        
        # 두 노드가 같은 집합에 속해 있지 않으면 (사이클을 형성하지 않으면)
        if find_parent(parent, a) != find_parent(parent, b):
            # 두 노드를 같은 집합으로 합치고
            union_parent(parent, a, b)
            # 해당 간선의 비용을 mst_cost에 더함
            mst_cost += cost
    
    # 절약할 수 있는 최대 비용 = 전체 비용 - 최소 비용
    savings = total_cost - mst_cost
    print(savings)