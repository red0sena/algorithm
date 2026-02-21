import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    out_edge = [0] * (N + 1)
    in_degree = [0] * (N + 1)
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        out_edge[u] = v
        in_degree[v] += 1
        idx += 2
        
    s = int(input_data[idx])
    
    # 1. 세종이의 마니또가 이미 누군지 밝혀진 경우
    if out_edge[s] != 0:
        print("NOJAM")
        return
        
    V_in = []  # 들어오는 간선이 없는 노드들 (지목받아야 할 후보들)
    V_out = [] # 나가는 간선이 없는 노드들 (지목해야 할 노드들)
    
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            V_in.append(i)
        if out_edge[i] == 0:
            V_out.append(i)
            
    # 각 V_out 노드가 어떤 V_in 노드에서 시작했는지(head) 추적
    head_of_out = {}
    for start_node in V_in:
        curr = start_node
        while out_edge[curr] != 0:
            curr = out_edge[curr]
        head_of_out[curr] = start_node # 경로의 끝점(curr)에 시작점(start_node) 매핑
        
    K = len(V_in)
    
    # K가 1이하라면 연결할 수 있는 경우의 수가 무조건 1개뿐임
    if K <= 1:
        print("NOJAM")
        return
        
    head_s = head_of_out[s]
    ans = 0
    
    # 2. 세종이가 지목할 수 있는 대상(v) 탐색
    for v in V_in:
        if v == s:
            # 스스로를 마니또로 지목할 수 없음
            continue
            
        if v == head_s:
            # 자신의 경로 시작점을 지목하여 사이클을 닫는 경우
            if K == 2:
                # 남은 경로가 1개일 때, 그 남은 경로가 단일 노드인지 확인
                other_in = [x for x in V_in if x != head_s][0]
                other_out = [x for x in V_out if x != s][0]
                
                # 남은 1명의 학생이 고립된 상태라면 자가 지목을 하게 되므로 불가능
                if other_in == other_out:
                    continue
            ans += 1
        else:
            # 다른 경로의 시작점을 지목하는 경우는 항상 가능
            ans += 1
            
    # 3. 정답 출력 (가능한 사람이 1명이면 NOJAM)
    if ans == 1:
        print("NOJAM")
    else:
        print(ans)

if __name__ == '__main__':
    solve()