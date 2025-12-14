from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    oil_dict = {} # {석유덩어리ID: 석유량}
    oil_id = 1    # 석유 덩어리에 부여할 고유 번호 (1부터 시작)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 1. BFS를 통해 석유 덩어리(Cluster) 탐색 및 ID 부여
    for i in range(n):
        for j in range(m):
            # 석유가 있고, 아직 방문하지 않은 덩어리라면 BFS 시작
            if land[i][j] == 1 and visited[i][j] == 0:
                q = deque([(i, j)])
                visited[i][j] = oil_id
                count = 1
                
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and visited[nx][ny] == 0:
                                visited[nx][ny] = oil_id # 방문 처리 시 ID 기록
                                q.append((nx, ny))
                                count += 1
                
                # 해당 ID의 석유량 저장
                oil_dict[oil_id] = count
                oil_id += 1

    # 2. 각 열(Column)을 지나가며 채굴 가능한 석유량 계산
    max_oil = 0
    
    for j in range(m):
        current_oil = 0
        seen_ids = set() # 현재 열에서 이미 더한 덩어리인지 확인용
        
        for i in range(n):
            if land[i][j] == 1:
                chunk_id = visited[i][j] # 해당 위치의 석유 ID 가져오기
                if chunk_id not in seen_ids:
                    current_oil += oil_dict[chunk_id]
                    seen_ids.add(chunk_id)
        
        if current_oil > max_oil:
            max_oil = current_oil
            
    return max_oil