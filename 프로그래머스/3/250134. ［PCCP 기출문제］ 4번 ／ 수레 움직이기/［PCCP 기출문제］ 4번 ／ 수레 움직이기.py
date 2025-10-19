from collections import deque

WALL = 5
RED_START, BLUE_START, RED_END, BLUE_END = 1, 2, 3, 4

def solution(maze):
    n, m = len(maze), len(maze[0])

    # 시작 / 도착 위치 찾기
    red_s = blue_s = red_e = blue_e = None
    for r in range(n):
        for c in range(m):
            v = maze[r][c]
            if v == RED_START: red_s = (r, c)
            elif v == BLUE_START: blue_s = (r, c)
            elif v == RED_END: red_e = (r, c)
            elif v == BLUE_END: blue_e = (r, c)

    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    # 각 말의 방문 경로를 2D 리스트로 관리하기 위해, 상태를 visited set으로 묶음
    # visited = {(red_pos, blue_pos, tuple of red visited map, tuple of blue visited map)}
    def copy_board(board):
        # 방문 배열을 불변형(tuple of tuple)으로 만들어 visited에 넣기 위해
        return tuple(tuple(row) for row in board)

    # 초기 방문 상태
    red_visited = [[False]*m for _ in range(n)]
    blue_visited = [[False]*m for _ in range(n)]
    rr, rc = red_s
    br, bc = blue_s
    red_visited[rr][rc] = True
    blue_visited[br][bc] = True

    q = deque([(red_s, blue_s, red_visited, blue_visited, 0)])
    visited = {(red_s, blue_s, copy_board(red_visited), copy_board(blue_visited))}

    while q:
        (rr, rc), (br, bc), rmap, bmap, turns = q.popleft()

        if (rr, rc) == red_e and (br, bc) == blue_e:
            return turns

        for dr_r, dc_r in dirs:
            # 빨강 이동
            if (rr, rc) == red_e:
                nR = (rr, rc)
            else:
                nR = (rr + dr_r, rc + dc_r)
            if not (0 <= nR[0] < n and 0 <= nR[1] < m): continue
            if maze[nR[0]][nR[1]] == WALL: continue
            if (rr, rc) != red_e and rmap[nR[0]][nR[1]]: continue

            for dr_b, dc_b in dirs:
                # 파랑 이동
                if (br, bc) == blue_e:
                    nB = (br, bc)
                else:
                    nB = (br + dr_b, bc + dc_b)
                if not (0 <= nB[0] < n and 0 <= nB[1] < m): continue
                if maze[nB[0]][nB[1]] == WALL: continue
                if (br, bc) != blue_e and bmap[nB[0]][nB[1]]: continue

                # 충돌 / 교차 금지
                if nR == nB: continue
                if nR == (br, bc) and nB == (rr, rc): continue

                # 새 방문 배열 복사
                new_rmap = [row[:] for row in rmap]
                new_bmap = [row[:] for row in bmap]
                new_rmap[nR[0]][nR[1]] = True
                new_bmap[nB[0]][nB[1]] = True

                state = (nR, nB, copy_board(new_rmap), copy_board(new_bmap))
                if state in visited:
                    continue
                visited.add(state)
                q.append((nR, nB, new_rmap, new_bmap, turns + 1))

    return 0