import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def solve():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        # 소수점 방지를 위해 거리를 2배로 설정
        adj[u].append((v, w * 2))
        adj[v].append((u, w * 2))

    # 여우의 다익스트라
    dist_fox = [INF] * (N + 1)
    dist_fox[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, curr = heapq.heappop(pq)
        if dist_fox[curr] < d:
            continue
        for nxt, weight in adj[curr]:
            if dist_fox[nxt] > d + weight:
                dist_fox[nxt] = d + weight
                heapq.heappush(pq, (dist_fox[nxt], nxt))

    # 늑대의 다익스트라 (상태: 0은 다음 차례에 빠르게, 1은 다음 차례에 느리게)
    # dist_wolf[node][0] -> 해당 노드에 '느리게' 도착한 상태 (즉, 다음엔 빠르게 달릴 상태)
    # dist_wolf[node][1] -> 해당 노드에 '빠르게' 도착한 상태 (즉, 다음엔 느리게 달릴 상태)
    dist_wolf = [[INF] * 2 for _ in range(N + 1)]
    dist_wolf[1][0] = 0
    pq = [(0, 1, 0)] # (거리, 현재노드, 다음상태)

    while pq:
        d, curr, state = heapq.heappop(pq)
        
        if dist_wolf[curr][state] < d:
            continue
        
        for nxt, weight in adj[curr]:
            if state == 0: # 이번에 빠르게 달릴 차례
                next_dist = d + weight // 2
                next_state = 1
            else: # 이번에 느리게 달릴 차례
                next_dist = d + weight * 2
                next_state = 0
                
            if dist_wolf[nxt][next_state] > next_dist:
                dist_wolf[nxt][next_state] = next_dist
                heapq.heappush(pq, (next_dist, nxt, next_state))

    # 결과 계산
    ans = 0
    for i in range(2, N + 1):
        if dist_fox[i] < min(dist_wolf[i]):
            ans += 1
    print(ans)

solve()