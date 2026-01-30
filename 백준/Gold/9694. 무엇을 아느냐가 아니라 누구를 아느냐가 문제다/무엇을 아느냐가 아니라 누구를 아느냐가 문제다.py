import sys
import heapq

# 입력 속도 향상
input = sys.stdin.readline

def solve():
    # 전체 테스트 케이스 개수
    t = int(input())

    for case_num in range(1, t + 1):
        # n: 관계의 개수(간선), m: 사람의 수(노드)
        n, m = map(int, input().split())
        
        # 인접 리스트 생성 (양방향 그래프)
        graph = [[] for _ in range(m)]
        for _ in range(n):
            u, v, cost = map(int, input().split())
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        # 다익스트라 초기화
        # dist: 최단 거리 저장, parent: 경로 복원용 이전 노드 저장
        dist = [float('inf')] * m
        parent = [-1] * m
        
        # 시작점 설정 (0번 노드)
        dist[0] = 0
        pq = [(0, 0)]  # (비용, 현재 노드)

        while pq:
            d, cur = heapq.heappop(pq)

            # 이미 처리된 거리보다 더 긴 경로라면 패스
            if dist[cur] < d:
                continue

            # 인접 노드 탐색
            for nxt, weight in graph[cur]:
                new_cost = d + weight
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    parent[nxt] = cur  # 어디서 왔는지 기록 (핵심)
                    heapq.heappush(pq, (new_cost, nxt))

        # 출력 형식 준비
        print(f"Case #{case_num}:", end=" ")

        # 도착점(M-1)에 도달하지 못한 경우
        if dist[m - 1] == float('inf'):
            print(-1)
        else:
            # 역추적: 도착점부터 시작점까지 거슬러 올라감
            path = []
            curr = m - 1
            while curr != -1:
                path.append(curr)
                curr = parent[curr]
            
            # 경로가 역순(M-1 -> ... -> 0)으로 담겼으므로 뒤집어서 출력
            print(*path[::-1])

if __name__ == "__main__":
    solve()