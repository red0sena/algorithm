import sys

# 파이썬 재귀 한도 해제 및 빠른 입력
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

# 다리 정보를 가중치(무게 제한) 기준 내림차순으로 입력과 동시에 정렬 (-x[2])
edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x: -x[2])

# 유니온 파인드용 부모 배열
p = list(range(N + 1))

# 루트 노드 찾기 (경로 압축)
def find(x):
    if p[x] != x: 
        p[x] = find(p[x])
    return p[x]

# 무거운 다리부터 차례대로 연결 (최대 스패닝 트리)
for u, v, w in edges:
    # 두 섬 연결 (Union)
    p[find(u)] = find(v)
    
    # S와 E가 방금 연결되었다면, 현재 다리 무게(w)가 정답!
    if find(S) == find(E):
        print(w)
        exit()

# 모든 다리를 연결해도 S와 E가 안 이어지면 0 출력
print(0)