def solution(n, s, a, b, fares):
    # 무한대를 표현하기 위한 큰 값 설정 (지점 개수가 최대 200개이므로 적당히 큰 값)
    INF = float('inf')
    
    # 1. 최단 거리 테이블 초기화 (n x n)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로 가는 비용은 0으로 설정
    for i in range(1, n + 1):
        graph[i][i] = 0
        
    # 2. 주어진 택시 요금(간선 정보) 입력받기
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f  # 양방향 통행 가능
        
    # 3. 플로이드-워셜 알고리즘 수행 (모든 정점에서 모든 정점으로의 최단 거리)
    for k in range(1, n + 1):        # 거쳐가는 노드
        for i in range(1, n + 1):    # 출발 노드
            for j in range(1, n + 1):# 도착 노드
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    # 4. 최적의 환승 지점(i)을 찾으며 최소 비용 갱신
    # 기본값은 합승하지 않고 각자 따로 택시를 타고 가는 경우
    answer = graph[s][a] + graph[s][b]
    
    # 모든 노드를 환승 지점(i)으로 검토
    for i in range(1, n + 1):
        # s -> i (합승) + i -> a (A 각자) + i -> b (B 각자)
        cost = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, cost)
        
    return answer