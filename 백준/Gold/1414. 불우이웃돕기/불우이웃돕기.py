import sys
from functools import lru_cache

input = sys.stdin.readline

hard_coding = {
    '0':0,
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    "A":27,
    "B":28,
    "C":29,
    "D":30,
    "E":31,
    "F":32,
    "G":33,
    "H":34,
    "I":35,
    "J":36,
    "K":37,
    "L":38,
    "M":39,
    "N":40,
    "O":41,
    "P":42,
    "Q":43,
    "R":44,
    "S":45,
    "T":46,
    "U":47,
    "V":48,
    "W":49,
    "X":50,
    "Y":51,
    "Z":52,
}

n = int(input())
min_lan_cable = float('inf')

input_list = []
for _ in range(n):
    input_list.append(list(input().rstrip()))

sum_val = 0
for i in range(n):
    for j in range(n):
        change_code = hard_coding[input_list[i][j]]
        input_list[i][j] = change_code
        sum_val += change_code

# 크루스칼 알고리즘으로 최소 스패닝 트리의 총 비용 찾기
def find_mst_total_cost():
    # n=1인 경우 특별 처리
    if n == 1:
        return input_list[0][0]  # 자기 자신을 연결하는 비용
    
    # 모든 간선을 (비용, 시작점, 끝점) 형태로 저장 (0이 아닌 간선만)
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j and input_list[i][j] != 0:  # 자기 자신으로 가는 간선과 0인 간선은 제외
                edges.append((input_list[i][j], i, j))
    
    # 비용 순으로 정렬
    edges.sort()
    
    # Union-Find를 위한 부모 배열
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    total_cost = 0
    edge_count = 0
    
    # 크루스칼 알고리즘
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += cost
            edge_count += 1
            if edge_count == n - 1:  # MST 완성
                break
    
    # 모든 노드가 연결되었는지 확인
    if edge_count < n - 1:
        return -1  # 모든 노드를 연결할 수 없는 경우
    
    return total_cost

min_lan_cable = find_mst_total_cost()
if min_lan_cable == -1:
    print(-1)
elif n == 1:
    print(sum_val)  # n=1인 경우 자기 자신 비용을 빼지 않음
else:
    print(sum_val - min_lan_cable)