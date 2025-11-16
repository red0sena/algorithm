import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N(동영상 수), Q(질문 수) 입력
N, Q = map(int, input().split())

# 그래프를 인접 리스트로 표현
# graph[i] = [(j, r), (k, s)] 
# -> i번 노드는 j와 USADO 'r'로, k와 USADO 's'로 연결됨
graph = [[] for _ in range(N + 1)]

# N-1개의 연결 정보 입력 (트리)
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    # 양방향으로 연결 정보 추가
    graph[p].append((q, r))
    graph[q].append((p, r))

# Q개의 질문(쿼리) 처리
for _ in range(Q):
    k, v = map(int, input().split())
    
    # k: USADO 임계값
    # v: 시작 동영상
    
    count = 0  # 추천될 동영상의 수
    
    # BFS(너비 우선 탐색)를 위한 큐와 방문 기록
    queue = deque([v])
    visited = [False] * (N + 1)
    visited[v] = True  # 시작 노드 방문 처리
    
    while queue:
        current_node = queue.popleft()
        
        # 현재 노드와 연결된 다른 노드들 확인
        for neighbor, relevance in graph[current_node]:
            
            # 1. 아직 방문하지 않았고,
            # 2. 연결된 경로의 USADO(relevance)가 k 이상인 경우
            if not visited[neighbor] and relevance >= k:
                
                # 방문 처리
                visited[neighbor] = True
                # 큐에 추가하여 다음 탐색 대상으로 삼음
                queue.append(neighbor)
                # 추천 동영상 개수 증가
                count += 1
                
    # 현재 쿼리(k, v)에 대한 결과 출력
    print(count)