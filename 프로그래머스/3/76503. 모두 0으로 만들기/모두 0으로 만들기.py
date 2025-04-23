from collections import deque

def solution(a, edges):
    n = len(a)
    
    # 1. 합이 0인지 확인
    if sum(a) != 0:
        return -1
    if all(x == 0 for x in a):
        return 0
    
    # 2. 인접 리스트 구성
    graph = {i:[] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 3. 루트 0에서 BFS로 부모 배열과 순서를 만든다
    parent = [-1]*n
    order = []
    q = deque([0])
    parent[0] = 0
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    
    # 4. 뒤에서 앞으로 - 후위 순회 효과
    ans = 0
    for u in reversed(order[1:]):          # root 제외
        w = a[u]
        ans += abs(w)
        a[parent[u]] += w                  # 무게를 부모로 이동
        # a[u] = 0  # 굳이 안 바꿔도 됨
    return ans