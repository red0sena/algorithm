import collections

def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    # 각 수레의 시작점과 도착점 좌표 찾기
    red_start, blue_start = [], []
    red_end, blue_end = [], []
    
    for r in range(n):
        for c in range(m):
            if maze[r][c] == 1: red_start = [r, c]
            elif maze[r][c] == 2: blue_start = [r, c]
            elif maze[r][c] == 3: red_end = [r, c]
            elif maze[r][c] == 4: blue_end = [r, c]

    # (r, c) 좌표를 비트로 변환하는 함수
    def pos_to_bit(r, c):
        return 1 << (r * m + c)

    # BFS를 위한 큐 초기화
    # 상태: (빨간_r, 빨간_c, 파란_r, 파란_c, 빨간_마스크, 파란_마스크, 턴_수)
    q = collections.deque([(
        red_start[0], red_start[1], 
        blue_start[0], blue_start[1], 
        pos_to_bit(red_start[0], red_start[1]), 
        pos_to_bit(blue_start[0], blue_start[1]), 
        0
    )])
    
    # 방문 기록을 위한 set: (빨간_r, 빨간_c, 파란_r, 파란_c, 빨간_마스크, 파란_마스크)
    visited = set()
    visited.add((
        red_start[0], red_start[1], 
        blue_start[0], blue_start[1], 
        pos_to_bit(red_start[0], red_start[1]), 
        pos_to_bit(blue_start[0], blue_start[1])
    ))
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        rr, rc, br, bc, r_mask, b_mask, count = q.popleft()

        if rr == red_end[0] and rc == red_end[1] and br == blue_end[0] and bc == blue_end[1]:
            return count

        # 모든 이동 조합 탐색
        for i in range(4):
            is_red_at_end = (rr == red_end[0] and rc == red_end[1])
            nrr, nrc = (rr, rc) if is_red_at_end else (rr + dr[i], rc + dc[i])

            for j in range(4):
                is_blue_at_end = (br == blue_end[0] and bc == blue_end[1])
                nbr, nbc = (br, bc) if is_blue_at_end else (br + dr[j], bc + dc[j])

                # 1. 격자 밖 또는 벽 체크
                if not (0 <= nrr < n and 0 <= nrc < m and maze[nrr][nrc] != 5): continue
                if not (0 <= nbr < n and 0 <= nbc < m and maze[nbr][nbc] != 5): continue

                # 2. ❗❗ (핵심 수정) 각 수레가 자신의 방문했던 칸으로 이동하는지 체크
                # 단, 도착해서 멈춰있는 경우는 예외
                if not is_red_at_end and (r_mask & pos_to_bit(nrr, nrc)): continue
                if not is_blue_at_end and (b_mask & pos_to_bit(nbr, nbc)): continue

                # 3. 두 수레가 같은 칸으로 이동 (충돌)
                if nrr == nbr and nrc == nbc: continue
                
                # 4. 두 수레가 자리를 교체
                if nrr == br and nrc == bc and nbr == rr and nbc == rc: continue

                # 새로운 방문 마스크 계산
                nr_mask = r_mask | pos_to_bit(nrr, nrc)
                nb_mask = b_mask | pos_to_bit(nbr, nbc)

                # 5. 현재 위치와 방문 기록(마스크)이 모두 동일한 상태를 방문했는지 체크
                if (nrr, nrc, nbr, nbc, nr_mask, nb_mask) in visited: continue
                
                visited.add((nrr, nrc, nbr, nbc, nr_mask, nb_mask))
                q.append((nrr, nrc, nbr, nbc, nr_mask, nb_mask, count + 1))
                
    return 0