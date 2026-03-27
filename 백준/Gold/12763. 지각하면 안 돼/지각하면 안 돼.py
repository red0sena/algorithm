import heapq
import sys

def solve_12763():
    input = sys.stdin.read().split()
    if not input: return
    
    N = int(input[0])
    T, M = int(input[1]), int(input[2])
    L = int(input[3])
    
    adj = [[] for _ in range(N + 1)]
    idx = 4
    for _ in range(L):
        u, v, t, m = map(int, input[idx:idx+4])
        adj[u].append((v, t, m))
        adj[v].append((u, t, m))
        idx += 4
        
    # dist[node][time] = min_cost
    # 시간은 최대 10,000분까지 가능하므로 넉넉하게 설정
    inf = float('inf')
    dist = [[inf] * (T + 1) for _ in range(N + 1)]
    
    # (비용, 현재노드, 소요시간)
    pq = [(0, 1, 0)]
    dist[1][0] = 0
    
    ans = inf
    
    while pq:
        cost, curr, time = heapq.heappop(pq)
        
        if cost > dist[curr][time]: continue
        if curr == N:
            ans = min(ans, cost)
            continue
            
        for nxt, n_t, n_m in adj[curr]:
            total_t = time + n_t
            total_m = cost + n_m
            
            if total_t <= T and total_m <= M:
                if total_m < dist[nxt][total_t]:
                    # 현재 시간 이후의 더 큰 시간대에 대해서도 
                    # 더 비싼 비용으로 저장되어 있다면 갱신 (최적화)
                    dist[nxt][total_t] = total_m
                    heapq.heappush(pq, (total_m, nxt, total_t))
                    
    print(ans if ans != inf else -1)

solve_12763()