from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    # 인접 리스트로 양방향 그래프 구성
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS로 destination에서 각 노드까지의 최단 거리 계산
    distances = [-1] * (n + 1)  # 1부터 n까지의 노드를 위해
    distances[destination] = 0
    queue = deque([destination])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        # 현재 노드와 연결된 이웃 노드 탐색
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 경우
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    # sources에 대해 결과 생성
    result = [distances[source] for source in sources]
    return result

# 테스트용 코드 (입출력 예 처리)