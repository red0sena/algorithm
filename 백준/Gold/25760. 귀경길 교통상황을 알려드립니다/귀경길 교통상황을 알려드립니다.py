import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cars = list(map(int, input().split()))

# 1번 정점을 루트로 하여 각 정점의 깊이(= 톨게이트까지 거리) 계산
depth = [-1] * (N + 1)
depth[1] = 0
stack = [1]

while stack:
    cur = stack.pop()
    for nxt in graph[cur]:
        if depth[nxt] == -1:
            depth[nxt] = depth[cur] + 1
            stack.append(nxt)

# 차가 있는 정점들의 도착 시간 수집
arrivals = []
for i in range(1, N + 1):
    if cars[i - 1] == 1:
        arrivals.append(depth[i])

# 도착 순서대로 처리
arrivals.sort()

ans = 0
for t in arrivals:
    ans = max(ans, t) + 1

print(ans)