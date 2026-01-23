import sys

# 입력 속도 향상
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solve():
    n = int(input())
    planets = []
    
    for i in range(n):
        x, y, z = map(int, input().split())
        # 정렬 후에도 원래 행성 번호를 알기 위해 i를 함께 저장
        planets.append((x, y, z, i))
        
    edges = []
    
    # 3개의 축(x, y, z) 각각에 대해 정렬 후 인접 간선 추출
    # k=0: x좌표, k=1: y좌표, k=2: z좌표
    for k in range(3):
        # 해당 좌표 기준으로 정렬
        planets.sort(key=lambda x: x[k])
        
        # 인접한 행성들끼리의 간선 정보 추가
        for i in range(n - 1):
            # 비용: 현재 좌표(k)의 차이 절대값
            cost = abs(planets[i][k] - planets[i+1][k])
            # (비용, 행성A번호, 행성B번호)
            edges.append((cost, planets[i][3], planets[i+1][3]))
            
    # 크루스칼 알고리즘 시작
    # 1. 간선을 비용 오름차순으로 정렬
    edges.sort()
    
    # 2. Union-Find 초기화
    parent = [i for i in range(n)]
    total_cost = 0
    count = 0
    
    # 3. 사이클이 생기지 않는 간선 선택
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            count += 1
            
            # n-1개의 간선이 선택되면 MST 완성 (조기 종료)
            if count == n - 1:
                break
                
    print(total_cost)

if __name__ == "__main__":
    solve()