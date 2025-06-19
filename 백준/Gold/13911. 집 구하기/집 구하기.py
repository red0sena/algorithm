import sys
import heapq

def multi_source_dijkstra(sources, adj, INF):
    V = len(adj) - 1
    dist = [INF] * (V + 1)
    pq = []
    # 초기화: 모든 source 의 거리를 0으로
    for s in sources:
        dist[s] = 0
        heapq.heappush(pq, (0, s))
    # 표준 다익스트라
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    # 맥도날드 정보
    M, x = map(int, input().split())
    mcds = list(map(int, input().split()))
    # 스타벅스 정보
    S, y = map(int, input().split())
    stars = list(map(int, input().split()))

    INF = 10**18
    # 맥도날드들로부터의 최단 거리
    dist_M = multi_source_dijkstra(mcds, adj, INF)
    # 스타벅스들로부터의 최단 거리
    dist_S = multi_source_dijkstra(stars, adj, INF)

    # 맥도날드나 스타벅스가 아닌 정점을 집 후보로
    forbidden = set(mcds) | set(stars)

    ans = INF
    for v in range(1, V + 1):
        if v in forbidden:
            continue
        if dist_M[v] <= x and dist_S[v] <= y:
            ans = min(ans, dist_M[v] + dist_S[v])

    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()
