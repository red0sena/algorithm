import sys

# 파이썬 재귀 최대 깊이 설정
sys.setrecursionlimit(200000)

# 시간 초과 방지를 위해 input() 함수를 빠른 입력으로 덮어씌우기
input = sys.stdin.readline

def solve():
    # 첫 줄 입력 받기 (N: 노드 개수, S: 출발점, D: 힘)
    N, S, D = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]
    
    # N-1개의 간선 정보 입력 받기
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (N + 1)
    move_count = 0
    
    # DFS 함수
    def dfs(node):
        nonlocal move_count
        visited[node] = True
        max_leaf_depth = 0
        
        for nxt in graph[node]:
            if not visited[nxt]:
                # 자식 노드 탐색 후, 리프까지의 깊이 계산
                child_depth = dfs(nxt)
                max_leaf_depth = max(max_leaf_depth, child_depth + 1)
        
        # 시작 노드가 아니면서 리프 노드까지의 최대 깊이가 D 이상이면 방문 필요
        if node != S and max_leaf_depth >= D:
            move_count += 1
            
        return max_leaf_depth
        
    # 탐색 시작
    dfs(S)
    
    # 왕복이므로 지나간 간선 수에 2를 곱해서 출력
    print(move_count * 2)

if __name__ == '__main__':
    solve()