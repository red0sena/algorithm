from collections import deque

def solution(n, results):
    # 정방향 그래프: graph[a] = [b1, b2, …]  (a가 이긴 선수들)
    # 역방향 그래프: rgraph[b] = [a1, a2, …] (b에게 진 선수들)
    graph = [[] for _ in range(n+1)]
    rgraph = [[] for _ in range(n+1)]
    for a, b in results:
        graph[a].append(b)
        rgraph[b].append(a)
    
    def bfs(start, adj):
        """start에서 출발해 adj 그래프를 따라 도달할 수 있는 모든 노드 수 리턴."""
        visited = [False] * (n+1)
        q = deque([start])
        visited[start] = True
        cnt = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    cnt += 1
                    q.append(v)
        return cnt
    
    answer = 0
    for i in range(1, n+1):
        # i가 이길 수 있는 선수 수 + i에게 이긴 선수 수
        win_cnt = bfs(i, graph)
        lose_cnt = bfs(i, rgraph)
        # 둘을 합쳐 나머지 선수 전원(n-1명)을 모두 알 수 있으면 순위 결정 가능
        if win_cnt + lose_cnt == n - 1:
            answer += 1

    return answer
