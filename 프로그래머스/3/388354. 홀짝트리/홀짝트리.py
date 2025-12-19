from collections import deque

def solution(nodes, edges):
    # nodes의 최대값이 크더라도, nodes에 포함된 값만 쓰므로 dict 기반도 가능하지만
    # 프로그래머스에선 보통 1..N 형태라 가정하고 max를 사용
    max_node = max(nodes) if nodes else 0

    adj = [[] for _ in range(max_node + 1)]
    deg = [0] * (max_node + 1)
    in_nodes = [False] * (max_node + 1)
    for v in nodes:
        in_nodes[v] = True

    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
        deg[a] += 1
        deg[b] += 1

    visited = [False] * (max_node + 1)

    reverse_tree = 0   # 홀짝 트리 가능 개수
    odd_even_tree = 0  # 역홀짝 트리 가능 개수

    for start in nodes:
        if visited[start]:
            continue

        # 연결요소(트리) 하나 BFS
        q = deque([start])
        visited[start] = True

        y_cnt = 0  # (루트 아님 가정)에서 홀짝노드(Y): node_parity == (deg-1)_parity
        r_cnt = 0  # (루트 아님 가정)에서 역홀짝노드(R): node_parity != (deg-1)_parity

        while q:
            v = q.popleft()

            node_parity = v & 1
            child_parity_if_not_root = (deg[v] - 1) & 1  # 루트가 아니면 자식 수 = deg-1 (parity만 필요)

            if node_parity == child_parity_if_not_root:
                y_cnt += 1
            else:
                r_cnt += 1

            for nx in adj[v]:
                if in_nodes[nx] and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)

        # 이 연결요소(트리)가 될 수 있는지 판정
        # 홀짝 트리: 루트만 R이어야 (루트가 되면 R->Y로 뒤집혀서 전부 Y)
        if r_cnt == 1:
            reverse_tree += 1

        # 역홀짝 트리: 루트만 Y이어야 (루트가 되면 Y->R로 뒤집혀서 전부 R)
        if y_cnt == 1:
            odd_even_tree += 1

    return [reverse_tree, odd_even_tree]