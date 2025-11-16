import sys
from collections import deque

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# n: 섬의 수, m: 다리의 수
n, m = map(int, input().split())

# 인접 리스트로 그래프를 저장합니다. (연결된 섬, 중량제한)
adj = [[] for _ in range(n + 1)]
low, high = 1, 0

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
    # 이분 탐색의 상한선을 입력받은 최대 중량제한으로 설정
    if c > high:
        high = c

# 출발 공장, 도착 공장
start_factory, end_factory = map(int, input().split())

# BFS 함수: 특정 'weight'로 start에서 end까지 갈 수 있는지 확인
def bfs(weight):
    q = deque()
    q.append(start_factory)
    visited = [False] * (n + 1)
    visited[start_factory] = True

    while q:
        current_node = q.popleft()

        # 도착지에 도달했다면 True 반환
        if current_node == end_factory:
            return True

        # 현재 섬(current_node)과 연결된 다리들을 확인
        for next_node, bridge_limit in adj[current_node]:
            # 아직 방문하지 않았고, 다리의 중량제한이 현재 'weight'보다 크거나 같다면
            if not visited[next_node] and bridge_limit >= weight:
                visited[next_node] = True
                q.append(next_node)

    # 큐가 비었는데 도착지에 도달 못했으면 False 반환
    return False

# 이분 탐색 실행
answer = 0
while low <= high:
    mid = (low + high) // 2
    
    # 'mid' 무게로 이동이 가능한지 (BFS) 확인
    if bfs(mid):
        # 이동 가능하다면, 이 무게(mid)를 정답 후보로 저장
        # 그리고 더 무거운 무게도 가능한지 탐색 (low 상향)
        answer = mid
        low = mid + 1
    else:
        # 이동 불가능하다면, 무게를 줄여야 함 (high 하향)
        high = mid - 1

# 최종적으로 저장된 최대 무게 출력
print(answer)